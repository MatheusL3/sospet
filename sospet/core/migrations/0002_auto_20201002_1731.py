# Generated by Django 3.1.1 on 2020-10-02 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='photo',
            field=models.ImageField(upload_to='pet'),
        ),
    ]
