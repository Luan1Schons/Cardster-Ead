from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CoursesConfig(AppConfig):
    name = "lms_ead.courses"
    verbose_name = _("Courses")

    def ready(self):
        try:
            import lms_ead.courses.signals  # noqa: F401
        except ImportError:
            pass
