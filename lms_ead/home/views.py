from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView
from ..courses.models import Course


## Class to load TemplateView for home page

class HomeView(TemplateView):
    """
    View to load home page.
    """
    model = Course
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context
    
home_view = HomeView.as_view()

