# Generated by Django 2.0.5 on 2018-08-28 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20180815_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='session',
            field=models.DurationField(default=0),
        ),
    ]
