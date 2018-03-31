from django.shortcuts import render,redirect
from maiziapp.models import *
from django.http import HttpResponse
import json
from django.contrib.auth import logout, login, authenticate
from maiziapp.forms import *
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.

def global_setting(request):
    # 友情链接数据
    link_list=links.objects.all()
    #推荐搜索标签
    keyword_list=RecommendKeywords.objects.all()
    #推荐阅读文章
    read_article_list=read_article.objects.all()
    read_basketball = read_article.objects.filter(reading_type=read_article.ACTIVITY)
    read_soccer = read_article.objects.filter(reading_type=read_article.NEWS)
    read_maizi = read_article.objects.filter(reading_type=read_article.DISCUSS)
    #首页老师信息
    read_teacher=userinfo.objects.filter(user_type=userinfo.TEACHER)
    #职业课程(最新课程排行)
    course_list=CareerCourse.objects.all()
    #职业课程（最多播放排行）
    play_count_list = CareerCourse.objects.all().order_by('-play_count')
    #职业课程（人气最高排行）
    study_count_list = CareerCourse.objects.all().order_by('-study_count')

    user_list=User.objects.all()
    return locals()

def index(request):
    return render(request, 'index.html', locals())

# 注销
def do_logout(request):
    try:
        logout(request)
    except Exception as e:
        pass
    return redirect(request.META['HTTP_REFERER'])

# 注册
def do_reg(request):
    try:
        if request.method == 'POST':
            reg_form = RegForm(request.POST)
            if reg_form.is_valid():
                # 注册
                user = User.objects.create(username=reg_form.cleaned_data["username"],
                                    email=reg_form.cleaned_data["email"],
                                    url=reg_form.cleaned_data["url"],
                                    password=make_password(reg_form.cleaned_data["password"]),)
                user.save()

                # 登录
                user.backend = 'django.contrib.auth.backends.ModelBackend' # 指定默认的登录验证方式
                login(request, user)
                return redirect(request.POST.get('source_url'))
            else:
                return render(request, 'failure.html', {'reason': reg_form.errors})
        else:
            reg_form = RegForm()
    except Exception as e:
        pass
    return render(request, 'reg.html', locals())

# 登录
def do_login(request):
    try:
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                # 登录
                username = login_form.cleaned_data["username"]
                password = login_form.cleaned_data["password"]
                user = authenticate(username=username, password=password)
                if user is not None:
                    user.backend = 'django.contrib.auth.backends.ModelBackend' # 指定默认的登录验证方式
                    login(request, user)
                else:
                    return render(request, 'failure.html', {'reason': '登录验证失败'})
                return redirect(request.POST.get('source_url'))
            else:
                return render(request, 'failure.html', {'reason': login_form.errors})
        else:
            login_form = LoginForm()
    except Exception as e:
        pass
    return render(request, 'login.html', locals())
#进入职业课程页面
def course(request):
    return render(request, 'course.html', locals())


#进入课程播放页面
def course_play(request,courseid,lessonid=None):
    course = CareerCourse.objects.get(id=courseid)
    lesson_list = lesson.objects.filter(course=course.id)
    if lessonid is not None:
        curr_lesson_id = lessonid
        curr_lesson = lesson.objects.get(id=lessonid)
        discusses = Discuss.objects.filter(lesson_id=lessonid).order_by('id')
    else:  # 如果没有上送视频id，默认查询第一个视频相关信息
        curr_lesson_id = lesson_list[0].id
        curr_lesson = lesson_list[0]
        discusses = Discuss.objects.filter(lesson_id=lesson_list[0]).order_by('id')

    discuss_list = check_sub_discuss(discusses)
    return render(request, 'course_play.html', locals())


# 区分主评论以及子评论
def check_sub_discuss(comments):
    comment_list = []
    for comment in comments:
        if comment.parent_id is None:
            comment_list.append(comment)
        for item in comment_list:
            if not hasattr(item, 'children_discuss'):
                setattr(item, 'children_discuss', [])
            if comment.parent_id == item:
                item.children_discuss.append(comment)
                break
    for citem in comment_list:
        if len(citem.children_discuss) == 0:
            citem.discuss_num = ''
        else:
            citem.discuss_num = len(citem.children_discuss)

    return comment_list

# 提交评论
@login_required
@csrf_exempt
def discuss_post(request):
        if request.method == "POST":
            user = User.objects.get(id=request.POST.get('user_id'))
            print(user)
            content=request.POST.get('content')
            lesson1=request.POST.get('lesson_id')
            print(content)
            print(lesson1)
            if request.POST.get('parent_id') is not None:
                discuss_p = Discuss.objects.get(id=request.POST.get('parent_id'))
            else:
                discuss_p = None
            discuss = Discuss(content=request.POST.get('content'),
                              parent_id=discuss_p,
                              lesson_id=request.POST.get('lesson_id'),
                              user_id=request.POST.get('user_id'))
            discuss.save()
            return redirect(request.META['HTTP_REFERER'])
        else:
            return HttpResponse(json.dumps({'status': 'fail', 'error_msg': '评论失败'}), content_type='application/json')

#老师界面
def teacher(request,teacherid):
    teacher_list = userinfo.objects.get(id=teacherid)
    course_list1=CareerCourse.objects.filter(user_id=teacherid)
    return render(request,'teacher.html',locals())

#学生个人中心界面
def student(request,studentid):
    student_info=User.objects.get(id=studentid)
    course_count=CareerCourse.objects.filter(student=studentid).count()
    course_study_list=CareerCourse.objects.filter(student=studentid)
    return render(request,'student.html',locals())

# 修改个人信息
def do_change(request):
    try:
        if request.method == 'POST':
            change_form = ChangeForm(request.POST)
            print(111111)
            if change_form.is_valid():
                # 修改信息
                print(request.POST.get("user_id"))
                user=User.objects.get(id=request.POST.get('user_id'))
                print(user)
                user.username=change_form.cleaned_data["username"]
                user.qq=change_form.cleaned_data["qq"]
                user.mobile=change_form.cleaned_data["moblie"]
                user.email=change_form.cleaned_data["email"]
                user.password=change_form.cleaned_data["password"]
                user.save()
                print(user.username)
                return redirect(request.POST.get('source_url'))
            else:
                return render(request, 'failure.html', {'reason': change_form.errors})
        else:
            change_form = ChangeForm()
    except Exception as e:
        pass
    return render(request, 'change.html', locals())

