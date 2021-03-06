# Generated by Django 3.2.11 on 2022-06-10 23:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(blank=True, max_length=250, null=True)),
                ('patient_id', models.CharField(blank=True, max_length=250, null=True)),
                ('disease', models.CharField(blank=True, max_length=250, null=True)),
                ('algorithm', models.CharField(blank=True, max_length=250, null=True)),
                ('symptom_1', models.CharField(blank=True, max_length=250, null=True, verbose_name='Symptom 1')),
                ('symptom_2', models.CharField(blank=True, max_length=250, null=True, verbose_name='Symptom 2')),
                ('symptom_3', models.CharField(blank=True, max_length=250, null=True, verbose_name='Symptom 3')),
                ('symptom_4', models.CharField(blank=True, max_length=250, null=True, verbose_name='Symptom 4')),
                ('symptom_5', models.CharField(blank=True, max_length=250, null=True, verbose_name='Symptom 5')),
                ('symptoms', models.JSONField(blank=True, default=dict, null=True, verbose_name='Collection of the symptoms')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
    ]
