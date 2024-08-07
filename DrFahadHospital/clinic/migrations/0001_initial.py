# Generated by Django 5.0.6 on 2024-08-07 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('working_hours', models.CharField(max_length=255)),
                ('feature_image', models.ImageField(upload_to='clinic_images/')),
                ('doctors', models.ManyToManyField(to='doctor.doctor')),
            ],
        ),
    ]