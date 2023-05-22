import django_tables2 as tables
from django_tables2 import RequestConfig
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, redirect
from allauth.account.forms import LoginForm
from allauth.account.views import LoginView
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import ListView
from .tables import FilteredUsersTable, UserFilterSet


User = get_user_model()

class AdminLoginView(LoginView):
    """
    View to handle admin login.
    """
    template_name = "admin/login.html"
    form_class = LoginForm
    
    def form_valid(self, form):
        # Verificar se o usuário é um administrador
        user = form.user
        if user.is_authenticated and user.is_superuser:
            return super().form_valid(form)
        else:
            messages.error(self.request, "Acesso restrito aos administradores.")
            return redirect("admin:login")


class AdminHome(ListView):
    template_name = "admin/home.html"
    model = User
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_form = UserFilterSet(self.request.GET, queryset=queryset)
        return filter_form.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filter_form = UserFilterSet(self.request.GET)
        table = FilteredUsersTable(filter_form.qs)
        RequestConfig(self.request).configure(table)
        
        context['filter_form'] = filter_form
        context['table'] = table
        return context

admin_login_view = AdminLoginView.as_view()
admin_home_view = AdminHome.as_view()
