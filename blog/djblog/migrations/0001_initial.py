# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 06:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='标题')),
                ('text', models.TextField(verbose_name='正文')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('status', models.CharField(choices=[('d', 'draft'), ('P', 'published')], max_length=1, verbose_name='文章状态')),
                ('abstract', models.CharField(blank=True, help_text='可选，如无则摘取正文前50字符', max_length=50, null=True, verbose_name='摘要')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='浏览量')),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='点赞数')),
                ('topped', models.BooleanField(default=False, verbose_name='置顶')),
            ],
        ),
        migrations.CreateModel(
            name='Bloger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField(blank=True, null=True, verbose_name='年龄')),
                ('sex', models.CharField(choices=[('F', 'FEMALE'), ('M', 'MALE')], default='F', max_length=10, verbose_name='性别')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='类名')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(verbose_name='评论')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('articleid', models.IntegerField(default=0, verbose_name='文章ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djblog.Article', verbose_name='所属文章')),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloger', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='djblog.Bloger', verbose_name='关系')),
            ],
        ),
        migrations.AddField(
            model_name='bloger',
            name='blacklist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blacklist', to='djblog.Relationship', verbose_name='拉黑列表'),
        ),
        migrations.AddField(
            model_name='bloger',
            name='likelist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likelist', to='djblog.Relationship', verbose_name='关注列表'),
        ),
        migrations.AddField(
            model_name='bloger',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djblog.Bloger', verbose_name='作者'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='djblog.Category', verbose_name='分类'),
        ),
    ]
