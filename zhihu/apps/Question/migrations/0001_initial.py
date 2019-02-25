# Generated by Django 2.0.2 on 2018-12-17 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='内容')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发布日期')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
                ('status', models.CharField(choices=[('draft', '草稿'), ('published', '已发布')], default='draft', max_length=10, verbose_name='回答状态')),
                ('vote', models.IntegerField(default=0, verbose_name='赞同数')),
                ('anonymous', models.BooleanField(default=False, verbose_name='是否匿名')),
                ('flows', models.PositiveIntegerField(default=0, verbose_name='关注')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to=settings.AUTH_USER_MODEL, verbose_name='回答者')),
                ('collection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collection', to=settings.AUTH_USER_MODEL, verbose_name='收藏')),
            ],
            options={
                'verbose_name': '回答',
                'verbose_name_plural': '回答',
                'ordering': ('-vote',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='标题')),
                ('body', models.TextField(blank=True, null=True, verbose_name='内容')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
                ('views', models.PositiveIntegerField(default=0)),
                ('anonymous', models.BooleanField(default=False, verbose_name='是否匿名')),
                ('flows', models.PositiveIntegerField(default=0, verbose_name='关注')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to=settings.AUTH_USER_MODEL, verbose_name='提问者')),
            ],
            options={
                'verbose_name': '问题',
                'verbose_name_plural': '问题',
                'ordering': ('-updated',),
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='话题名')),
                ('desc', models.TextField(verbose_name='话题描述')),
                ('topic_type', models.IntegerField(choices=[(1, '一级话题'), (2, '二级话题'), (3, '三级话题')], verbose_name='话题级别')),
                ('flows', models.PositiveIntegerField(default=0, verbose_name='关注')),
                ('parent_topic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='Question.Topic', verbose_name='父话题')),
            ],
            options={
                'verbose_name': '话题',
                'verbose_name_plural': '话题',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='Question.Topic', verbose_name='话题'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='Question.Question', verbose_name='问题'),
        ),
    ]
