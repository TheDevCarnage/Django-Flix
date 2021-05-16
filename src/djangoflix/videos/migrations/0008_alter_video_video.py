# Generated by Django 3.2.2 on 2021-05-16 17:17

from django.db import migrations, models
import videos.validators


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_videoproxy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(default=False, upload_to='videos', validators=[videos.validators.file_validator]),
        ),
    ]