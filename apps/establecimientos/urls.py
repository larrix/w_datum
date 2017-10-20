from django.conf.urls import url
from . import views

app_name = 'establecimientos'

urlpatterns = [

    url(r'establecimientos/agregar/$', views.EstablecimientoCreate.as_view(), name='establemiento-agregar'),

    url(r'listar/$', views.IndexView.as_view(), name='listar'),

]
