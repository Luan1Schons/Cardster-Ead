# Generated by Django 4.1.9 on 2023-05-20 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("courses", "0003_course_image_course_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="CourseLessons",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(blank=True, max_length=255, verbose_name="Nome da aula")),
                ("description", models.CharField(blank=True, max_length=555, verbose_name="Descrição da aula")),
                ("image", models.ImageField(default="default.png", upload_to="uploads/courses/% Y/% m/% d/")),
                ("status", models.CharField(default="N", max_length=1)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="CourseMaterials",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(blank=True, max_length=255, verbose_name="Nome do material")),
                ("description", models.CharField(blank=True, max_length=555, verbose_name="Descrição do material")),
                ("image", models.ImageField(default="default.png", upload_to="uploads/courses/% Y/% m/% d/")),
                ("status", models.CharField(default="N", max_length=1)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="CourseModules",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(blank=True, max_length=255, verbose_name="Name of Module")),
                ("description", models.CharField(blank=True, max_length=555, verbose_name="Description of Module")),
                ("image", models.ImageField(default="default.png", upload_to="uploads/courses/% Y/% m/% d/")),
                ("status", models.CharField(default="N", max_length=1)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name="course",
            name="user",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="CourseQuestions",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(blank=True, max_length=255, verbose_name="Nome da questão")),
                ("description", models.CharField(blank=True, max_length=555, verbose_name="Descrição da questão")),
                ("image", models.ImageField(default="default.png", upload_to="uploads/courses/% Y/% m/% d/")),
                ("status", models.CharField(default="N", max_length=1)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("course", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="courses.course")),
                ("lesson", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="courses.courselessons")),
                (
                    "material",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="courses.coursematerials"),
                ),
                ("module", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="courses.coursemodules")),
            ],
        ),
        migrations.CreateModel(
            name="CourseProgress",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("status", models.CharField(default="N", max_length=1)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("course", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="courses.course")),
                ("lesson", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="courses.courselessons")),
                (
                    "material",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="courses.coursematerials"),
                ),
                ("module", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="courses.coursemodules")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="CoursePrice",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("status", models.CharField(default="N", max_length=1)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("course", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="courses.course")),
            ],
        ),
        migrations.CreateModel(
            name="CoursePayment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("status", models.CharField(default="N", max_length=1)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("course", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="courses.course")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name="coursemodules",
            name="course",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="courses.course"),
        ),
        migrations.AddField(
            model_name="coursematerials",
            name="course",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="courses.course"),
        ),
        migrations.AddField(
            model_name="coursematerials",
            name="lesson",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="courses.courselessons"),
        ),
        migrations.AddField(
            model_name="coursematerials",
            name="module",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="courses.coursemodules"),
        ),
        migrations.AddField(
            model_name="courselessons",
            name="course",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="courses.course"),
        ),
        migrations.AddField(
            model_name="courselessons",
            name="module",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="courses.coursemodules"),
        ),
        migrations.CreateModel(
            name="CourseComment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("comment", models.CharField(blank=True, max_length=555, verbose_name="Comentário do curso")),
                ("status", models.CharField(default="N", max_length=1)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("course", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="courses.course")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="CourseAnswers",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(blank=True, max_length=255, verbose_name="Nome da resposta")),
                ("description", models.CharField(blank=True, max_length=555, verbose_name="Descrição da resposta")),
                ("image", models.ImageField(default="default.png", upload_to="uploads/courses/% Y/% m/% d/")),
                ("status", models.CharField(default="N", max_length=1)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("course", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="courses.course")),
                ("lesson", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="courses.courselessons")),
                (
                    "material",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="courses.coursematerials"),
                ),
                ("module", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="courses.coursemodules")),
                (
                    "question",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="courses.coursequestions"),
                ),
            ],
        ),
    ]
