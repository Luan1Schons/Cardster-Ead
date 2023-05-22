from django.db import models
from django.db.models import CharField, ImageField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from datetime import date, datetime

User = get_user_model()

# Obtenha a data atual
today = date.today()
# Crie o diretório no formato "ano/mês/dia"
time_dir = today.strftime("%Y/%m/%d")

class Course(models.Model):

    # First and last name do not cover name patterns around the globe
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = CharField(_("Nome do curso"), blank=True, max_length=255)
    description =  CharField(_("Descrição do curso"), blank=True, max_length=555)
    image = ImageField(upload_to ='uploads/courses/' + time_dir, default="default.png")
    status = CharField(default='N', max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS = [name, description]

    class Meta:
        verbose_name = _("Curso")
        verbose_name_plural = _("Cursos")
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self) -> str:
        """Get URL for course's detail view.

        Returns:
            str: URL for course detail.

        """
        return reverse("courses:detail", kwargs={"pk": self.id})
    
class CourseModules(models.Model):
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = CharField(_("Nome do módulo"), blank=True, max_length=255)
    description = CharField(_("Descrição do módulo"), blank=True, max_length=555)
    image = ImageField(upload_to ='uploads/courses/' + time_dir, default="default.png")
    status = CharField(default='N', max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS = [name, description, image, status]
    
    class Meta:
        verbose_name = _("Módulos do curso")
        verbose_name_plural = _("Módulos dos cursos")
        
    def __str__(self):
        created_at_formatted = self.created_at.strftime("%d/%m/%Y")
        return f"{self.name} - {created_at_formatted}"



class CourseLessons(models.Model):
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    module = models.ForeignKey(CourseModules, on_delete=models.CASCADE)
    name = CharField(_("Nome da aula"), blank=True, max_length=255)
    description = CharField(_("Descrição da aula"), blank=True, max_length=555)
    image = ImageField(upload_to ='uploads/courses/' + time_dir, default="default.png")
    status = CharField(default='N', max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS = [name, module, description, image, status]
    
    class Meta:
        verbose_name = _("Aulas do curso")
        verbose_name_plural = _("Aulas dos cursos")
    
class CourseMaterials(models.Model):
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    module = models.ForeignKey(CourseModules, on_delete=models.CASCADE)
    lesson = models.ForeignKey(CourseLessons, on_delete=models.CASCADE)
    name = CharField(_("Nome do material"), blank=True, max_length=255)
    description = CharField(_("Descrição do material"), blank=True, max_length=555)
    image = ImageField(upload_to ='uploads/courses/' + time_dir, default="default.png")
    status = CharField(default='N', max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS = [name, module, lesson, description, image, status]
    
    class Meta:
        verbose_name = _("Matérias do curso")
        verbose_name_plural = _("Matérias dos cursos")
    
class CourseQuestions(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    module = models.ForeignKey(CourseModules, on_delete=models.CASCADE)
    lesson = models.ForeignKey(CourseLessons, on_delete=models.CASCADE)
    material = models.ForeignKey(CourseMaterials, on_delete=models.CASCADE)
    name = CharField(_("Nome da questão"), blank=True, max_length=255)
    description = CharField(_("Descrição da questão"), blank=True, max_length=555)
    image = ImageField(upload_to ='uploads/courses/' + time_dir, default="default.png")
    status = CharField(default='N', max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS = [name, module, lesson, material, description, image, status]
    

class CourseAnswers(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    module = models.ForeignKey(CourseModules, on_delete=models.CASCADE)
    lesson = models.ForeignKey(CourseLessons, on_delete=models.CASCADE)
    material = models.ForeignKey(CourseMaterials, on_delete=models.CASCADE)
    question = models.ForeignKey(CourseQuestions, on_delete=models.CASCADE)
    name = CharField(_("Nome da resposta"), blank=True, max_length=255)
    description = CharField(_("Descrição da resposta"), blank=True, max_length=555)
    image = ImageField(upload_to ='uploads/courses/' + time_dir, default="default.png")
    status = CharField(default='N', max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS = [name, module, lesson, material, question, description, image, status]

class CourseProgress(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    module = models.ForeignKey(CourseModules, on_delete=models.CASCADE)
    lesson = models.ForeignKey(CourseLessons, on_delete=models.CASCADE)
    material = models.ForeignKey(CourseMaterials, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = CharField(default='N', max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS = [course, module, lesson, material, user, status]
    
    
class CoursePrice(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = CharField(default='N', max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS = [course, price, status]
    
class CoursePayment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = CharField(default='N', max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS = [course, user, status]

class CourseComment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = CharField(_("Comentário do curso"), blank=True, max_length=555)
    status = CharField(default='N', max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS = [course, user, comment, status]

