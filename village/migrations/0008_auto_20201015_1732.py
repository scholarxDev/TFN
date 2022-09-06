# Generated by Django 2.2 on 2020-10-15 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
        ('village', '0007_auto_20191015_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='village_comment_organization', to='organizations.Organization'),
        ),
        migrations.AddField(
            model_name='fundrequest',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='village_fundrequest_organization', to='organizations.Organization'),
        ),
        migrations.AddField(
            model_name='village',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='village_village_organization', to='organizations.Organization'),
        ),
    ]
