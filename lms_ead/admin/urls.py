from django.urls import path

from lms_ead.admin.views import (
    admin_login_view,
    admin_home_view,
)

app_name = "admin"
urlpatterns = [
    path("", view=admin_login_view, name="login"),
    path("home", view=admin_home_view, name="home"),
]
