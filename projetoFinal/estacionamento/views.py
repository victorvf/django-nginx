from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils import timezone
from . import models
from . import forms

############## CLASS-BASED ##################

from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

############### END CLASS-BASED ################

########### PDF #################
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import io
from django.views import View

class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)

class Pdf(View):

    def get(self, request, model):
        if model == 'people':
            objetos = models.People.objects.all()
        elif model == 'vehicle':
            objetos = models.Vehicle.objects.all()
        elif model == 'monthly':
            objetos = models.Monthly.objects.all()
        else:
            objetos = models.Rotary.objects.all()

        params = {
            'request': request,
            'objetos': objetos,
            'model': model,
        }
        return Render.render('estacionamento/relatorio.html', params, 'relatorio')
########### END-PDF #################

@login_required #login_required não precisa ser colocado pra quem utilizar o as_view() na urls.py
def home(request):
    context = {'mensagem':'Olaa mundo'}
    return render(request, 'estacionamento/index.html', {'context':context})

########### PEOPLE #################
@login_required
def list_peoples(request):
    peoples = models.People.objects.all().order_by('id')
    return render(request, 'estacionamento/people/list_people.html', {'peoples':peoples})

@login_required
def detail_people(request, id):
    people = get_object_or_404(models.People, id=id)
    return render(request, 'estacionamento/people/detail_people.html', {'people':people})

@login_required
def new_people(request):
    if request.method == "POST":
        form_people = forms.PeopleForm(request.POST)
        if form_people.is_valid():
            people = form_people.save(commit=False)
            people.save()
            return redirect('detail_people', id=people.id)
    else:
        form_people = forms.PeopleForm()
    return render(request, 'estacionamento/people/edit_people.html', {'form':form_people})

@login_required
def update_people(request, id):
    people = get_object_or_404(models.People, id=id)
    if request.method == 'POST':
        form_people = forms.PeopleForm(request.POST, instance=people)
        if form_people.is_valid():
            f_people = form_people.save(commit=False)
            f_people.save()
            return redirect('detail_people', id=f_people.id)
    else:
        form_people = forms.PeopleForm(instance=people)
    return render(request, 'estacionamento/people/edit_people.html', {'form':form_people})

@login_required
def delete_people(request, id):
    people = get_object_or_404(models.People, id=id)
    if request.method == 'POST':
        people.delete()
        return redirect('list_people')
    else:
        return render(request, 'estacionamento/people/delete_people.html', {'people':people})

########### END-PEOPLE #################

########### ROTARY ####################

class ListRotary(ListView):
    model = models.Rotary
    template_name = 'estacionamento/rotary/list_rotary.html'
    context_object_name = 'rotaries'

class DetailRotary(DetailView):
    model = models.Rotary
    template_name = 'estacionamento/rotary/detail_rotary.html'
    context_object_name = 'rotary'

class CreateRotary(CreateView):
    model = models.Rotary
    template_name = 'estacionamento/rotary/edit_rotary.html'
    fields = ['input','output','paid','vehicle']
    success_url = '/rotativos/'

class UpdateRotary(UpdateView):
    model = models.Rotary
    template_name = 'estacionamento/rotary/edit_rotary.html'
    fields = ['input','output','paid','vehicle']
    context_object_name = 'update'
    success_url = '/rotativos/{id}/'

class DeleteRotary(DeleteView):
    template_name = 'estacionamento/rotary/delete_rotary.html'
    model = models.Rotary
    context_object_name = 'rotary'
    success_url = reverse_lazy('list_rotary')

########### END-ROTARY ####################

########### VEHICLE ####################
@login_required
def list_vehicle(request):
    vehicles = models.Vehicle.objects.all().order_by('id')
    return render(request, 'estacionamento/vehicle/list_vehicle.html', {'vehicles':vehicles})

@login_required
def detail_vehicle(request, id):
    vehicle = get_object_or_404(models.Vehicle, id=id)
    return render(request,'estacionamento/vehicle/detail_vehicle.html', {'vehicle':vehicle})

@login_required
def create_vehicle(request):
    if request.method == 'POST':
        form_vehicle = forms.VehicleForm(request.POST)
        if form_vehicle.is_valid():
            vehicle = form_vehicle.save(commit=False)
            vehicle.save()
            return redirect('detail_vehicle', id=vehicle.id)
    else:
        form_vehicle = forms.VehicleForm()
    return render(request, 'estacionamento/vehicle/edit_vehicle.html', {'form':form_vehicle})

@login_required
def update_vehicle(request, id):
    vehicle = get_object_or_404(models.Vehicle, id=id)
    if request.method == 'POST':
        form_vehicle = forms.VehicleForm(request.POST, instance=vehicle)
        if form_vehicle.is_valid():
            vehicle_save = form_vehicle.save(commit=False)
            vehicle_save.save()
            return redirect('detail_vehicle',id=vehicle_save.id)
    else:
        form_vehicle = forms.VehicleForm(instance=vehicle)
    return render(request, 'estacionamento/vehicle/edit_vehicle.html', {'form':form_vehicle})

class DeleteVehicle(DeleteView):
    template_name = "estacionamento/vehicle/delete_vehicle.html"
    model = models.Vehicle
    context_object_name = 'vehicle'
    success_url = reverse_lazy('list_vehicle')

########### END-VEHICLE ####################

########### MONTHLY ####################
class ListMonthly(ListView):
    model = models.Monthly
    template_name = 'estacionamento/monthly/list_monthly.html'
    context_object_name = 'monthly'

class DetailMonthly(DetailView):
    model = models.Monthly
    template_name = 'estacionamento/monthly/detail_monthly.html'
    context_object_name = 'month'

class CreateMonthly(CreateView):
    model = models.Monthly
    template_name = 'estacionamento/monthly/edit_monthly.html'
    fields = ['input','output','paid','vehicle']
    success_url = reverse_lazy('list_monthly')

class UpdateMonthly(UpdateView):
    model = models.Monthly
    template_name = 'estacionamento/monthly/edit_monthly.html'
    fields = ['input','output','paid','vehicle']
    context_object_name = 'update'
    success_url = reverse_lazy('list_monthly')

class DeleteMonthly(DeleteView):
    template_name = 'estacionamento/monthly/delete_monthly.html'
    model = models.Monthly
    context_object_name = 'month'
    success_url = reverse_lazy('list_monthly')

########### END-MONTHLY ####################
