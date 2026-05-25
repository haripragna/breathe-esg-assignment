# MODEL

## Tenant
Represents enterprise clients.

## DataSource
Tracks source type:
- SAP
- Utility
- Travel

## RawRecord
Stores uploaded source payload.

## NormalizedRecord
Stores processed ESG records including:
- category
- scope
- emissions value
- status

## AuditLog
Tracks analyst review actions.