# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
import locale

class User(AbstractUser):
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='QQ号码')
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号码')
    url = models.URLField(max_length=100, blank=True, null=True, verbose_name='个人网页地址')

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.username

# 友情链接
class links(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    description = models.CharField(max_length=200, verbose_name='友情链接描述')
    callback_url = models.URLField(verbose_name='url地址')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    index = models.IntegerField(default=999, verbose_name='排列顺序(从小到大)')

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __unicode__(self):
        return self.title
#搜索标签
class RecommendKeywords(models.Model):
    name = models.CharField(u'推荐搜索标签', max_length=50)
    class Meta:
        verbose_name = u'推荐搜索标签'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

#用户信息（学生和老师）
class userinfo(models.Model):
    TEACHER="老师"
    STUDENT="学生"
    USER_TYPES = (
        (TEACHER, '老师'),
        (STUDENT, '学生'),
    )
    user_type=models.CharField(u'用户类型',max_length=10,
                               choices=USER_TYPES,default=TEACHER)
    username = models.CharField(u'名称', max_length=30, unique=True)
    description = models.CharField(u'个人介绍', max_length=50,default="")
    infomation=models.CharField(u'详细信息',max_length=100,default="")
    img_url=models.CharField(u'头像链接', max_length=200,default="/static/test/15.png")
    class Meta:
        verbose_name = u'老师'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.username

#职业课程
class CareerCourse(models.Model):
    name = models.CharField(u'职业课程名称', max_length=50)
    desc = models.CharField(u'课程描述',max_length=50,default="")
    study_count = models.IntegerField(default=0, verbose_name='学习人数')
    user = models.ForeignKey(userinfo, verbose_name='授课老师', default="",on_delete=models.CASCADE)
    play_count = models.IntegerField(default=0, verbose_name='播放次数')
    course_img = models.CharField(u'课程图片', max_length=200,default="/static/test/15.png")
    student=models.ManyToManyField(User,verbose_name='报名学生')
    class Meta:
        verbose_name = u'职业课程'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.name
#推荐阅读文章
class read_article(models.Model):
    ACTIVITY = 'AV'
    NEWS = 'NW'
    DISCUSS = 'DC'
    READING_TYPES = (
        (ACTIVITY, '篮球'),
        (NEWS, '足球'),
        (DISCUSS, '麦子学院'),
    )
    reading_type = models.CharField(u'文章类型', max_length=2,
                                    choices=READING_TYPES, default=ACTIVITY)
    title = models.CharField(u'文章标题', max_length=200)
    url = models.URLField(u'文章链接', max_length=200,default="")

    class Meta:
        verbose_name = u'首页推荐文章'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.title

#課程播放
class lesson(models.Model):
    name = models.CharField(max_length=128, verbose_name=u'名称')
    video_url = models.CharField(verbose_name=u'视频', default="",max_length=100)
    video_length = models.IntegerField(verbose_name=u'视频长度')
    index = models.IntegerField(verbose_name=u'次序')
    course = models.ForeignKey(CareerCourse, verbose_name=u'课程',default="",on_delete=models.CASCADE)
    teacher = models.ForeignKey(userinfo, verbose_name=u'讲课老师',default="",on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'课时表'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

#評論
class Discuss(models.Model):
    content = models.CharField(max_length=256, verbose_name=u'评论内容')
    parent_id = models.ForeignKey('self', db_column='parent_id', verbose_name=u'上一级回复', related_name='parent', blank=True, null=True,default="",on_delete=models.CASCADE)
    lesson = models.ForeignKey(lesson, verbose_name=u'课时',default="",on_delete=models.CASCADE)
    date_publish = models.DateTimeField(verbose_name=u'发表时间', auto_now_add=True)
    user = models.ForeignKey(User, related_name='user', verbose_name=u'用户',default="",on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'评论表'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish', ]

    def __unicode__(self):
        return "%s:%s" % (self.lesson.name, self.content)



