# Generated by Django 2.0.5 on 2018-08-15 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_teacher_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='session',
            field=models.DateField(default=0),
        ),
    ]