from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='estacionamento_home'),#name=estacionamento_home

    ############# PEOPLE ##############

    path('pessoas/', views.list_peoples, name='list_people'),#name=list_peoples
    path('pessoas/new/', views.new_people, name='new_people'),
    path('pessoas/<int:id>/', views.detail_people, name='detail_people'),
    path('pessoas/<int:id>/edit/', views.update_people, name='update_people'),
    path('pessoas/<int:id>/delete/', views.delete_people, name='delete_people'),


    ########### END-PEOPLE ############

    ############# ROTARY ##############

    path('rotativos', views.list_rotary, name='list_rotary'),
    path('rotativos/new/', views.new_rotary, name='new_rotary'),
    path('rotativos/<int:id>/', views.detail_rotary, name='detail_rotary'),
    path('rotativos/<int:id>/edit/', views.update_rotary, name='update_rotary'),
    path('rotativos/<pk>/delete/', views.delete_rotary.as_view(), name='delete_rotary'),

    ############# END-ROTARY ##############

    ############# VEHICLE ##############

    path('veiculos', views.list_vehicle, name='list_vehicle'),
    path('veiculos/new/', views.new_vehicle, name='new_vehicle'),
    path('veiculos/<int:id>/', views.detail_vehicle, name='detail_vehicle'),
    path('veiculos/<int:id>/edit/', views.update_vehicle, name='update_vehicle'),
    path('veiculos/<pk>/delete/', views.delete_vehicle.as_view(), name='delete_vehicle'),

    ############# END-VEHICLE ##############

    ############# MONTHLY ##############

    path('mensalistas', views.list_monthly, name='list_monthly'),
    path('mensalistas/new/', views.new_monthly, name='new_monthly'),
    path('mensalistas/<int:id>/', views.detail_monthly, name='detail_monthly'),
    path('mensalistas/<int:id>/edit/', views.update_monthly, name='update_monthly'),
    path('mensalistas/<pk>/delete/', views.delete_monthly.as_view(), name='delete_monthly'),

    ############# END-MONTHLY ##############
]
