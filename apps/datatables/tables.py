import django_tables2 as tables
from .models import SampleData

class SampleDataTable(tables.Table):
    class Meta:
        model = SampleData
        template_name = "django_tables2/bootstrap5-responsive.html"
        fields = ("name", "position", "office", "age", "start_date", "salary")
        attrs = {
            "class": "table table-bordered table-hover",
            "thead": {
                "class": "table-light"
            }
        }