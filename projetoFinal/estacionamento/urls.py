from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='estacionamento_home'),#name=estacionamento_home

    ############# PEOPLE ##############

    path('pessoas/', views.list_peoples, name='list_people'),#name=list_peoples
    path('pessoas/new/', views.new_people, name='new_people'),
    path('pessoas/<int:id>/', views.detail_people, name='detail_people'),
    path('pessoas/<int:id>/edit/', views.update_people, name='update_people'),
    path('pessoas/<int:id>/delete/', views.delete_people, name='delete_people'),
    path('relatorio/<str:model>/', views.Pdf.as_view(), name='relatorio_people'),

    ########### END-PEOPLE ############

    ############# ROTARY ##############

    path('rotativos/', views.ListRotary.as_view(), name='list_rotary'),
    path('rotativos/new/', views.CreateRotary.as_view(), name='new_rotary'),
    path('rotativos/<pk>/', views.DetailRotary.as_view(), name='detail_rotary'),
    path('rotativos/<pk>/edit/', views.UpdateRotary.as_view(), name='update_rotary'),
    path('rotativos/<pk>/delete/', views.DeleteRotary.as_view(), name='delete_rotary'),

    ############# END-ROTARY ##############

    ############# VEHICLE ##############

    path('veiculos/', views.list_vehicle, name='list_vehicle'),
    path('veiculos/new/', views.create_vehicle, name='create_vehicle'),
    path('veiculos/<int:id>/', views.detail_vehicle, name='detail_vehicle'),
    path('veiculos/<int:id>/edit/', views.update_vehicle, name='update_vehicle'),
    path('veiculos/<pk>/delete/', views.DeleteVehicle.as_view(), name='delete_vehicle'),

    ############# END-VEHICLE ##############

    ############# MONTHLY ##############

    path('mensalistas/', views.ListMonthly.as_view(), name='list_monthly'),
    path('mensalistas/new/', views.CreateMonthly.as_view(), name='new_monthly'),
    path('mensalistas/<pk>/', views.DetailMonthly.as_view(), name='detail_monthly'),
    path('mensalistas/<pk>/edit/', views.UpdateMonthly.as_view(), name='update_monthly'),
    path('mensalistas/<pk>/delete/', views.DeleteMonthly.as_view(), name='delete_monthly'),

    ############# END-MONTHLY ##############
]
