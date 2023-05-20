from django.db import models
from django.db.models import CharField, ImageField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Course(models.Model):

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of Course"), blank=True, max_length=255)
    description =  CharField(_("Description of Course"), blank=True, max_length=555)
    image = ImageField(upload_to ='uploads/courses/% Y/% m/% d/', default="default.png")
    status = CharField(default='N', max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS = [name, description]

    def get_absolute_url(self) -> str:
        """Get URL for course's detail view.

        Returns:
            str: URL for course detail.

        """
        return reverse("courses:detail", kwargs={"pk": self.id})
