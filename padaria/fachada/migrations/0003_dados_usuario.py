# Generated by Django 5.1.2 on 2024-10-16 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fachada', '0002_produto_descricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dados_usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('funcao', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=25)),
                ('salario', models.IntegerField()),
            ],
        ),
    ]
