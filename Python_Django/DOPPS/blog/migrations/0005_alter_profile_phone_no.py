# Generated by Django 3.2.18 on 2023-03-04 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_profile_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_no',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]