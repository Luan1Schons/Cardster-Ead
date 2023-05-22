from django import forms
from django.forms import inlineformset_factory
from .models import Course, CourseModules

class CourseForm(forms.ModelForm):
    status = forms.ChoiceField(choices=(("S", "S"), ("N", "N")))
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Course
        fields = ["user", "name", "description", "image", "status"]


class CourseModulesForm(forms.ModelForm):

    class Meta:
        model = CourseModules
        fields = ["name", "description", "image", "status"]


CourseModulesFormSet = inlineformset_factory(
    Course,
    CourseModules,
    form=CourseModulesForm,
    extra=1,
    can_delete=False,
)

def course_modules_formset_clean(formset):
    for form in formset.forms:
        if form.is_valid():
            course_modules_data = form.cleaned_data.get('status')
            if course_modules_data not in ['S', 'N']:
                form.add_error('status', "Status inválido. Por favor, escolha uma opção entre: [S, N].")

CourseModulesFormSet.clean = course_modules_formset_clean
