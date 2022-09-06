# Generated by Django 2.2 on 2020-10-15 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
        ('xpro', '0002_remove_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='xpro_school_organization', to='organizations.Organization'),
        ),
        migrations.AddField(
            model_name='sponsor',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='xpro_sponsor_organization', to='organizations.Organization'),
        ),
        migrations.AddField(
            model_name='student',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='xpro_student_organization', to='organizations.Organization'),
        ),
        migrations.AddField(
            model_name='user',
            name='organization',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='organizations.Organization'),
        ),
    ]
