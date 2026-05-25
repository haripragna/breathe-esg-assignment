from django.contrib import admin
from .models import Tenant, DataSource, RawRecord, NormalizedRecord, AuditLog

admin.site.register(Tenant)
admin.site.register(DataSource)
admin.site.register(RawRecord)
admin.site.register(NormalizedRecord)
admin.site.register(AuditLog)