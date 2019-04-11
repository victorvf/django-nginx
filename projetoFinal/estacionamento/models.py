from django.db import models

############################### Models ########################################
class People(models.Model):
    name = models.CharField('Nome',max_length=40)
    address = models.CharField('Endereço',max_length=100)
    telephone = models.CharField('Telefone',max_length=14)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Pessoa'

#BRAND = MARCA
class Brand(models.Model):
    name = models.CharField('Nome',max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Marca'

class Vehicle(models.Model):
    board = models.CharField('Placa',max_length=7)
    color = models.CharField('Cor',max_length=10)
    note = models.TextField(verbose_name='Observação')
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, null=True, verbose_name='Marca')
    owner = models.ForeignKey('People', on_delete=models.CASCADE, null=True, verbose_name='Proprietário(a)')

    def __str__(self):
        return self.board

    class Meta:
        verbose_name = 'Veículo'

class Parameter(models.Model):
    hour_value = models.DecimalField(max_digits=5, decimal_places=2)
    month_value = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.hour_value + '-' + self.month_value

    class Meta:
        verbose_name = 'Parâmetros'

class Rotary(models.Model):
    input = models.DateTimeField('Entrada',auto_now=False)
    output = models.DateTimeField('Saída',auto_now=False, blank=True, null=True)
    paid = models.BooleanField(default=False, verbose_name='Pago')
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE, verbose_name='Veículo')

    def result_paid(self):
        return yes_paid(self)

    def total_hour(self):
        #import math -- math.ceil() ela arredonda qualquer valor pra mais, tipo 0.1 vai pra 1
        return calculo_hora(self)

    def __str__(self):
        return self.vehicle.board

    class Meta:
        verbose_name = 'Rotativo'

class Monthly(models.Model):
    input = models.DateTimeField('Entrada', auto_now=False)
    output = models.DateTimeField('Saída', auto_now=False, blank=True, null=True)
    paid = models.BooleanField(default=False, verbose_name='Pago')
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE, verbose_name='Veículo')

    def result_paid(self):
        return yes_paid(self)

    def total_month(self):
        return calculo_mes(self)

    def __str__(self):
        return self.vehicle.board

    class Meta:
        verbose_name = 'Mensalista'

######################## Regras de Negócio ####################################
def yes_paid(obj):
    if obj.paid:
        return 'Sim'
    else:
        return 'Não'

def calculo_hora(obj):
    value = Parameter.objects.first()
    hour_value = int(value.hour_value)

    hour_total = ((obj.output - obj.input).total_seconds())//3600
    if hour_total <= 1:
        return str(hour_value)+'R$'
    else:
        return str(hour_total*hour_value)+'R$'

def calculo_mes(obj):
    value = Parameter.objects.first()
    month_value = int(value.month_value)

    month_total = ((obj.output - obj.input).total_seconds()//3600)//730
    if month_total == 1:
        return str(month_value)+'R$'
    else:
        return str(month_total*month_value)+'R$'
