from django.conf.urls import url
from . import views

app_name = 'establecimientos'

urlpatterns = [
    # /establecimientos/
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'establecimientos/agregar/$', views.EstablecimientoCreate.as_view(), name='establemiento-agregar'),

]
