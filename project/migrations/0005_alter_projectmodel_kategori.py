# Generated by Django 3.2.7 on 2021-12-24 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_projectmodel_kategori'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmodel',
            name='kategori',
            field=models.CharField(choices=[('Networking', 'Networking'), ('Design', 'Design'), ('Dekstop App', 'Dekstop App'), ('Mobile App', 'Mobile App'), ('Website', 'Website'), ('Architect', 'Architect')], max_length=50),
        ),
    ]