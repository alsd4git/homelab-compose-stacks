"""Apply a source-checked patch to the RomM 5.4.0 RQ worker."""

import ast
import hashlib
from pathlib import Path

path = Path('/backend/handler/rq_worker.py')
source = path.read_text()
expected = 'd410c902246f16e95acef1ed470c91529c0c78d0848b08361601c22f8b0fb053'
if hashlib.sha256(source.encode()).hexdigest() != expected:
    raise SystemExit('Unsupported RomM worker source; review this patch before upgrading')

method = '''    def perform_job(self, job: Job, queue: Any) -> bool:
        try:
            return super().perform_job(job, queue)
        finally:
            # RQ terminates the work horse with os._exit, bypassing Python
            # finalizers. Return pooled DB connections with COM_QUIT first.
            # Do not import the ORM for a job that never used the database.
            database = sys.modules.get("handler.database.base_handler")
            if database is not None:
                try:
                    database.sync_engine.dispose()
                except Exception:
                    self.log.exception("Could not close the work horse database pool")

'''

source = source.replace('import logging\n', 'import logging\nimport sys\n', 1)
anchor = '    def handle_work_horse_killed(\n'
assert source.count(anchor) == 1
source = source.replace(anchor, method + anchor, 1)
ast.parse(source)
path.write_text(source)
