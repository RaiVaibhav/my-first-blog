# Generated by Django 2.1 on 2018-08-24 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180822_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(default='Anonymous', max_length=200),
        ),
    ]