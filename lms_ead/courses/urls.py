from django.urls import path

from lms_ead.courses.views import (
    course_detail_view,
)

app_name = "courses"
urlpatterns = [
    path("<int:pk>/", view=course_detail_view, name="detail"),
]
