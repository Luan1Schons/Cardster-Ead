import django_tables2 as tables
from django_tables2.utils import A
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django_tables2 import SingleTableView
from django_filters import FilterSet, CharFilter

User = get_user_model()

class UserFilterSet(FilterSet):
    email = CharFilter(field_name='email', lookup_expr='icontains', label=_('Endereço de Email'))

    class Meta:
        model = User
        fields = ['email']


class FilteredUsersTable(tables.Table):
    email = tables.Column(verbose_name=_("Endereço de Email"), attrs={"td": {"class": "email-column"}})
    date_joined = tables.Column(verbose_name=_("Criado"), attrs={"td": {"class": "email-column"}})

    class Meta:
        model = User
        template_name = "django_tables2/bootstrap5-responsive.html"
        attrs = {"class": "table table-striped table-bordered"}
        empty_text = "Nenhum usuário encontrado"
        fields = ["email", "date_joined"]
        per_page = 10
        sequence = ("email", "date_joined")

    def render_name(self, value, record):
        return record.get_full_name()