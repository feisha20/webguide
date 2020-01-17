# Generated by Django 2.1.4 on 2020-01-16 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('is_main', models.BooleanField(verbose_name='is_main')),
                ('sort', models.CharField(max_length=200, verbose_name='sort')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': 'Titles管理',
                'verbose_name_plural': 'Titles管理',
            },
        ),
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='title_name')),
                ('url', models.CharField(max_length=200, verbose_name='name')),
                ('logo', models.ImageField(upload_to='logo')),
                ('sort', models.CharField(max_length=200, verbose_name='logo_url')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.Titles')),
            ],
            options={
                'verbose_name': 'Urls管理',
                'verbose_name_plural': 'Urls管理',
            },
        ),
    ]