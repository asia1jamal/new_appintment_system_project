# Generated by Django 4.1.3 on 2023-02-22 05:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=10)),
                ('middleName', models.CharField(max_length=25)),
                ('lastName', models.CharField(max_length=25)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('password', models.CharField(max_length=10)),
                ('phoneNum', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=1)),
                ('idNum', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
