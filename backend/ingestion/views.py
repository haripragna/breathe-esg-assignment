from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tenant, DataSource, NormalizedRecord


@api_view(['POST'])
def upload_file(request):
    source_type = request.data.get('source_type')

    tenant, _ = Tenant.objects.get_or_create(name="Breathe ESG Demo")

    source = DataSource.objects.create(
        tenant=tenant,
        source_type=source_type
    )

    record = NormalizedRecord.objects.create(
        source=source,
        category="Sample Category",
        scope="Scope 1",
        value=100,
        unit="kgCO2e",
        status="PENDING",
        flagged=False
    )

    return Response({
        "message": "File uploaded successfully",
        "record_id": record.id
    })


@api_view(['GET'])
def get_records(request):
    records = NormalizedRecord.objects.all()

    data = []
    for record in records:
        data.append({
            "id": record.id,
            "category": record.category,
            "scope": record.scope,
            "value": record.value,
            "unit": record.unit,
            "status": record.status
        })

    return Response(data)

# Create your views here.
