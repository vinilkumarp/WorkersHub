from django.conf.urls import url,include
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView , LogoutView

urlpatterns=[
    url(r'^$',views.home),
    url(r'^login/$',  LoginView.as_view(template_name='page1/login.html'), name="login"),
    url(r'^logout/$', LogoutView.as_view(template_name='page1/logout.html'), name="logout"),
    url(r'^register/$',views.register, name='register'),
    url(r'^profile/$',views.view_profile,name='view_profile'),
    url(r'^profile/edit/$',views.edit_profile,name='edit_profile'),
    url(r'^change-password/$',views.change_password, name='change-password'),
    url(r'^workers-register/$',views.Workers_registration,name='Workers_registration'),
    url(r'^appointment/$',views.appointment,name='appointment'),
    path('filter/<int:id>/',views.send_conf,name='send_conf'),
    ]
