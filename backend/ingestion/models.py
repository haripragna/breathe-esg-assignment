from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=255)


class DataSource(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    source_type = models.CharField(max_length=20)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class RawRecord(models.Model):
    source = models.ForeignKey(DataSource, on_delete=models.CASCADE)
    payload = models.JSONField()


class NormalizedRecord(models.Model):
    source = models.ForeignKey(DataSource, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    scope = models.CharField(max_length=20)
    value = models.FloatField()
    unit = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default='PENDING')
    flagged = models.BooleanField(default=False)


class AuditLog(models.Model):
    record = models.ForeignKey(NormalizedRecord, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)