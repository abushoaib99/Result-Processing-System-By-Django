# Generated by Django 2.0.5 on 2018-08-07 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20180807_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='session',
            field=models.IntegerField(default=0, help_text='-'),
        ),
    ]
