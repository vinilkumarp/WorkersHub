from django.contrib import admin
from django.conf.urls import url, include
from p1 import views

urlpatterns = [
    url(r'^$',views.login_redirect, name='login_redirect'),
    url(r'^admin/',admin.site.urls),
    url(r'^page1/', include('page1.urls')),
]  