# Generated by Django 4.2.2 on 2023-07-31 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='slug',
            field=models.SlugField(default=None, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='phone',
            name='release_date',
            field=models.DateField(),
        ),
    ]
