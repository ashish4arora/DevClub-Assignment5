# Generated by Django 4.0.6 on 2022-07-30 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grades', '0003_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
