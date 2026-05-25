# MODEL

## Backend

The backend is built using Django REST Framework.

It handles:

- Data ingestion API
- Record storage
- Data normalization
- Analyst review workflow
- Admin management

Main models:

### Tenant
Represents enterprise clients.

### DataSource
Tracks uploaded source type:
- SAP
- Utility
- Travel

### RawRecord
Stores uploaded source payload.

### NormalizedRecord
Stores processed ESG data.

Fields:
- category
- scope
- value
- unit
- status

### AuditLog
Tracks review actions.

---

## Frontend

The frontend is built using React.

It provides:

- Source selection interface
- Upload trigger
- Analyst dashboard
- Normalized record display