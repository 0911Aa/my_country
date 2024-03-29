# Generated by Django 2.2.2 on 2019-07-16 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_superman'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
            ],
            options={
                'verbose_name_plural': '分类',
                'db_table': 'Classification',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name_plural': '难度等级',
                'db_table': 'Level',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, '下线'), (2, '上线')], default=1, verbose_name='状态')),
                ('weight', models.IntegerField(default=0, verbose_name='权重（从大到小排序）')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('img', models.CharField(max_length=32, verbose_name='图片')),
                ('href', models.CharField(max_length=256, verbose_name='视频地址')),
                ('create_data', models.DateTimeField(auto_now_add=True)),
                ('classification', models.ForeignKey(on_delete=None, to='company.Classification')),
                ('level', models.ForeignKey(on_delete=None, to='company.Level')),
            ],
            options={
                'verbose_name_plural': '视频',
                'db_table': 'Vedio',
            },
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='名称')),
                ('classification', models.ManyToManyField(to='company.Classification')),
            ],
            options={
                'verbose_name_plural': '方向(视频方向)',
                'db_table': 'Direction',
            },
        ),
    ]
