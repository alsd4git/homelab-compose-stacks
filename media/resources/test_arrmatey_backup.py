"""Tests for ArrMatey backup codec compatibility and safe inspection."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import arrmatey_backup


PASSWORD = "test-only-arrmatey-password"


class ArrMateyBackupTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.root = Path(self.temp_dir.name)

    def round_trip(self, document: dict) -> dict:
        source = self.root / "backup.json"
        encrypted = self.root / "backup.enc.json"
        decrypted = self.root / "decrypted.json"
        source.write_text(json.dumps(document), encoding="utf-8")

        arrmatey_backup.encrypt_backup(source, encrypted, PASSWORD, force=False)
        result = arrmatey_backup.decrypt_backup(
            encrypted, decrypted, PASSWORD, force=False
        )

        self.assertEqual(result, document)
        self.assertEqual(json.loads(decrypted.read_text(encoding="utf-8")), document)
        return result

    def test_legacy_backup_round_trips_without_custom_webpages(self) -> None:
        legacy = {
            "version": 1,
            "instances": [
                {
                    "type": "Sonarr",
                    "label": "Series",
                    "url": "http://sonarr:8989",
                    "apiKey": "instance-secret",
                }
            ],
            "downloadClients": [],
            "globalPreferences": {"useServiceNavLogos": True},
        }

        result = self.round_trip(legacy)

        self.assertNotIn("customWebpages", result)
        self.assertEqual(arrmatey_backup.summary(result)["customWebpages"], [])

    def test_new_backup_preserves_custom_webpages_headers_and_unknown_fields(self) -> None:
        modern = {
            "version": 1,
            "instances": [],
            "downloadClients": [],
            "customWebpages": [
                {
                    "name": "Private service",
                    "url": "https://service.example.test",
                    "headers": [
                        {"key": "Authorization", "value": "Bearer very-secret-value"},
                        {"key": "X-Service-Token", "value": "another-secret-value"},
                    ],
                    "futureWebpageOption": {"enabled": True},
                }
            ],
            "futureTopLevelField": [1, "preserve me"],
        }

        result = self.round_trip(modern)
        summary_json = json.dumps(arrmatey_backup.summary(result))
        webpage_summary = arrmatey_backup.summary(result)["customWebpages"][0]

        self.assertEqual(result["customWebpages"], modern["customWebpages"])
        self.assertEqual(result["futureTopLevelField"], modern["futureTopLevelField"])
        self.assertEqual(webpage_summary["name"], "Private service")
        self.assertEqual(webpage_summary["url"], "https://service.example.test")
        self.assertEqual(webpage_summary["headerCount"], 2)
        self.assertNotIn("Authorization", summary_json)
        self.assertNotIn("Bearer very-secret-value", summary_json)
        self.assertNotIn("another-secret-value", summary_json)

    def test_wrong_password_fails_without_writing_plaintext(self) -> None:
        source = self.root / "backup.json"
        encrypted = self.root / "backup.enc.json"
        destination = self.root / "wrong-password.json"
        source.write_text(
            json.dumps({"version": 1, "instances": [], "downloadClients": []}),
            encoding="utf-8",
        )
        arrmatey_backup.encrypt_backup(source, encrypted, PASSWORD, force=False)

        with self.assertRaises((RuntimeError, ValueError)):
            arrmatey_backup.decrypt_backup(
                encrypted, destination, "incorrect-password", force=False
            )

        self.assertFalse(destination.exists())

    def test_malformed_ciphertext_is_rejected(self) -> None:
        malformed = self.root / "malformed.enc.json"
        malformed.write_text("not valid base64!", encoding="ascii")

        with self.assertRaisesRegex(ValueError, "invalid ArrMatey Base64"):
            arrmatey_backup.decrypt_backup(
                malformed, self.root / "out.json", PASSWORD, force=False
            )

        malformed.write_text("YQ==", encoding="ascii")
        with self.assertRaisesRegex(ValueError, "shorter than the ArrMatey header"):
            arrmatey_backup.decrypt_backup(
                malformed, self.root / "out.json", PASSWORD, force=False
            )


if __name__ == "__main__":
    unittest.main()
