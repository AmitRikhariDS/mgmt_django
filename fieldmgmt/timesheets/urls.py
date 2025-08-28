from django.urls import path
from . import views

app_name = "timesheets"

urlpatterns = [
    path("", views.timesheet_list, name="timesheet_list"),
    path("new/", views.timesheet_create, name="timesheet_create"),
]
