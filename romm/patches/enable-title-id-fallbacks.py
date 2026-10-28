"""Connect the verified compatibility readers to RomM 5.4.0's sigil adapter."""

import ast
import hashlib
from pathlib import Path

path = Path('/backend/adapters/services/sigil.py')
source = path.read_text()
expected = '6bce62451966fd90a0b48905a6d3b661e0bd82d83b4d0e193c53f771df6d5660'
if hashlib.sha256(source.encode()).hexdigest() != expected:
    raise SystemExit('Unsupported RomM sigil adapter; review this patch before upgrading')

old = '''            result = await asyncio.to_thread(
                sigil.extract, file_path, platform=sigil_slug, filename_fallback=False
            )'''
new = '''            from adapters.services.title_id_fallbacks import extract_title_id

            result = await asyncio.to_thread(extract_title_id, file_path, sigil_slug)'''
assert source.count(old) == 1
source = source.replace(old, new, 1)
# The CFFI binding's codes are integers, while the old adapter compares names.
old = '            if code in ROUTINE_SIGIL_ERROR_CODES:'
new = '''            if code in ROUTINE_SIGIL_ERROR_CODES or isinstance(
                exc, (sigil.SigilNotFoundError, sigil.SigilUnsupportedFormatError, sigil.SigilNeedsKeyError)
            ):'''
assert source.count(old) == 1
source = source.replace(old, new, 1)
ast.parse(source)
path.write_text(source)
