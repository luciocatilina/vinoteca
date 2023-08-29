# Generated by Django 4.2.4 on 2023-08-28 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upload_wine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WineImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='wine_photos')),
            ],
        ),
        migrations.RemoveField(
            model_name='wine',
            name='photo',
        ),
        migrations.AlterField(
            model_name='wine',
            name='cellar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload_wine.cellar'),
        ),
        migrations.AlterField(
            model_name='wine',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload_wine.province'),
        ),
    ]