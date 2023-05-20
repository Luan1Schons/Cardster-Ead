from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from .models import Course

class CourseDetailView(DetailView):
    model = Course
    slug_field = "id"
    slug_url_kwarg = "id"
    
course_detail_view = CourseDetailView.as_view()

