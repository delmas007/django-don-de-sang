# Generated by Django 4.0.6 on 2022-09-29 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_membre_admins_membre_hopital_delete_demande'),
    ]

    operations = [
        migrations.AddField(
            model_name='hopital',
            name='slug',
            field=models.SlugField(blank=True, max_length=255),
        ),
    ]