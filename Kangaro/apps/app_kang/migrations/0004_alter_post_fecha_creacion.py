# Generated by Django 4.1.7 on 2023-04-07 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_kang', '0003_alter_post_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
