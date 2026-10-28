"""Missing CIA and PS2 raw-CD readers for the sigil bundled with RomM 5.4.0."""

import ctypes
import os
import re
from dataclasses import replace
from pathlib import Path

import sigil
import sigil._sigil

# 3dbrew Title metadata and Ticket: signed-body offsets by signature type.
SIGNATURE_BODY = {
    0x10000: 0x240, 0x10001: 0x140, 0x10002: 0x80,
    0x10003: 0x240, 0x10004: 0x140, 0x10005: 0x80,
}


def _signed_title_id(stream, offset: int, field: int) -> str:
    stream.seek(offset)
    raw = stream.read(4)
    body = SIGNATURE_BODY.get(int.from_bytes(raw, 'big'))
    if len(raw) != 4 or body is None:
        raise ValueError('Unsupported CIA signature type')
    stream.seek(offset + body)
    if stream.read(4) != b'Root':
        raise ValueError('Invalid CIA issuer')
    stream.seek(offset + body + field)
    title_id = stream.read(8)
    if len(title_id) != 8 or not title_id.hex().startswith('0004'):
        raise ValueError('Invalid CIA title ID')
    return title_id.hex().upper()


def _cia(path: Path):
    align = lambda n: (n + 63) // 64 * 64
    with path.open('rb') as stream:
        header = stream.read(32)
        sizes = [int.from_bytes(header[a:a+4], 'little') for a in (0, 8, 12, 16)]
        size, cert, ticket, tmd = sizes
        if len(header) != 32 or size != 0x2020 or not all((cert, ticket, tmd)):
            raise ValueError('Invalid CIA header')
        ticket_at = align(size) + align(cert)
        tmd_at = ticket_at + align(ticket)
        if tmd_at + tmd > path.stat().st_size:
            raise ValueError('Truncated CIA metadata')
        ticket_id = _signed_title_id(stream, ticket_at, 0x9C)
        title_id = _signed_title_id(stream, tmd_at, 0x4C)
        if title_id != ticket_id:
            raise ValueError('CIA ticket and TMD disagree on title ID')
    result = sigil.SigilResult.persisted(
        '3ds', title_id, f'{title_id[:8].lower()}/{title_id[8:].lower()}', 0
    )
    return replace(result, usage='folder-split')


def _raw_ps2(path: Path):
    # Reuse sigil's own raw-sector reader, ISO9660 parser and BOOT2 parser.
    # The bundled path dispatcher only selects the raw reader for PSX/DC.
    ffi = sigil.ffi
    library = ctypes.CDLL(sigil._sigil.__file__)
    open_reader = ffi.cast(
        'sigil_io *(*)(const char *)',
        ctypes.cast(library.sigil_io_open_raw_cd, ctypes.c_void_p).value,
    )
    extract = ffi.cast(
        'int(*)(const sigil_io *,const char *,sigil_platform,const sigil_options *,sigil_result *)',
        ctypes.cast(library.sigil_extract_from_io, ctypes.c_void_p).value,
    )
    reader = open_reader(os.fsencode(path))
    if reader == ffi.NULL:
        raise OSError(f'Cannot open PS2 track: {path.name}')
    out = ffi.new('sigil_result *')
    out.struct_version = sigil.lib.SIGIL_RESULT_V3
    opts = ffi.new('sigil_options *')
    opts.struct_version = sigil.lib.SIGIL_OPTIONS_V1
    try:
        status = extract(reader, os.fsencode(path.name), sigil.platform_from_slug('ps2'), opts, out)
        if status != sigil.lib.SIGIL_OK:
            # Use the public reader to produce sigil's normal typed error.
            return sigil.extract(path, platform='ps2', filename_fallback=False)
        result = sigil.SigilResult.persisted(
            'ps2', ffi.string(out.title_id).decode(), ffi.string(out.save_id).decode(), 0
        )
        return replace(result, usage='folder-prefix')
    finally:
        sigil.lib.sigil_io_close(reader)


def extract_title_id(path: str, platform: str):
    file = Path(path)
    if platform == '3ds' and file.suffix.lower() == '.cia':
        return _cia(file)
    if platform == 'ps2':
        if file.suffix.lower() == '.cue':
            refs = re.findall(r'^\s*FILE\s+"([^"]+)"', file.read_text(), re.M | re.I)
            if not refs:
                raise ValueError('PS2 CUE has no quoted FILE reference')
            track = (file.parent / refs[0]).resolve()
            if not track.is_relative_to(file.parent.resolve()) or track.suffix.lower() != '.bin':
                raise ValueError('PS2 CUE track must be a BIN within the game folder')
            file = track
        if file.suffix.lower() == '.bin':
            return _raw_ps2(file)
    return sigil.extract(file, platform=platform, filename_fallback=False)
