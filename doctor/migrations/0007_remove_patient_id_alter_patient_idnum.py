# Generated by Django 4.1.3 on 2023-02-22 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_vaccinelocations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='id',
        ),
        migrations.AlterField(
            model_name='patient',
            name='idNum',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
