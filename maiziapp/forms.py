# -*- coding:utf-8 -*-
from django import forms
from django.conf import settings
from django.db.models import Q
import re
from maiziapp.models import *

class LoginForm(forms.Form):
    '''
    登录Form
    '''
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "用户名", "required": "required",}),
                              max_length=50,error_messages={"required": "用户名不能为空",})
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "密码", "required": "required",}),
                              max_length=20,error_messages={"required": "密码不能为空",})

class RegForm(forms.Form):
    '''
    注册表单
    '''
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "用户名", "required": "required",}),
                              max_length=50,error_messages={"required": "用户名不能为空",})
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Email", "required": "required",}),
                              max_length=50,error_messages={"required": "email不能为空",})
    url = forms.URLField(widget=forms.TextInput(attrs={"placeholder": "Url", }),
                              max_length=100, required=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "密码", "required": "required",}),
                              max_length=20,error_messages={"required": "密码不能为空",})
#修改个人信息表单
class ChangeForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "昵称", "required": "required", }),
                                   max_length=50, error_messages={"required": "昵称不能为空", })
    qq = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "qq号码", "required": "required", }),
                                 max_length=50, error_messages={"required": "qq不能为空", })
    moblie=forms.CharField(widget=forms.TextInput(attrs={"placeholder": "手机号码", "required": "required", }),
                                 max_length=50, error_messages={"required": "手机号码不能为空", })
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Email", "required": "required", }),
                                 max_length=50, error_messages={"required": "email不能为空", })
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "密码", "required": "required", }),
                                   max_length=20, error_messages={"required": "密码不能为空", })



