# Generated by Django 4.2.4 on 2023-10-04 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor_users', '0005_alter_editorusers_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editorusers',
            name='version',
            field=models.CharField(max_length=2),
        ),
    ]
