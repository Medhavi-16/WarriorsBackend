# Generated by Django 3.1.1 on 2020-09-29 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BreastCancerApp', '0002_quotes_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotes',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
    ]