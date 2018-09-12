# Generated by Django 2.0 on 2018-09-12 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20180907_0127'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='marks',
            options={'ordering': ['all_semester']},
        ),
        migrations.AlterField(
            model_name='informations',
            name='student_roll',
            field=models.PositiveIntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='marks',
            name='assignment_marks',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='marks',
            name='class_test_marks',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='marks',
            name='midterm_marks',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='marks',
            name='subject_marks',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='semester',
            name='student_semester',
            field=models.CharField(choices=[('1st Semester', '1st Semester'), ('2nd Semester', '2nd Semester'), ('3rd Semester', '3rd Semester'), ('4th Semester', '4th Semester'), ('5th Semester', '5th Semester'), ('6th Semester', '6th Semester'), ('7th Semester', '7th Semester'), ('8th Semester', '8th Semester')], max_length=15, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='marks',
            unique_together={('student_info', 'subject_name')},
        ),
    ]