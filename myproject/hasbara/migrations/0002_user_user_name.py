# Generated by Django 4.2.7 on 2023-11-16 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hasbara', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
