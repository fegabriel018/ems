from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('redirect-admin', RedirectView.as_view(url="/admin"),name="redirect-admin"),
    path('', views.index, name="index-page"),
    path('home', views.home, name="home-page"),
    path('login', auth_views.LoginView.as_view(template_name = 'employee_information/login.html',redirect_authenticated_user=True), name="login"),
    path('userlogin', views.login_user, name="login-user"),
    path('logout', views.logoutuser, name="logout"),
    path('about', views.about, name="about-page"),
    path('departments', views.departments, name="department-page"),
    path('manage_departments', views.manage_departments, name="manage_departments-page"),
    path('save_department', views.save_department, name="save-department-page"),
    path('delete_department', views.delete_department, name="delete-department"),
    #Predio
    path('predio', views.predio, name="predio-page"),
    path('manage_predio', views.manage_predio, name="manage_predio-page"),
    path('save_predio', views.save_predio, name="save-predio-page"),
    path('delete_predio', views.delete_predio, name="delete-predio"),
    #Fim Predio
    #Apartamento
    path('apartamento', views.apartamento, name="apartamento-page"),
    path('manage_apartamento', views.manage_apartamento, name="manage_apartamento-page"),
    path('save_apartamento', views.save_apartamento, name="save-apartamento-page"),
    path('delete_apartamento', views.delete_apartamento, name="delete-apartamento"),
    
    #Loja
    path('loja', views.loja, name="loja-page"),
    path('manage_loja', views.manage_loja, name="manage_loja-page"),
    path('save_loja', views.save_loja, name="save-loja-page"),
    path('delete_loja', views.delete_loja, name="delete-loja"),
    #Fim Loja
    
    
    
    
    #Fim Apartamento
    path('positions', views.positions, name="position-page"),
    path('manage_positions', views.manage_positions, name="manage_positions-page"),
    path('save_position', views.save_position, name="save-position-page"),
    path('delete_position', views.delete_position, name="delete-position"),
    path('employees', views.employees, name="employee-page"),
    path('manage_employees', views.manage_employees, name="manage_employees-page"),
    path('save_employee', views.save_employee, name="save-employee-page"),
    path('delete_employee', views.delete_employee, name="delete-employee"),
    path('view_employee', views.view_employee, name="view-employee-page"),
    
    #Contrato
    path('contrato', views.contrato, name='contrato'),
    path('manage_contrato', views.manage_contrato, name='manage_contrato'),
    path('save_contrato', views.save_contrato, name='save_contrato'),
    path('delete_contrato', views.delete_contrato, name='delete_contrato'),
    path('contrato1/', views.contrato1, name='contrato1'),
    
    #Contrato de Venda
    path('contrato11', views.contrato11, name='contrato11'),
    path('manage_contrato1', views.manage_contrato1, name='manage_contrato1'),
    path('save_contrato1', views.save_contrato1, name='save_contrato1'),
    path('delete_contrato1', views.delete_contrato1, name='delete_contrato1'),
    #LOJA
    path('contrato2', views.contrato2, name='contrato2'),
    path('manage_contrato2', views.manage_contrato2, name='manage_contrato2'),
    path('save_contrato2', views.save_contrato2, name='save_contrato2'),
    path('delete_contrato2', views.delete_contrato2, name='delete_contrato2'),
    
    #Beckup
    path('backup/', views.backup_database, name='backup-database'),  
    path('backup1/', views.beckup, name='backup1'),
    
    #Pagamento    
    path('pagamento_list', views.pagamento_list, name='pagamento_list'),
    path('manage_pagamento', views.manage_pagamento, name='manage_pagamento'),
    path('save_pagamento', views.save_pagamento, name='save_pagamento'),
    path('delete_pagamento', views.delete_pagamento, name='delete_pagamento'),
    path('pagamento/', views.pagamento, name='pagamento'),
    
    path('pagamento_list1', views.pagamento_list1, name='pagamento_list1'),
    path('manage_pagamento1', views.manage_pagamento1, name='manage_pagamento1'),
    path('save_pagamento1', views.save_pagamento1, name='save_pagamento1'),
    path('delete_pagamento1', views.delete_pagamento1, name='delete_pagamento1'),
    
    #Manuntenção
    path('manutencao', views.manutencao, name='manutencao'),
    path('manage_manutencao', views.manage_manutencao, name='manage_manutencao'),
    path('save_manutencao', views.save_manutencao, name='save_manutencao'),
    path('delete_manutencao', views.delete_manutencao, name='delete_manutencao'),

    
    #path('download_contrato', views.download_contrato, name='download_contrato'),
    path('contrato/<int:contract_id>/pdf/', views.generate_contract_pdf, name='generate_contract_pdf'),
    path('contrato1/<int:contract_id>/pdf/', views.generate_contract_pdf1, name='generate_contract_pdf1'),
    path('contrato2/<int:contract_id>/pdf/', views.generate_contract_pdf2, name='generate_contract_pdf2'),


]

