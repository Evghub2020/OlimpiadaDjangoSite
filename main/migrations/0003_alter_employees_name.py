# Generated by Django 4.2.4 on 2023-09-01 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_employees_emp_img_alter_participants_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='name',
            field=models.CharField(max_length=75, verbose_name='ФИО сотрудника'),
        ),
    ]
