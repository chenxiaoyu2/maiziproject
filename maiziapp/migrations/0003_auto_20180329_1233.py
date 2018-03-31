# Generated by Django 2.0.3 on 2018-03-29 04:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maiziapp', '0002_auto_20180329_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discuss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=256, verbose_name='评论内容')),
                ('date_publish', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('lesson', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='maiziapp.lesson', verbose_name='课时')),
                ('parent_id', models.ForeignKey(blank=True, db_column='parent_id', default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='maiziapp.Discuss', verbose_name='上一级回复')),
            ],
            options={
                'verbose_name': '评论表',
                'verbose_name_plural': '评论表',
                'ordering': ['-date_publish'],
            },
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-id'], 'verbose_name': '学生', 'verbose_name_plural': '学生'},
        ),
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': '老师', 'verbose_name_plural': '老师'},
        ),
        migrations.AddField(
            model_name='discuss',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]