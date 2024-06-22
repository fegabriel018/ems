from datetime import datetime
from django.db import models
from django.forms import ValidationError
from django.utils import timezone
import uuid

# Modelo De Quadro
escolha=[('1','1'),
('2','2'), ('3','3'),
('4','4'),
('5','5'),
]
class Department(models.Model):
    name = models.IntegerField()
    quatQ = models.IntegerField() 
    quatMoradia = models.IntegerField()
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return str(self.name)
    
class Predio(models.Model):
    name = models.IntegerField()
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE ,null= True) 
    loja = models.IntegerField()
    #loja = models.ForeignKey('Loja', on_delete=models.CASCADE, related_name='predios', null= True) 
    status = models.IntegerField() 
    def __str__(self):
        return str(self.name)   

class Apartamento(models.Model):
    name = models.TextField()
    predio = models.ForeignKey(Predio, on_delete=models.CASCADE)
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return self.name + ' ' +self.predio + ' '
    
class Loja(models.Model):
    name = models.TextField()
    predio = models.ForeignKey(Predio, on_delete=models.CASCADE, related_name='lojas')
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return self.name + ' ' +self.predio + ' '



class Position(models.Model):
    name = models.TextField()
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE, null= True) 
    description = models.TextField() 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return self.name + ' ' +self.department_id + ' '


class Employees(models.Model):

    code = models.CharField(max_length=100,blank=True) 
    firstname = models.TextField() 
    middlename = models.TextField(blank=True,null= True) 
    lastname = models.TextField() 
    gender = models.TextField(blank=True,null= True) 
    dob = models.DateField(blank=True,null= True) 
    contact = models.TextField()
    nacionlidade = models.TextField(blank=True,null= True)
    age = models.IntegerField()
    #address = models.TextField() 
    email = models.TextField() 
    #date_hired = models.DateField() 
    #salary = models.FloatField(default=0) 
    #status = models.IntegerField() 

    #date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.firstname + ' ' +self.middlename + ' '+self.lastname + ' '+self.code + ' '
    
    
class Contrato(models.Model):
    cliente = models.ForeignKey(Employees, on_delete=models.CASCADE)
    apartamento = models.ForeignKey(Apartamento, on_delete=models.CASCADE, null=True, blank=True)
    moradia = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True)
    data_inicio = models.DateField(null=True)
    data_fim = models.DateField(null=True, blank=True)
    valor_contratual = models.DecimalField(max_digits=20, decimal_places=2)
    termos_contrato = models.TextField(default='')
    data_assinatura = models.DateField(null=True)
    forma_pagamento = models.CharField(max_length=100)
    #tipo_contrato = models.CharField(max_length=100, choices=(('venda', 'Venda'), ('aluguel', 'Aluguel')))
    ativo = models.BooleanField(default=True)
    codigo = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def clean(self):
        if self.apartamento and self.moradia:
            raise ValidationError("Um contrato só pode ser registrado com um apartamento ou com uma moradia, mas não com ambos ao mesmo tempo.")
        
    def __str__(self):
        return f"Contrato de {self.cliente} - Apartamento: {self.apartamento} | Moradia: {self.moradia}"

    
    
    
class Contrato1(models.Model):
    cliente = models.ForeignKey(Employees, on_delete=models.CASCADE, null=False, default='')
    apartamento = models.ForeignKey(Apartamento, on_delete=models.CASCADE, null=True, blank=True)
    moradia = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True)
    data_inicio = models.DateField(default=None, null=True)
   
    valor_contratual = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    termos_contrato = models.TextField(default='')
    data_assinatura = models.DateField(default=timezone.now)
    forma_pagamento = models.CharField(max_length=100, default='')
    
    ativo = models.BooleanField(default=True)
    codigo = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    def clean(self):
        if self.apartamento and self.moradia:
            raise ValidationError("Um contrato só pode ser registrado com um apartamento ou com uma moradia, mas não com ambos ao mesmo tempo.")
        
    def __str__(self):
        return f"Contrato de {self.cliente} - Apartamento: {self.apartamento} | Moradia: {self.moradia}"
    
class Contrato2(models.Model):
    cliente = models.ForeignKey(Employees, on_delete=models.CASCADE, null=False, default='')
    apartamento = models.ForeignKey(Loja, on_delete=models.CASCADE, null=True, blank=True)
    #moradia = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True)
    data_inicio = models.DateField(default=None, null=True)
   
    valor_contratual = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    termos_contrato = models.TextField(default='')
    data_assinatura = models.DateField(default=timezone.now)
    forma_pagamento = models.CharField(max_length=100, default='')
    
    ativo = models.BooleanField(default=True)
    codigo = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    def __str__(self):
        return f"Contrato de {self.cliente} - Apartamento: {self.apartamento}"
    
class Pagamento(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField(default=timezone.now)
    metodo_pagamento = models.CharField(max_length=100)
    mes = models.CharField(max_length=100, null=False, default='')
    def __str__(self):
        return f"Pagamento de {self.valor_pago} para {self.contrato.cliente} em {self.data_pagamento}"
    
    
class Pagamento1(models.Model):
    contrato = models.ForeignKey(Contrato1, on_delete=models.CASCADE)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField(default=timezone.now)
    metodo_pagamento = models.CharField(max_length=100)
    def __str__(self):
        return f"Pagamento de {self.valor_pago} para {self.contrato.cliente} em {self.data_pagamento}"
    

class Pagamento2(models.Model):
    contrato = models.ForeignKey(Contrato2, on_delete=models.CASCADE)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField(default=timezone.now)
    metodo_pagamento = models.CharField(max_length=100)
    def __str__(self):
        return f"Pagamento de {self.valor_pago} para {self.contrato.cliente} em {self.data_pagamento}"