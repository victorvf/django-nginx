from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from . import models
from . import forms

def home(request):
    context = {'mensagem':'Olaa mundo'}
    return render(request, 'estacionamento/index.html', {'context':context})

########### PEOPLE #################

def list_peoples(request):
    peoples = models.People.objects.all().order_by('id')
    return render(request, 'estacionamento/people/list_people.html', {'peoples':peoples})

def detail_people(request, id):
    people = get_object_or_404(models.People, id=id)
    return render(request, 'estacionamento/people/detail_people.html', {'people':people})

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

def delete_people(request, id):
    people = get_object_or_404(models.People, id=id)
    if request.method == 'POST':
        people.delete()
        return redirect('list_people')
    else:
        return render(request, 'estacionamento/people/delete_people.html', {'people':people})

########### END-PEOPLE #################

########### ROTARY ####################

def list_rotary(request):
    rotaries = models.Rotary.objects.all().order_by('id')
    return render(request, 'estacionamento/rotary/list_rotary.html', {'rotaries':rotaries})

def detail_rotary(request, id):
    rotary = get_object_or_404(models.Rotary, id=id)
    return render(request, 'estacionamento/rotary/detail_rotary.html', {'rotary':rotary})

def new_rotary(request):
    if request.method == 'POST':
        form_rotary = forms.RotaryForm(request.POST)
        if form_rotary.is_valid():
            rotary = form_rotary.save(commit=False)
            rotary.save()
            return redirect('detail_rotary', id=rotary.id)
    else:
        form_rotary = forms.RotaryForm()
    return render(request, 'estacionamento/rotary/edit_rotary.html', {'form':form_rotary})

def update_rotary(request, id):
    rotary = get_object_or_404(models.Rotary, id=id)
    if request.method == 'POST':
        form_rotary = forms.RotaryForm(request.POST, instance=rotary)
        if form_rotary.is_valid():
            f_rotary = form_rotary.save(commit=False)
            f_rotary.save()
            return redirect('detail_rotary', id=f_rotary.id)
    else:
        form_rotary = forms.RotaryForm(instance=rotary)
    return render(request,'estacionamento/rotary/edit_rotary.html', {'form':form_rotary})

class delete_rotary(DeleteView):
    template_name = 'estacionamento/rotary/delete_rotary.html'
    model = models.Rotary
    context_object_name = 'rotary'
    success_url = reverse_lazy('list_rotary')
########### END-ROTARY ####################

########### VEHICLE ####################

def list_vehicle(request):
    vehicles=models.Vehicle.objects.all().order_by('id')
    return render(request, 'estacionamento/vehicle/list_vehicle.html', {'vehicles':vehicles})

def detail_vehicle(request, id):
    vehicle = get_object_or_404(models.Vehicle, id=id)
    return render(request, 'estacionamento/vehicle/detail_vehicle.html', {'vehicle':vehicle})

def new_vehicle(request):
    if request.method == 'POST':
        form_vehicle = forms.VehicleForm(request.POST)
        if form_vehicle.is_valid():
            vehicle = form_vehicle.save(commit=False)
            vehicle.save()
            return redirect('detail_vehicle', id=vehicle.id)
    else:
        form_vehicle = forms.VehicleForm()
    return render(request, 'estacionamento/vehicle/edit_vehicle.html', {'form':form_vehicle})

def update_vehicle(request, id):
    vehicle = get_object_or_404(models.Vehicle, id=id)
    if request.method == 'POST':
        form_vehicle = forms.VehicleForm(request.POST, instance=vehicle)
        if form_vehicle.is_valid():
            f_vehicle = form_vehicle.save(commit=False)
            f_vehicle.save()
            return redirect('detail_vehicle', id=f_vehicle.id)
    else:
        form_vehicle = forms.VehicleForm(instance=vehicle)
    return render(request,'estacionamento/vehicle/edit_vehicle.html', {'form':form_vehicle})

class delete_vehicle(DeleteView):
    template_name = "estacionamento/vehicle/delete_vehicle.html"
    model = models.Vehicle
    context_object_name = 'vehicle'
    success_url = reverse_lazy('list_vehicle')

########### END-VEHICLE ####################

########### MONTHLY ####################

def list_monthly(request):
    monthly = models.Monthly.objects.all().order_by('id')
    return render(request, 'estacionamento/monthly/list_monthly.html', {'monthly':monthly})

def detail_monthly(request, id):
    monthly = get_object_or_404(models.Monthly, id=id)
    return render(request, 'estacionamento/monthly/detail_monthly.html', {'monthly':monthly})

def new_monthly(request):
    if request.method == 'POST':
        form_monthly = forms.MonthlyForm(request.POST)
        if form_monthly.is_valid():
            monthly = form_monthly.save(commit=False)
            monthly.save()
            return redirect('detail_monthly', id=monthly.id)
    else:
        form_monthly = forms.MonthlyForm()
    return render(request, 'estacionamento/monthly/edit_monthly.html', {'form':form_monthly})

def update_monthly(request, id):
    monthly = get_object_or_404(models.Monthly, id=id)
    if request.method == 'POST':
        form_monthly = forms.MonthlyForm(request.POST, instance=monthly)
        if form_monthly.is_valid():
            f_monthly = form_monthly.save(commit=False)
            f_monthly.save()
            return redirect('detail_monthly', id=f_monthly.id)
    else:
        form_monthly = forms.MonthlyForm(instance=monthly)
    return render(request, 'estacionamento/monthly/edit_monthly.html', {'form':form_monthly})

class delete_monthly(DeleteView):
    template_name = 'estacionamento/monthly/delete_monthly.html'
    model = models.Monthly
    context_object_name = 'month'
    success_url = reverse_lazy('list_monthly')

########### END-MONTHLY ####################
