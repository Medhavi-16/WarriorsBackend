# Generated by Django 3.1.1 on 2020-10-11 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BreastCancerApp', '0005_auto_20201011_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='content',
            field=models.CharField(max_length=3000),
        ),
    ]