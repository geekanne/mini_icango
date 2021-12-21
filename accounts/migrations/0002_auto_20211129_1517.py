# Generated by Django 3.2.6 on 2021-11-29 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
            ],
        ),
        migrations.RenameField(
            model_name='account',
            old_name='delete_at',
            new_name='date_deleted',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='update_at',
            new_name='date_updated',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='is_deleted',
            new_name='is_admin',
        ),
        migrations.RenameField(
            model_name='feedbackimage',
            old_name='img_path',
            new_name='image_path',
        ),
        migrations.RemoveField(
            model_name='account',
            name='create_at',
        ),
        migrations.RemoveField(
            model_name='account',
            name='email',
        ),
        migrations.RemoveField(
            model_name='account',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='account',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='account',
            name='kakoid',
        ),
        migrations.RemoveField(
            model_name='account',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='account',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='account',
            name='user_permissions',
        ),
        migrations.AddField(
            model_name='account',
            name='kakakoid',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='account',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
