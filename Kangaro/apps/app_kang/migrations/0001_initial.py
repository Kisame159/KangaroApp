# Generated by Django 4.1.7 on 2023-04-02 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProfesional',
            fields=[
                ('id_categoria_profesional', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombreCatPro', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id_estatus', models.BigAutoField(primary_key=True, serialize=False)),
                ('grado', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoEmpresa',
            fields=[
                ('id_tipo_empresa', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombreTipEmp', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombresUs', models.CharField(max_length=100)),
                ('correoUs', models.EmailField(max_length=254)),
                ('dniUs', models.CharField(max_length=8)),
                ('sexoUs', models.CharField(max_length=1)),
                ('userUs', models.CharField(max_length=100)),
                ('passwordUs', models.CharField(max_length=50)),
                ('id_categoria_profesional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_kang.categoriaprofesional')),
                ('id_estatusUs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_kang.status')),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id_empresa', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombreEmp', models.CharField(max_length=100)),
                ('correoEmp', models.EmailField(max_length=254)),
                ('rucEmp', models.CharField(max_length=11)),
                ('userEmp', models.CharField(max_length=100)),
                ('passwordEmp', models.CharField(max_length=50)),
                ('url_sitioEmp', models.URLField()),
                ('id_estatusEmp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_kang.status')),
                ('id_tipo_empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_kang.tipoempresa')),
            ],
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id_administrador', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombresAdm', models.CharField(max_length=100)),
                ('correoAdm', models.EmailField(max_length=254)),
                ('dniAdm', models.CharField(max_length=8)),
                ('sexoAdm', models.CharField(max_length=1)),
                ('userAdm', models.CharField(max_length=100)),
                ('passwordAdm', models.CharField(max_length=50)),
                ('id_estatusAdm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_kang.status')),
            ],
        ),
    ]
