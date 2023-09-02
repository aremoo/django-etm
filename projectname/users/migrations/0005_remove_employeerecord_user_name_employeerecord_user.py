# Generated by Django 4.2.3 on 2023-08-13 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_employeerecord'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeerecord',
            name='user_name',
        ),
        migrations.AddField(
            model_name='employeerecord',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
