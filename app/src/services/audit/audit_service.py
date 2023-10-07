from ...models import Audit
from ...providers.database import DatabaseProvider


class AuditService:
    def log(self, action: str, content: str):
        db = DatabaseProvider()
        audit_entry = Audit(action=action, content=content)
        db.insert_audit(audit_entry)
