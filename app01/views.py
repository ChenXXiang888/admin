from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.


def index(request):
    """进入首页"""
    # 调用模型
    # 模板界面要显示的动态数据(字典)
    context = {
        'name': 'django',
        'sex': '男',
        'age': 25,
        'salary': 10000,
        'hobby': ['python', 'c/c++', 'java']
    }

    # # 方式一:
    # # 调用模板
    # # 加载模板,得到一个Template对象
    # # alt + enter: 导包
    # template = loader.get_template('index.html')
    # # 模板渲染, 生成标准的html界面内容
    # html_str = template.render(context, request)
    # # 响应请求,返回html界面给浏览器显示
    # return HttpResponse(html_str)

    # 方式二: ctrl + p: 查看参数
    return render(request, 'app01/index.html', context)


# def show_deps(request):
#     """显示所有的部门"""
#     # 查询所有的部门信息
#     # QuerySet对象
#     departments = Department.objects.all()
#     # 定义模板显示的数据
#     context = {
#         'departments': departments
#     }
#     # 调用模板,请求请求
#     # HttpResponse
#     return render(request, 'app01/show_deps.html', context)
#
#
# def show_dep(request, dep_id):
#     """
#     显示部门下所有的员工
#     :param request:
#     :param dep_id: 部门id
#     :return:
#     """
#     # 查询部门下所有的员工
#     d = Department.objects.get(id=dep_id)
#     employees = d.employee_set.all()
#
#     context = {
#         'department': d,
#         'employees': employees
#     }
#     # 响应请求
#     return render(request, 'app01/show_dep.html', context)



