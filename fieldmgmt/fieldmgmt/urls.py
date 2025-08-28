from django.contrib import admin
from django.urls import path, include
from accounts.views import landing, register_view

urlpatterns = [
    path("", landing, name="landing"),
    path("accounts/register/<str:role>/", register_view, name="register_with_role"),
    path("accounts/", include("django.contrib.auth.urls")),  # login/logout
    path("accounts/", include("accounts.urls")),
    path("jobs/", include("jobs.urls")),
    path("timesheets/", include("timesheets.urls")),
    path("admin/", admin.site.urls),
    path("invoices/", include("invoices.urls", namespace="invoices")),

]
