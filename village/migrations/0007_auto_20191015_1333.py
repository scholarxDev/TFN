# Generated by Django 2.2.6 on 2019-10-15 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('village', '0006_auto_20190911_1512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fundrequest',
            old_name='title',
            new_name='request_title',
        ),
    ]
