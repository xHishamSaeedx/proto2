# Generated by Django 4.1.4 on 2023-01-04 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exampleproject', '0008_remove_timetable_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]