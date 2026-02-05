from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from users import views

def profile_redirect(request):
    return redirect("dashboard")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/profile/", profile_redirect),   
    path("accounts/login/", views.custom_login, name="login"),
    path("accounts/logout/", views.custom_logout, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("sign_up/", views.sign_up, name="sign_up"),
]
