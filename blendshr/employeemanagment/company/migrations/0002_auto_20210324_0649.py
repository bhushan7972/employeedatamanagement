# Generated by Django 3.1.5 on 2021-03-24 10:49

from django.db import migrations, models
import moderator.validators


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyp',
            name='profile_picture',
            field=models.ImageField(upload_to='company/profile/avatar/%Y/%m/%d', validators=[moderator.validators.validate_file_size, moderator.validators.empty_file]),
        ),
    ]
