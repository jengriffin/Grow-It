# Generated by Django 4.1.1 on 2022-09-09 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grow', '0002_rename_plants_plant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='plants',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plants', to='grow.plant'),
        ),
    ]