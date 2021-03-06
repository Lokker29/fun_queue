# Generated by Django 3.2 on 2021-04-07 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_auto_20210407_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Назва')),
            ],
            options={
                'verbose_name': 'Факультет',
                'verbose_name_plural': 'Факультети',
            },
        ),
        migrations.AddField(
            model_name='unigroup',
            name='faculty',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user_profile.faculty'),
            preserve_default=False,
        ),
    ]
