from django.contrib import admin
from django.conf.urls import include, url
from django.contrib.auth.views import login



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^establecimientos/', include('apps.establecimientos.urls', namespace='establecimientos')),
    url(r'^$', login, {'template_name': 'establecimientos/index.html'}, name='login'),
]
