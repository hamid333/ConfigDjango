# Generated by Django 4.2.7 on 2023-11-21 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, verbose_name='نوع مشاوره'),
        ),
    ]