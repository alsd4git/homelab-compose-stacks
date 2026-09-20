#!/usr/bin/env python3
"""Read and write ArrMatey v0.9.x encrypted backups.

The format matches ArrMatey's Android implementation:
Base64(salt[16] + iv[16] + AES-256-CBC(ciphertext)), with a PBKDF2-HMAC-SHA256
key derived from the password using 65,536 iterations.
"""

from __future__ import annotations

import argparse
import base64
import getpass
import hashlib
import json
import os
import secrets
import subprocess
import sys
import tempfile
from pathlib import Path


SALT_LENGTH = 16
IV_LENGTH = 16
ITERATIONS = 65_536
KEY_LENGTH = 32


def password_from_args(args: argparse.Namespace) -> str:
    if args.password_file:
        password = Path(args.password_file).read_text(encoding="utf-8").rstrip("\r\n")
    elif args.password_env:
        password = os.environ.get(args.password_env, "")
    elif args.password is not None:
        password = args.password
    else:
        password = getpass.getpass("ArrMatey backup password: ")

    if not password:
        raise ValueError("the password is empty")
    return password


def derive_key(password: str, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        ITERATIONS,
        KEY_LENGTH,
    )


def run_cipher(operation: str, source: Path, destination: Path, key: bytes, iv: bytes) -> None:
    command = ["openssl", "enc"]
    if operation:
        command.append(operation)
    command += [
        "-aes-256-cbc",
        "-K",
        key.hex(),
        "-iv",
        iv.hex(),
        "-in",
        str(source),
        "-out",
        str(destination),
    ]
    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
    except FileNotFoundError as exc:
        raise RuntimeError("openssl is required but was not found") from exc
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or "").strip()
        raise RuntimeError(detail or "OpenSSL could not process the backup") from exc


def write_new(path: Path, data: bytes, force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(f"refusing to overwrite {path}; use --force")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    path.chmod(0o600)


def decrypt_backup(source: Path, destination: Path, password: str, force: bool) -> dict:
    try:
        encoded = b"".join(source.read_bytes().split())
        combined = base64.b64decode(encoded, validate=True)
    except (OSError, ValueError) as exc:
        raise ValueError(f"invalid ArrMatey Base64 backup: {source}") from exc

    if len(combined) <= SALT_LENGTH + IV_LENGTH:
        raise ValueError("backup is shorter than the ArrMatey header")

    salt = combined[:SALT_LENGTH]
    iv = combined[SALT_LENGTH : SALT_LENGTH + IV_LENGTH]
    ciphertext = combined[SALT_LENGTH + IV_LENGTH :]
    key = derive_key(password, salt)

    with tempfile.TemporaryDirectory(prefix="arrmatey-decrypt-") as workdir:
        encrypted_path = Path(workdir) / "cipher.bin"
        plain_path = Path(workdir) / "plain.json"
        encrypted_path.write_bytes(ciphertext)
        run_cipher("-d", encrypted_path, plain_path, key, iv)
        plain = plain_path.read_text(encoding="utf-8")

    try:
        document = json.loads(plain)
    except json.JSONDecodeError as exc:
        raise ValueError("password was accepted by AES, but the result is not JSON") from exc

    if not isinstance(document, dict) or not {"version", "instances", "downloadClients"}.issubset(document):
        raise ValueError("decrypted data does not look like an ArrMatey backup")

    formatted = json.dumps(document, ensure_ascii=False, indent=2) + "\n"
    write_new(destination, formatted.encode("utf-8"), force)
    return document


def encrypt_backup(source: Path, destination: Path, password: str, force: bool) -> dict:
    try:
        document = json.loads(source.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"input is not readable JSON: {source}") from exc

    if not isinstance(document, dict) or not {"version", "instances", "downloadClients"}.issubset(document):
        raise ValueError("JSON does not look like an ArrMatey backup")

    salt = secrets.token_bytes(SALT_LENGTH)
    iv = secrets.token_bytes(IV_LENGTH)
    key = derive_key(password, salt)

    with tempfile.TemporaryDirectory(prefix="arrmatey-encrypt-") as workdir:
        plain_path = Path(workdir) / "plain.json"
        encrypted_path = Path(workdir) / "cipher.bin"
        plain_path.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
        run_cipher("", plain_path, encrypted_path, key, iv)
        encrypted = encrypted_path.read_bytes()

    encoded = base64.b64encode(salt + iv + encrypted)
    write_new(destination, encoded, force)
    return document


def summary(document: dict) -> dict:
    return {
        "version": document.get("version"),
        "instances": [
            {
                "type": item.get("type"),
                "label": item.get("label"),
                "url": item.get("url"),
                "enabled": item.get("enabled"),
                "hasApiKey": bool(item.get("apiKey")),
                "localNetworkEnabled": item.get("localNetworkEnabled"),
                "preferences": item.get("preferences") is not None,
            }
            for item in document.get("instances", [])
        ],
        "downloadClients": [
            {
                "type": item.get("type"),
                "label": item.get("label"),
                "url": item.get("url"),
                "hasUsername": bool(item.get("username")),
                "hasPassword": bool(item.get("password")),
                "hasApiKey": bool(item.get("apiKey")),
            }
            for item in document.get("downloadClients", [])
        ],
        "hasGlobalPreferences": document.get("globalPreferences") is not None,
    }


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("command", choices=("decrypt", "encrypt", "inspect"))
    p.add_argument("source", type=Path)
    p.add_argument("destination", type=Path, nargs="?")
    p.add_argument("--password-file", type=Path)
    p.add_argument("--password-env")
    p.add_argument("--password")
    p.add_argument("--force", action="store_true")
    return p


def main() -> int:
    args = parser().parse_args()
    try:
        password = password_from_args(args)
        if args.command == "inspect":
            with tempfile.TemporaryDirectory(prefix="arrmatey-inspect-") as workdir:
                document = decrypt_backup(args.source, Path(workdir) / "plain.json", password, False)
            print(json.dumps(summary(document), ensure_ascii=False, indent=2))
            return 0

        if args.destination is None:
            raise ValueError("a destination path is required for encrypt/decrypt")
        if args.command == "decrypt":
            document = decrypt_backup(args.source, args.destination, password, args.force)
        else:
            document = encrypt_backup(args.source, args.destination, password, args.force)
        print(json.dumps(summary(document), ensure_ascii=False, indent=2))
        return 0
    except (FileExistsError, OSError, RuntimeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
