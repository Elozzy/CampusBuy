# Generated by Django 2.0.1 on 2008-01-01 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campusbuy', '0005_auto_20080101_0406'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemadvert',
            name='Location',
            field=models.CharField(default='University of Benin', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itemadvert',
            name='Phone_Number',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
