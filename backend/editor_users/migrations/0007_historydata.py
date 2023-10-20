# Generated by Django 4.2.4 on 2023-10-07 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('editor_users', '0006_alter_editorusers_version'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField()),
                ('key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor_users.editorusers')),
            ],
        ),
    ]