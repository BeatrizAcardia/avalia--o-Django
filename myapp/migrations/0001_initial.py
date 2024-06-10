# Generated by Django 5.0.6 on 2024-06-10 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idEquipamento', models.CharField(max_length=100)),
                ('local', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='inscriptions/')),
            ],
        ),
    ]
