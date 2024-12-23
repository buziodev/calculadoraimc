# Generated by Django 3.0.14 on 2024-11-25 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calcimc', '0002_auto_20241122_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historico',
            name='altura',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='historico',
            name='data',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='historico',
            name='imc',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historico',
            name='nome',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='historico',
            name='peso',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='historico',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='altura',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='peso',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=1),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
