# Generated by Django 4.2.3 on 2023-07-30 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("editor_users", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(old_name="Editor_Users", new_name="EditorUsers",),
        migrations.RenameField(
            model_name="editorusers", old_name="description", new_name="content",
        ),
    ]
