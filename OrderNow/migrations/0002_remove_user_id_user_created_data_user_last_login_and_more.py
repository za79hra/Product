# Generated by Django 4.1.7 on 2023-07-10 22:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("OrderNow", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="id",
        ),
        migrations.AddField(
            model_name="user",
            name="created_data",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="last_login",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(
                max_length=255, primary_key=True, serialize=False, unique=True
            ),
        ),
    ]
