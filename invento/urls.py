"""invento URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include

from inventory import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.invento, name='home'),
    path('register/', views.reg, name='registration'),
    path('login/',views.branchlog, name='brlog'),
    path('branch_home/', views.bhome),
    path('product/', views.phome, name= 'product'),
    path('p_details/', views.pro, name='pdetails' ),
    path('emp/', views.emp, name='empdetails'),
    path('branch_prod/', views.bpro, name='bpro'),
    path('logout/', views.logout),
    path('smt/', views.smt),
    path('rgh/', views.sampl, name='sampl'),
    path('stk/', views.stok, name='stock'),
    path('elc/', views.ele),
    path('srd/', views.storage),
    path('ped/', views.editp, name='editp'),
    path('viewemp', views.view_emp, name='view'),
    path('edit_emp/<id>', views.e_emp, name='editEmp'),
    path('updateEmp/<id>', views.nxt, name='e_dit'),
    path('delEmp/<id>', views.delEmp, name='deleteEmp'),
    path('searchemp/', views.edit, name='edit'),
    path('admin_stockview/', views.stockview, name='stkv'),
    path('addstk/<id>', views.addstk, name='addStock'),
    path('req/', views.reqst, name='reqform'),
    path('reqst/<id>', views.rform, name='reqStock'),
    path('reqstview/', views.viewreq, name='viewreq'),
    path('delreqst/<id>', views.delrq, name='delReq'),
    path('viewpro/', views.proview, name='proview'),
    path('delpro/<id>', views.delp, name = 'delPro'),
    path('branchall/', views.branchall, name="all"),
    path('editbranch/<id>', views.editb, name = 'editBranch'),
    path('delbranch/<id>', views.delb, name = 'deleteOut'),
    path('change/',views.change,name ='clog')


 ]