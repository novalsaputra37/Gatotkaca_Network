# Generated by Django 3.2.7 on 2021-12-24 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20211224_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmodel',
            name='cover',
            field=models.ImageField(default=1, upload_to='content/cover'),
            preserve_default=False,
        ),
    ]
