# Generated by Django 3.1.5 on 2021-01-23 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20210123_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio'),
        ),
        migrations.AddField(
            model_name='startup',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio'),
        ),
        migrations.AddField(
            model_name='web',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio'),
        ),
        migrations.AddField(
            model_name='web',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio'),
        ),
    ]