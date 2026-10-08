from django.urls import path
from .views import IndexView, SampleDataTableView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("table-ajax/", SampleDataTableView.as_view(), name="table_ajax"),
]