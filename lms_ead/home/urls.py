from django.urls import path

from lms_ead.home.views import (
    home_view,
)

app_name = "home"
urlpatterns = [
    path("", view=home_view, name="home"),
]
