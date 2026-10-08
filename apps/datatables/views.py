from django.views.generic import TemplateView
from django_tables2 import SingleTableView
from .models import SampleData
from .tables import SampleDataTable
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(TemplateView):
    template_name = "datatables/index.html"
    login_url = '/admin/login/'  # Or your custom login URL

class SampleDataTableView(SingleTableView):
    model = SampleData
    table_class = SampleDataTable
    template_name = "datatables/table_ajax.html"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().order_by('name')