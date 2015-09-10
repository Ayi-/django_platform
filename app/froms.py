# -*- coding:utf-8 -*-
# ****************************************************************#
# ScriptName:
# Author: Eli
# Create Date:2015-07-17 11：12
# Modify Author:
# Modify Date:
# Function: 模型函数
# ****************************************************************#

from django import forms
from app.models import User
from django.utils.translation import ugettext_lazy as _

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        error_messages={'required': u'请输入用户名！',},
    )
    password = forms.CharField(
        required=True,
        error_messages={'required': u'请输入密码！'},
                               )
    def clean(self):
        try:
            cleaned_data = super(LoginForm, self).clean()
            username = cleaned_data.get("username")
            password = cleaned_data.get("password")
            user = User.objects.get(username=username)
        except:
             # raise forms.ValidationError(_(u'用户不存在'),code='invalid')
             if username:
                self.add_error('username', _(u'用户不存在！'))
        else:
            if password and not user.check_password(password):

                self.add_error('password', _(u'密码错误！'))
            return cleaned_data

# model Form
# class MyUserForm(forms.ModelForm):
#
#     def __init__(self, *args, **kwarg):
#         super(MyUserForm, self).__init__(*args, **kwarg)
#         self.fields['username'].required = True  # 设置字段为必填，而不需要在改写model的filed，如下
#         self.fields['pasword'].required = True  # pasword = forms.CharField(required=True)
#
#     def clean_username(self):
#         cleaned_data=super(MyUserForm,self).clean()
#         username=cleaned_data.get('username')
#
#
#     def clean(self):
#         cleaned_data=super(MyUserForm,self).clean()
#         username=cleaned_data.get('username')
#         if User.objects.filter(username=username).count() is not 0:
#             msg = u'用户已经存在'
#             self._errors['username']=self.error_class([msg])
#             del cleaned_data['username']
#         return cleaned_data
#
#     class Meta:
#         model = User
#         fields=('username','password')  # 设置field
#         # fields = '__all__'