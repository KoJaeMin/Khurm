# Generated by Django 3.2 on 2021-05-17 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('folder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='file_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to='folder.file'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='user_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='file',
            name='owner',
            field=models.ForeignKey(db_column='f_owner', on_delete=django.db.models.deletion.CASCADE, related_name='file', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shared',
            name='file_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shared', to='folder.file'),
        ),
        migrations.AlterField(
            model_name='shared',
            name='user_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shared', to=settings.AUTH_USER_MODEL),
        ),
    ]