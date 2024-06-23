from django.shortcuts import redirect, render
from django.http import HttpResponse
from employee_information.models import Department, Position, Employees, Predio, Apartamento, Contrato, Contrato1, Loja, Contrato2, Pagamento, Pagamento1, Pagamento2, Manutencao
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import json
from datetime import datetime, timedelta


# Login
def login_user(request):
    logout(request)
    resp = {"status":'failed','msg':''}
    username = ''
    password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                resp['status']='success'
            else:
                resp['msg'] = "Nome de usuário ou senha incorreta"
        else:
            resp['msg'] = "Nome de usuário ou senha incorreta"
    return HttpResponse(json.dumps(resp),content_type='application/json')

#Logout
def logoutuser(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')

def index(request):
    return render(request,'employee_information/index.html')

# Create your views here.
@login_required
def home(request):
    context = {
        'page_title':'Home',
        'employees':employees,
        'total_department':len(Department.objects.all()),
        'total_apartamento':len(Apartamento.objects.all()),
        #'total_position':len(Position.objects.all()),
        'total_employee':len(Employees.objects.all()),
        'total_predio':len(Predio.objects.all()),
        'total_moradia':len(Position.objects.all()),
    }
    return render(request, 'employee_information/home.html',context)


def about(request):
    context = {
        'page_title':'About',
    }
    return render(request, 'employee_information/about.html',context)

# Quadra
@login_required
def departments(request):
    department_list = Department.objects.all()
    context = {
        'page_title':'Departments',
        'departments':department_list,
    }
    return render(request, 'employee_information/departments.html',context)
@login_required
def manage_departments(request):
    department = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            department = Department.objects.filter(id=id).first()
    
    context = {
        'department' : department
    }
    return render(request, 'employee_information/manage_department.html',context)

@login_required
def save_department(request):
    data =  request.POST
    resp = {'status':'failed'}
    if (data['id']).isnumeric() and int(data['id']) > 0:
        check  = Department.objects.exclude(id = data['id']).filter(name = data['name'])
    else:
        check  = Department.objects.filter(name = data['name'])

    if len(check) > 0:
        resp['status'] = 'failed'
        resp['msg'] = 'Quadra já registrada'
    else:
        try:
            if (data['id']).isnumeric() and int(data['id']) > 0 :
                save_department = Department.objects.filter(id = data['id']).update(name=data['name'], quatQ = data['quatQ'] , quatMoradia = data['quatMoradia'] ,status = data['status'])
            else:
                save_department = Department(name=data['name'], quatQ = data['quatQ'] , quatMoradia = data['quatMoradia'],status = data['status'])
                save_department.save()
            resp['status'] = 'success'
        except:
            resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_department(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Department.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")



# Prédio
@login_required
def predio(request):
    predio_list = Predio.objects.all()
    context = {
        'page_title':'Predios',
        'predios':predio_list,
    }
    return render(request, 'employee_information/predio.html',context)
@login_required
def manage_predio(request):
    predio = {}
    departments = Department.objects.all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            predio = Predio.objects.filter(id=id).first()
    
    context = {
        'predio' : predio,
        'departments' : departments
    }
    return render(request, 'employee_information/manage_predio.html',context)

@login_required
def save_predio(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        dept = Department.objects.filter(id=data['department_id']).first()
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_predio = Predio.objects.filter(id = data['id']).update(name=data['name'], department_id = dept, loja = data['loja'],status = data['status'])
        else:
            save_predio = Predio(name=data['name'],department_id = dept, loja = data['loja'],status = data['status'])
            save_predio.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
        print(Exception)
        print(json.dumps({"name":data['name'], "department_id" : data['department_id'], "loja" : data['loja'],"status" : data['status']}))
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_predio(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Predio.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")



#Apartamento
@login_required
def apartamento(request):
    apartamento_list = Apartamento.objects.all()
    context = {
        'page_title':'Apartamento',
        'apartamentos':apartamento_list,
    }
    return render(request, 'employee_information/apartamento.html',context)
@login_required
def manage_apartamento(request):
    apartamento = {}
    predios = Predio.objects.all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            apartamento = Apartamento.objects.filter(id=id).first()
    
    context = {
        'apartamento' : apartamento,
        'predios' : predios
        
    }
    return render(request, 'employee_information/manage_apartamento.html',context)

@login_required
def save_apartamento(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        dept = Predio.objects.filter(id=data['predio']).first()
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_apartamento = Apartamento.objects.filter(id = data['id']).update(name=data['name'], predio = dept, status = data['status'])
        else:
            save_apartamento = Apartamento(name=data['name'], predio = dept, status = data['status'])
            save_apartamento.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
        print(Exception)
        print(json.dumps({"name":data['name'], "predio" : data['predio'], "status" : data['status']}))
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_apartamento(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Apartamento.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")




#Loja
@login_required
def loja(request):
    apartamento_list = Loja.objects.all()
    context = {
        'page_title':'Apartamento',
        'apartamentos':apartamento_list,
    }
    return render(request, 'employee_information/loja.html',context)

@login_required
def manage_loja(request):
    apartamento = {}
    predios = Predio.objects.all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            apartamento = Loja.objects.filter(id=id).first()
    
    context = {
        'apartamento' : apartamento,
        'predios' : predios
        
    }
    return render(request, 'employee_information/manage_loja.html',context)

@login_required
def save_loja(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        dept = Predio.objects.filter(id=data['predio']).first()
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_apartamento = Loja.objects.filter(id = data['id']).update(name=data['name'], predio = dept, status = data['status'])
        else:
            save_apartamento = Loja(name=data['name'], predio = dept, status = data['status'])
            save_apartamento.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
        print(Exception)
        print(json.dumps({"name":data['name'], "predio" : data['predio'], "status" : data['status']}))
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_loja(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Loja.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")





# Positions
@login_required
def positions(request):
    position_list = Position.objects.all()
    context = {
        'page_title':'Positions',
        'positions':position_list,
    }
    return render(request, 'employee_information/positions.html',context)
@login_required
def manage_positions(request):
    position = {}
    departments = Department.objects.all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            position = Position.objects.filter(id=id).first()
    
    context = {
        'position' : position,
        'departments' : departments
    }
    return render(request, 'employee_information/manage_position.html',context)

@login_required
def save_position(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        dept = Department.objects.filter(id=data['department_id']).first()
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_position = Position.objects.filter(id = data['id']).update(name=data['name'],department_id = dept, description = data['description'],status = data['status'])
        else:
            save_position = Position(name=data['name'],department_id = dept, description = data['description'],status = data['status'])
            save_position.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
        print(Exception)
        print(json.dumps({"name":data['name'], "department_id" : data['department_id'],"status" : data['status']}))
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_position(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Position.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


# Employees
import csv
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

@login_required
def employees(request):
    employee_list = Employees.objects.all()
    
    # Check if the request is for CSV download
    if 'csv' in request.GET:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="employees.csv"'

        writer = csv.writer(response)
        writer.writerow(['ID', 'First Name', 'Middle Name', 'Last Name', 'Code', 'Date of Birth', 'Gender', 'Nationality'])
        for employee in employee_list:
            writer.writerow([
                employee.id,
                employee.firstname,
                employee.middlename,
                employee.lastname,
                employee.code,
                employee.dob,
                employee.gender,
                employee.nacionlidade
            ])

        return response

    # Check if the request is for PDF download
    elif 'pdf' in request.GET:
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="employees.pdf"'

        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter

        p.drawString(100, height - 40, "Employee List")

        x_offset = 50
        y_offset = height - 80
        line_height = 20

        p.drawString(x_offset, y_offset, 'ID')
        p.drawString(x_offset + 40, y_offset, 'First Name')
        p.drawString(x_offset + 140, y_offset, 'Middle Name')
        p.drawString(x_offset + 240, y_offset, 'Last Name')
        p.drawString(x_offset + 340, y_offset, 'Code')
        p.drawString(x_offset + 440, y_offset, 'Date of Birth')
        p.drawString(x_offset + 540, y_offset, 'Gender')
        p.drawString(x_offset + 600, y_offset, 'Nationality')

        y_offset -= line_height

        for employee in employee_list:
            p.drawString(x_offset, y_offset, str(employee.id))
            p.drawString(x_offset + 40, y_offset, employee.firstname)
            p.drawString(x_offset + 140, y_offset, employee.middlename or "")
            p.drawString(x_offset + 240, y_offset, employee.lastname)
            p.drawString(x_offset + 340, y_offset, employee.code)
            p.drawString(x_offset + 440, y_offset, str(employee.dob))
            p.drawString(x_offset + 540, y_offset, employee.gender or "")
            p.drawString(x_offset + 600, y_offset, employee.nacionlidade or "")

            y_offset -= line_height
            if y_offset < 40:
                p.showPage()
                y_offset = height - 40

        p.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    context = {
        'page_title': 'Employees',
        'employees': employee_list,
    }
    return render(request, 'employee_information/employees.html', context)




@login_required
def manage_employees(request):
    employee = {}
    
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Employees.objects.filter(id=id).first()
    context = {
        'employee' : employee,

    }
    return render(request, 'employee_information/manage_employee.html',context)



@login_required
def save_employee(request):
    data = request.POST
    resp = {'status': 'failed'}

    # Verificar se há números nos campos de nome
    if any(char.isdigit() for char in data['firstname']) or any(char.isdigit() for char in data['middlename']) or any(char.isdigit() for char in data['lastname']):
        resp['msg'] = 'Nome não pode conter números'
        return HttpResponse(json.dumps(resp), content_type="application/json")

    # Validar a data de nascimento e garantir que o funcionário tenha pelo menos 18 anos
    try:
        dob = datetime.strptime(data['dob'], '%Y-%m-%d')
        if datetime.now().date() - dob.date() < timedelta(days=365 * 18):
            resp['msg'] = 'O cliente deve ter pelo menos 18 anos de idade.'
            return HttpResponse(json.dumps(resp), content_type="application/json")
    except ValueError:
        resp['msg'] = 'Data de nascimento inválida.'
        return HttpResponse(json.dumps(resp), content_type="application/json")

    # Verificar se há duplicatas no código 
    if data['id'].isnumeric() and int(data['id']) > 0:
        check = Employees.objects.exclude(id=data['id']).filter(code=data['code'])
    else:
        check = Employees.objects.filter(code=data['code'])

    if check.exists():
        resp['msg'] = 'BI/Passaporte já registrado'
        return HttpResponse(json.dumps(resp), content_type="application/json")

    try:
        if data['id'].isnumeric() and int(data['id']) > 0:
            employee = Employees.objects.get(id=data['id'])
            employee.code = data['code']
            employee.firstname = data['firstname']
            employee.middlename = data['middlename']
            employee.lastname = data['lastname']
            employee.dob = data['dob']
            employee.gender = data['gender']
            employee.contact = data['contact']
            employee.email = data['email']
            employee.nacionlidade = data['nacionlidade']
            employee.age = data['age']
            employee.save()
        else:
            Employees.objects.create(
                code=data['code'],
                firstname=data['firstname'],
                middlename=data['middlename'],
                lastname=data['lastname'],
                dob=data['dob'],
                gender=data['gender'],
                contact=data['contact'],
                email=data['email'],
                nacionlidade=data['nacionlidade'],
                age=data['age']
            )
        resp['status'] = 'success'
    except Exception as e:
        resp['msg'] = str(e)

    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_employee(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Employees.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def view_employee(request):
    employee = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Employees.objects.filter(id=id).first()
    context = {
        'employee' : employee,

    }
    return render(request, 'employee_information/view_employee.html',context)




# Gestão de Contratos
@login_required
def contrato1(request):
    return render(request, 'employee_information/contrato1.html')



from django.db.models import Q
@login_required
def contrato(request):
    contrato_list = Contrato.objects.all()
    context = {
        'page_title': 'Contratos',
        'contratos': contrato_list,
    }
    return render(request, 'employee_information/contrato.html', context)


@login_required
def manage_contrato(request):
    contrato = {}
    clientes = Employees.objects.all()
    apartamentos = Apartamento.objects.all()
    moradias = Position.objects.all()

    if request.method == 'GET':
        data = request.GET
        id = ''
        if 'id' in data:
            id = data['id']
        if id.isnumeric() and int(id) > 0:
            contrato = Contrato.objects.filter(id=id).first()

    context = {
        'contrato': contrato,
        'clientes': clientes,
        'apartamentos': apartamentos,
        'moradias': moradias,
    }
    return render(request, 'employee_information/manage_contrato.html', context)



@login_required
def save_contrato(request):
    data = request.POST
    resp = {'status': 'failed'}

    try:
        cliente = Employees.objects.filter(id=data['cliente']).first()

        if cliente is None:
            resp['msg'] = 'Selecione um cliente válido.'
            return HttpResponse(json.dumps(resp), content_type="application/json")

        # Verificar se o cliente já possui contrato
        if Contrato.objects.filter(cliente=cliente).exists():
            resp['msg'] = 'Este cliente já possui um contrato registrado.'
            return HttpResponse(json.dumps(resp), content_type="application/json")

        apartamento_id = data.get('apartamento')
        moradia_id = data.get('moradia')

        if apartamento_id:
            apartamento = Apartamento.objects.filter(id=apartamento_id).first()
        else:
            apartamento = None

        if moradia_id:
            moradia = Position.objects.filter(id=moradia_id).first()
        else:
            moradia = None

        if 'id' in data and data['id'].isnumeric() and int(data['id']) > 0:
            contrato = Contrato.objects.filter(id=data['id']).first()
            if contrato:
                contrato.cliente = cliente
                contrato.apartamento = apartamento
                contrato.moradia = moradia
                contrato.data_inicio = data['data_inicio']
                contrato.data_fim = data['data_fim']
                contrato.valor_contratual = data['valor_contratual']
                contrato.termos_contrato = data['termos_contrato']
                contrato.data_assinatura = data['data_assinatura']
                contrato.forma_pagamento = data['forma_pagamento']
                
                contrato.ativo = data['ativo']
                contrato.save()
                resp['status'] = 'success'
        else:
            contrato = Contrato(
                cliente=cliente,
                apartamento=apartamento,
                moradia=moradia,
                data_inicio=data['data_inicio'],
                data_fim=data['data_fim'],
                valor_contratual=data['valor_contratual'],
                termos_contrato=data['termos_contrato'],
                data_assinatura=data['data_assinatura'],
                forma_pagamento=data['forma_pagamento'],
                
                ativo=data['ativo']
            )
            contrato.save()
            resp['status'] = 'success'

    except Exception as e:
        print(e)
        resp['status'] = 'failed'

    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def delete_contrato(request):
    data = request.POST
    resp = {'status': ''}
    try:
        Contrato.objects.filter(id=data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")




# CONTRATO DE VENDA
@login_required
def contrato11(request):
    contrato_list = Contrato1.objects.all()
    context = {
        'page_title': 'Contratos',
        'contratos': contrato_list,
    }
    return render(request, 'employee_information/contrato_venda.html', context)


@login_required
def manage_contrato1(request):
    contrato = {}
    clientes = Employees.objects.all()
    apartamentos = Apartamento.objects.all()
    moradias = Position.objects.all()

    if request.method == 'GET':
        data = request.GET
        id = ''
        if 'id' in data:
            id = data['id']
        if id.isnumeric() and int(id) > 0:
            contrato = Contrato1.objects.filter(id=id).first()

    context = {
        'contrato': contrato,
        'clientes': clientes,
        'apartamentos': apartamentos,
        'moradias': moradias,
    }
    return render(request, 'employee_information/manage_contrato1.html', context)



@login_required
def save_contrato1(request):
    data = request.POST
    resp = {'status': 'failed'}

    try:
        cliente = Employees.objects.filter(id=data['cliente']).first()

        if cliente is None:
            resp['msg'] = 'Selecione um cliente válido.'
            return HttpResponse(json.dumps(resp), content_type="application/json")

        # Verificar se o cliente já possui contrato
        if Contrato1.objects.filter(cliente=cliente).exists():
            resp['msg'] = 'Este cliente já possui um contrato registrado.'
            return HttpResponse(json.dumps(resp), content_type="application/json")

        apartamento_id = data.get('apartamento')
        moradia_id = data.get('moradia')

        if apartamento_id:
            apartamento = Apartamento.objects.filter(id=apartamento_id).first()
        else:
            apartamento = None

        if moradia_id:
            moradia = Position.objects.filter(id=moradia_id).first()
        else:
            moradia = None

        if 'id' in data and data['id'].isnumeric() and int(data['id']) > 0:
            contrato = Contrato1.objects.filter(id=data['id']).first()
            if contrato:
                contrato.cliente = cliente
                contrato.apartamento = apartamento
                contrato.moradia = moradia
                contrato.data_inicio = data['data_inicio']
                
                contrato.valor_contratual = data['valor_contratual']
                contrato.termos_contrato = data['termos_contrato']
                contrato.data_assinatura = data['data_assinatura']
                contrato.forma_pagamento = data['forma_pagamento']
                
                contrato.ativo = data['ativo']
                contrato.save()
                resp['status'] = 'success'
        else:
            contrato = Contrato1(
                cliente=cliente,
                apartamento=apartamento,
                moradia=moradia,
                data_inicio=data['data_inicio'],
                
                valor_contratual=data['valor_contratual'],
                termos_contrato=data['termos_contrato'],
                data_assinatura=data['data_assinatura'],
                forma_pagamento=data['forma_pagamento'],
                
                ativo=data['ativo']
            )
            contrato.save()
            resp['status'] = 'success'

    except Exception as e:
        print(e)
        resp['status'] = 'failed'

    return HttpResponse(json.dumps(resp), content_type="application/json")







@login_required
def delete_contrato1(request):
    data = request.POST
    resp = {'status': ''}
    try:
        Contrato1.objects.filter(id=data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")




#LOJAS
@login_required
def contrato2(request):
    contrato_list = Contrato2.objects.all()
    context = {
        'page_title': 'Contratos',
        'contratos': contrato_list,
    }
    return render(request, 'employee_information/contrato2.html', context)


@login_required
def manage_contrato2(request):
    contrato = {}
    clientes = Employees.objects.all()
    loja = Loja.objects.all()
    

    if request.method == 'GET':
        data = request.GET
        id = ''
        if 'id' in data:
            id = data['id']
        if id.isnumeric() and int(id) > 0:
            contrato = Contrato2.objects.filter(id=id).first()

    context = {
        'contrato': contrato,
        'clientes': clientes,
        'apartamentos': loja,
       
    }
    return render(request, 'employee_information/manage_contrato2.html', context)



@login_required
def save_contrato2(request):
    data = request.POST
    resp = {'status': 'failed'}

    try:
        cliente = Employees.objects.filter(id=data['cliente']).first()

        if cliente is None:
            resp['msg'] = 'Selecione um cliente válido.'
            return HttpResponse(json.dumps(resp), content_type="application/json")

        # Verificar se o cliente já possui contrato
        if Contrato1.objects.filter(cliente=cliente).exists():
            resp['msg'] = 'Este cliente já possui um contrato registrado.'
            return HttpResponse(json.dumps(resp), content_type="application/json")

        apartamento_id = data.get('apartamento')
        #moradia_id = data.get('moradia')

        if apartamento_id:
            apartamento = Loja.objects.filter(id=apartamento_id).first()
        else:
            apartamento = None

        

        if 'id' in data and data['id'].isnumeric() and int(data['id']) > 0:
            contrato = Contrato2.objects.filter(id=data['id']).first()
            if contrato:
                contrato.cliente = cliente
                contrato.apartamento = apartamento
                #contrato.moradia = moradia
                contrato.data_inicio = data['data_inicio']
                
                contrato.valor_contratual = data['valor_contratual']
                contrato.termos_contrato = data['termos_contrato']
                contrato.data_assinatura = data['data_assinatura']
                contrato.forma_pagamento = data['forma_pagamento']
                
                contrato.ativo = data['ativo']
                contrato.save()
                resp['status'] = 'success'
        else:
            contrato = Contrato2(
                cliente=cliente,
                apartamento=apartamento,
                #moradia=moradia,
                data_inicio=data['data_inicio'],
                
                valor_contratual=data['valor_contratual'],
                termos_contrato=data['termos_contrato'],
                data_assinatura=data['data_assinatura'],
                forma_pagamento=data['forma_pagamento'],
                
                ativo=data['ativo']
            )
            contrato.save()
            resp['status'] = 'success'

    except Exception as e:
        print(e)
        resp['status'] = 'failed'

    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_contrato2(request):
    data = request.POST
    resp = {'status': ''}
    try:
        Contrato2.objects.filter(id=data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


#Pagamentos
@login_required
def pagamento(request):
    return render(request, 'employee_information/pagamento.html')

@login_required
def pagamento_list(request):
    pagamentos = Pagamento.objects.all()
    context = {
        'page_title': 'Pagamentos',
        'pagamentos': pagamentos,
    }
    return render(request, 'employee_information/pagamento_list.html', context)

@login_required
def manage_pagamento(request):
    pagamento = {}
    contratos = Contrato.objects.all()

    if request.method == 'GET':
        data = request.GET
        id = ''
        if 'id' in data:
            id = data['id']
        if id.isnumeric() and int(id) > 0:
            pagamento = Pagamento.objects.filter(id=id).first()

    context = {
        'pagamento': pagamento,
        'contratos': contratos,
    }
    return render(request, 'employee_information/manage_pagamento.html', context)



@login_required
def save_pagamento(request):
    data = request.POST
    resp = {'status': 'failed'}

    try:
        contrato = Contrato.objects.filter(id=data['contrato']).first()

        if contrato is None:
            resp['msg'] = 'Selecione um contrato válido.'
            return HttpResponse(json.dumps(resp), content_type="application/json")

        if 'id' in data and data['id'].isnumeric() and int(data['id']) > 0:
            pagamento = Pagamento.objects.filter(id=data['id']).first()
            if pagamento:
                pagamento.contrato = contrato
                pagamento.valor_pago = data['valor_pago']
                pagamento.data_pagamento = data['data_pagamento']
                pagamento.metodo_pagamento = data['metodo_pagamento']
                pagamento.mes = data['mes']
                pagamento.save()
                resp['status'] = 'success'
        else:
            pagamento = Pagamento(
                contrato=contrato,
                valor_pago=data['valor_pago'],
                data_pagamento=data['data_pagamento'],
                metodo_pagamento=data['metodo_pagamento'],
                mes=data['mes'],
            )
            pagamento.save()
            resp['status'] = 'success'

    except Exception as e:
        print(e)
        resp['status'] = 'failed'

    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_pagamento(request):
    data = request.POST
    resp = {'status': ''}
    try:
        Pagamento.objects.filter(id=data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")



#Aquisição de loja
@login_required
def pagamento_list1(request):
    pagamentos = Pagamento1.objects.all()
    context = {
        'page_title': 'Pagamentos',
        'pagamentos': pagamentos,
    }
    return render(request, 'employee_information/pagamento_list1.html', context)

@login_required
def manage_pagamento1(request):
    pagamento = {}
    contratos = Contrato1.objects.all()

    if request.method == 'GET':
        data = request.GET
        id = ''
        if 'id' in data:
            id = data['id']
        if id.isnumeric() and int(id) > 0:
            pagamento = Pagamento1.objects.filter(id=id).first()

    context = {
        'pagamento': pagamento,
        'contratos': contratos,
    }
    return render(request, 'employee_information/manage_pagamento1.html', context)



@login_required
def save_pagamento1(request):
    data = request.POST
    resp = {'status': 'failed'}

    try:
        contrato = Contrato1.objects.filter(id=data['contrato']).first()

        if contrato is None:
            resp['msg'] = 'Selecione um contrato válido.'
            return HttpResponse(json.dumps(resp), content_type="application/json")

        if 'id' in data and data['id'].isnumeric() and int(data['id']) > 0:
            pagamento = Pagamento1.objects.filter(id=data['id']).first()
            if pagamento:
                pagamento.contrato = contrato
                pagamento.valor_pago = data['valor_pago']
                pagamento.data_pagamento = data['data_pagamento']
                pagamento.metodo_pagamento = data['metodo_pagamento']
                pagamento.save()
                resp['status'] = 'success'
        else:
            pagamento = Pagamento1(
                contrato=contrato,
                valor_pago=data['valor_pago'],
                data_pagamento=data['data_pagamento'],
                metodo_pagamento=data['metodo_pagamento'],
            )
            pagamento.save()
            resp['status'] = 'success'

    except Exception as e:
        print(e)
        resp['status'] = 'failed'

    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_pagamento1(request):
    data = request.POST
    resp = {'status': ''}
    try:
        Pagamento1.objects.filter(id=data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")




from django.shortcuts import render, redirect, get_object_or_404


#MANUTENÇÃO
@login_required
def manutencao(request):
    manutencoes = Manutencao.objects.all()
    context = {
        'page_title': 'Manutenções',
        'manutencoes': manutencoes,
    }
    return render(request, 'employee_information/manutencao.html', context)

@login_required
def manage_manutencao(request):
    manutencao = None
    apartamentos = Apartamento.objects.all()
    moradias = Position.objects.all()
    lojas = Loja.objects.all()

    if request.method == 'GET':
        data = request.GET
        id = data.get('id', '')
        if id.isnumeric() and int(id) > 0:
            manutencao = Manutencao.objects.filter(id=id).first()

    context = {
        'manutencao': manutencao,
        'apartamentos': apartamentos,
        'moradias': moradias,
        'lojas': lojas,
    }
    return render(request, 'employee_information/manage_manutencao.html', context)

@login_required
def save_manutencao(request):
    data = request.POST
    resp = {'status': 'failed'}

    try:
        # Recuperar os dados básicos do formulário
        valor_pago = data.get('valor_pago')
        data_manutencao = data.get('data_manutencao')
        descricao = data.get('descricao')
        tipo = data.get('tipo')

        # Verificar e recuperar o tipo específico
        if tipo == 'apartamento':
            entidade = Apartamento.objects.get(id=data.get('apartamento'))
        elif tipo == 'moradia':
            entidade = Position.objects.get(id=data.get('moradia'))
        elif tipo == 'loja':
            entidade = Loja.objects.get(id=data.get('loja'))
        else:
            resp['msg'] = 'Tipo de manutenção inválido.'
            return HttpResponse(json.dumps(resp), content_type="application/json")

        # Verificar se estamos editando uma manutenção existente
        if 'id' in data and data['id'].isnumeric() and int(data['id']) > 0:
            manutencao = Manutencao.objects.filter(id=data['id']).first()
            if manutencao:
                manutencao.valor_pago = valor_pago
                manutencao.data_manutencao = data_manutencao
                manutencao.descricao = descricao
                manutencao.tipo = tipo
                if tipo == 'apartamento':
                    manutencao.apartamento = entidade
                    manutencao.moradia = None
                    manutencao.loja = None
                elif tipo == 'moradia':
                    manutencao.moradia = entidade
                    manutencao.apartamento = None
                    manutencao.loja = None
                elif tipo == 'loja':
                    manutencao.loja = entidade
                    manutencao.apartamento = None
                    manutencao.moradia = None
                manutencao.save()
                resp['status'] = 'success'
            else:
                resp['msg'] = 'Manutenção não encontrada.'
        else:
            # Criar uma nova manutenção
            manutencao = Manutencao(
                valor_pago=valor_pago,
                data_manutencao=data_manutencao,
                descricao=descricao,
                tipo=tipo
            )
            if tipo == 'apartamento':
                manutencao.apartamento = entidade
            elif tipo == 'moradia':
                manutencao.moradia = entidade
            elif tipo == 'loja':
                manutencao.loja = entidade
            manutencao.save()
            resp['status'] = 'success'
    except Exception as e:
        print(e)
        resp['msg'] = str(e)

    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_manutencao(request):
    data = request.POST
    resp = {'status': ''}

    try:
        Manutencao.objects.filter(id=data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'

    return HttpResponse(json.dumps(resp), content_type="application/json")



from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generate_contract_pdf(request, contract_id):
    # Buscar o contrato com base no ID fornecido
    contract = Contrato.objects.get(pk=contract_id)

    # Criar um objeto HttpResponse com cabeçalho de PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="contrato_{contract_id}.pdf"'

    # Criar um objeto Story para adicionar elementos ao PDF
    story = []

    # Adicionar imagem no topo do contrato
    logo_path = 'static/employee_information/assets/img/rp.png'
    logo = Image(logo_path, width=80, height=80)
    story.append(logo)

    # Adicionar espaço
    story.append(Spacer(1, 24))

    # Adicionar informações do contrato
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    body_style = styles['Normal']

    head = f"""REPÚBLICA DE ANGOLA 
    """
    h = f"""__________________________________________

    """
    
    title = f'Contrato de Locação - ID: {contract_id}'
    body = f"""Este contrato é celebrado entre {contract.cliente.firstname} {contract.cliente.lastname}  nascido em {contract.cliente.dob} com BI nº {contract.cliente.code}, e a Comissão de gestão da Centralidade Horizonte do Cuito para locação do apartamento/moradia localizado no Município do Cuito, Província do Bié.
    
    Detalhes do Contrato:
    - Data de Início: {contract.data_inicio}
    - Data de Término: {contract.data_fim}
    - Valor Contratual: {contract.valor_contratual}
    - Termos do Contrato: {contract.termos_contrato}
    - Forma de Pagamento: {contract.forma_pagamento}
    """
    story.append(Paragraph(head, title_style))
    story.append(Spacer(1, 6))
    story.append(Paragraph(h, title_style))
    story.append(Spacer(1, 8))
    story.append(Paragraph(title, title_style))
    story.append(Spacer(1, 12))
    story.append(Paragraph(body, body_style))
    story.append(Spacer(1, 12))

    # Adicionar uma tabela com os detalhes do contrato
    data = [
        ['Cliente:', f"{contract.cliente.firstname} {contract.cliente.lastname}"],
        ['Apartamento:', contract.apartamento.name if contract.apartamento else 'N/A'],
        ['Moradia:', contract.moradia.name if contract.moradia else 'N/A'],
        ['Data de Início:', str(contract.data_inicio)],
        ['Data de Término:', str(contract.data_fim)],
        ['Valor Contratual:', str(contract.valor_contratual)],
        ['Termos do Contrato:', contract.termos_contrato],
        ['Forma de Pagamento:', contract.forma_pagamento],
    ]

    table = Table(data, colWidths=[120, 350])
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    story.append(table)

    # Adicionar espaço para assinaturas
    story.append(Spacer(1, 48))
    story.append(Paragraph("Assinatura do Locatário:_______________________________", body_style))
    story.append(Spacer(1, 24))
    story.append(Paragraph("Assinatura do Locador:__________________________________", body_style))

    # Criar o PDF
    doc = SimpleDocTemplate(response, pagesize=letter)
    doc.build(story)

    return response

#VENDA
def generate_contract_pdf1(request, contract_id):
    # Buscar o contrato com base no ID fornecido
    contract = Contrato1.objects.get(pk=contract_id)

    # Criar um objeto HttpResponse com cabeçalho de PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="contrato_{contract_id}.pdf"'

    # Criar um objeto Story para adicionar elementos ao PDF
    story = []

    # Adicionar imagem no topo do contrato
    logo_path = 'static/employee_information/assets/img/rp.png'
    logo = Image(logo_path, width=80, height=80)
    story.append(logo)

    # Adicionar espaço
    story.append(Spacer(1, 24))

    # Adicionar informações do contrato
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    body_style = styles['Normal']

    head = f"""REPÚBLICA DE ANGOLA 
    """
    h = f"""__________________________________________

    """
    
    title = f'Contrato de Compra - ID: {contract_id}'
    body = f"""Este contrato é celebrado entre {contract.cliente.firstname} {contract.cliente.lastname}  nascido em {contract.cliente.dob} com BI nº {contract.cliente.code}, e a Comissão de gestão da Centralidade Horizonte do Cuito para venda do apartamento/moradia localizado no Município do Cuito, Província do Bié.
    
    Detalhes do Contrato:
    - Data de Aquisição: {contract.data_inicio}
 
    - Valor Contratual: {contract.valor_contratual}
    - Termos do Contrato: {contract.termos_contrato}
    - Forma de Pagamento: {contract.forma_pagamento}
    """
    story.append(Paragraph(head, title_style))
    story.append(Spacer(1, 6))
    story.append(Paragraph(h, title_style))
    story.append(Spacer(1, 8))
    story.append(Paragraph(title, title_style))
    story.append(Spacer(1, 12))
    story.append(Paragraph(body, body_style))
    story.append(Spacer(1, 12))

    # Adicionar uma tabela com os detalhes do contrato
    data = [
        ['Cliente:', f"{contract.cliente.firstname} {contract.cliente.lastname}"],
        ['Apartamento:', contract.apartamento.name if contract.apartamento else 'N/A'],
        ['Moradia:', contract.moradia.name if contract.moradia else 'N/A'],
        ['Data de Aquisição:', str(contract.data_inicio)],     
        ['Valor Contratual:', str(contract.valor_contratual)],
        ['Termos do Contrato:', contract.termos_contrato],
        ['Forma de Pagamento:', contract.forma_pagamento],
        
    ]

    table = Table(data, colWidths=[120, 350])
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    story.append(table)

    # Adicionar espaço para assinaturas
    story.append(Spacer(1, 48))
    story.append(Paragraph("Assinatura do Vendendor:_______________________________", body_style))
    story.append(Spacer(1, 24))
    story.append(Paragraph("Assinatura do Comprador:__________________________________", body_style))

    # Criar o PDF
    doc = SimpleDocTemplate(response, pagesize=letter)
    doc.build(story)

    return response



# COMPRA DE LOJA
def generate_contract_pdf2(request, contract_id):
    # Buscar o contrato com base no ID fornecido
    contract = Contrato2.objects.get(pk=contract_id)

    # Criar um objeto HttpResponse com cabeçalho de PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="contrato_{contract_id}.pdf"'

    # Criar um objeto Story para adicionar elementos ao PDF
    story = []

    # Adicionar imagem no topo do contrato
    logo_path = 'static/employee_information/assets/img/rp.png'
    logo = Image(logo_path, width=80, height=80)
    story.append(logo)

    # Adicionar espaço
    story.append(Spacer(1, 24))

    # Adicionar informações do contrato
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    body_style = styles['Normal']

    head = f"""REPÚBLICA DE ANGOLA 
    """
    h = f"""__________________________________________

    """
    
    title = f'Contrato de Aquisição de Loja - ID: {contract_id}'
    body = f"""Este contrato é celebrado entre {contract.cliente.firstname} {contract.cliente.lastname}  nascido em {contract.cliente.dob} com BI nº {contract.cliente.code}, e a Comissão de gestão da Centralidade Horizonte do Cuito para aquisição da loja localizado no Município do Cuito, Província do Bié.
    
    Detalhes do Contrato:
    - Data de Aquisição: {contract.data_inicio}
    - Valor Contratual: {contract.valor_contratual} kz
    - Termos do Contrato: {contract.termos_contrato}
    - Forma de Pagamento: {contract.forma_pagamento}
    """
    story.append(Paragraph(head, title_style))
    story.append(Spacer(1, 6))
    story.append(Paragraph(h, title_style))
    story.append(Spacer(1, 8))
    story.append(Paragraph(title, title_style))
    story.append(Spacer(1, 12))
    story.append(Paragraph(body, body_style))
    story.append(Spacer(1, 12))

    # Adicionar uma tabela com os detalhes do contrato
    data = [
        ['Cliente:', f"{contract.cliente.firstname} {contract.cliente.lastname}"],
        ['Apartamento:', contract.apartamento.name if contract.apartamento else 'N/A'],
        ['Data de Aquisição:', str(contract.data_inicio)],     
        ['Valor Contratual:', str(contract.valor_contratual)],
        ['Termos do Contrato:', contract.termos_contrato],
        ['Forma de Pagamento:', contract.forma_pagamento],
        
    ]

    table = Table(data, colWidths=[120, 350])
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    story.append(table)

    # Adicionar espaço para assinaturas
    story.append(Spacer(1, 48))
    story.append(Paragraph("Assinatura do Vendendor:_______________________________", body_style))
    story.append(Spacer(1, 24))
    story.append(Paragraph("Assinatura do Comprador:__________________________________", body_style))

    # Criar o PDF
    doc = SimpleDocTemplate(response, pagesize=letter)
    doc.build(story)

    return response






#Beckup
@login_required
def beckup(request):
    return render(request, 'employee_information/beckup.html')






import os
import shutil
from django.conf import settings
from django.utils import timezone

from django.http import JsonResponse

def backup_database(request):
    # Definindo o caminho do arquivo de backup
    backup_dir = os.path.join(settings.BASE_DIR, 'backups')
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    timestamp = timezone.now().strftime('%Y%m%d_%H%M%S')
    backup_file = os.path.join(backup_dir, f'backup_{timestamp}.sqlite3')
    
    # Caminho do arquivo de banco de dados
    db_file = settings.DATABASES['default']['NAME']
    
    # Fazendo a cópia do arquivo
    shutil.copy(db_file, backup_file)
    
    # Retornando o caminho do arquivo de backup como JSON
    return JsonResponse({'backup_file': backup_file})
