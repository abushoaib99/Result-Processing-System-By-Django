# Generated by Django 2.0.5 on 2018-08-07 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('student_id', models.IntegerField(max_length=10)),
                ('dept', models.CharField(max_length=100)),
                ('session', models.IntegerField(max_length=50)),
                ('semester', models.CharField(max_length=500)),
            ],
        ),
    ]
