# Generated by Django 4.2.2 on 2023-08-08 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
