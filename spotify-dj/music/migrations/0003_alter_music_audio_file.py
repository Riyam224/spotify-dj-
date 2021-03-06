# Generated by Django 3.2.7 on 2021-09-07 16:37

from django.db import migrations, models
import music.validators


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_rename_musoc_music'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to='musics', validators=[music.validators.validate_is_audio]),
        ),
    ]
