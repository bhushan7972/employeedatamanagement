# Generated by Django 3.1.4 on 2021-02-10 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_employee_leave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_leave',
            name='leave_reason',
            field=models.CharField(max_length=100),
        ),
    ]
