# Generated by Django 4.2.4 on 2023-09-01 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_employees_options_alter_participants_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='emp_img',
            field=models.ImageField(upload_to='images/', verbose_name='Фото сотрудника'),
        ),
    ]
