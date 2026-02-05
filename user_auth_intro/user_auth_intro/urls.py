from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from users import views

def profile_redirect(request):
    return redirect("dashboard")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/profile/", profile_redirect),   # 👈 ADD THIS
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("sign_up/", views.sign_up, name="sign_up"),
]
