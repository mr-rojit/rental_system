# Generated by Django 5.0 on 2024-01-17 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_postimage_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='city',
            field=models.CharField(default='a', max_length=50),
            preserve_default=False,
        ),
    ]