from django.contrib import admin
from django.forms import inlineformset_factory, Textarea
from .models import Course, CourseModules
from .forms import CourseForm, CourseModulesFormSet
from django import forms


class CourseModulesInlineForm(forms.ModelForm):
    STATUS_CHOICES = [
        ("S", "S"),
        ("N", "N"),
    ]
    
    status = forms.TypedChoiceField(
        choices=STATUS_CHOICES,
        coerce=lambda x: x == 'S',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

    class Meta:
        model = CourseModules
        fields = ["name", "description", "image", "status"]


CourseModulesFormSet = inlineformset_factory(
    Course,
    CourseModules,
    form=CourseModulesInlineForm,
    extra=1,
    can_delete=False,
)


class CourseModulesInline(admin.StackedInline):
    model = CourseModules
    formset = CourseModulesFormSet
    form = CourseModulesInlineForm
    extra = 1
    can_delete = False


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    form = CourseForm
    inlines = [CourseModulesInline]
