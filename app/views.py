# -*- coding:utf-8 -*-
# ****************************************************************#
# ScriptName:
# Author: Eli
# Create Date:2015-07-13 14:56:09
# Modify Author:
# Modify Date:
# Function: 视图函数
# ****************************************************************#
import json
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db.models.query_utils import Q
from django.template.context import Context
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, render, redirect

from app.froms import LoginForm
from app.modelchoice import modelchoice
from app.models import User, MyCustomBackend, EquipmentForConstructionMachine


@login_required
def index(request):
    return render_to_response('index.html')


def loginApp(request):
    if request.method == 'POST':
        loginForm = LoginForm(request.POST)

        if loginForm.is_valid():
            user = authenticate(username=loginForm.cleaned_data['username'],
                                password=loginForm.cleaned_data['password'])

            if user and user.is_authenticated():
                user.set_last_time()  # 更新登录时间
                login(request, user)
                return redirect('/')  # Redirect after POST
    else:
        loginForm = LoginForm()
    return render(request, 'login.html', locals())


@login_required
def logoutApp(request):
    logout(request)
    return redirect('/login')


from django.http import JsonResponse, HttpResponse





def ajax_tem(request):

    if request.is_ajax():  # 判断request请求是否是Ajax类型的
        # 获取模型名
        ob = request.GET.get('name')
        request.session['model'] = ob


        # 获取列的数据
        order_columns = [f for f in modelchoice.get(request.GET.get('name')).objects.first()._meta.fields]

        t = get_template('table.html')  # 获取模板内容


        # 获取模板
        content_html = t.render({'order_columns': order_columns})  # 渲染模板生成想要的全部局部html内容，而不是某一个变量
        columns = [{'data':column.attname }for column in order_columns]

        payload = {
            'content_html': content_html,
            'columns': columns,
            'ob':ob,
            'success': True}  # 构造json类型数据，以方便前端处理

        return HttpResponse(json.dumps(payload),  # 这个地方最好保证用json的方法传送数据，否则会出现意想不到的错误
                            content_type="application/json")  # 用json类型返回数据到前端


from django_datatables_view.base_datatable_view import BaseDatatableView


class OrderListJson(BaseDatatableView):

    def prepare_results(self, qs):
        data = []

        for item in qs:
            data.append(item.get_dict())

        return data

    def  initialize(self, *args, **kwargs):
        self.model = modelchoice.get(self.request.session.get('model'))
        self.columns = [f.name for f in self.model.objects.first()._meta.fields]
