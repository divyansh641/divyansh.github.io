from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from personal.models import contactForm

urlpatterns=[
 url(r'^$', views.index, name='index'),
 url('^$', ListView.as_view(queryset=contactForm.objects.all().order_by("name"), template_name="personal/index.html")),
 url('^(?P<pk>\d+)$', DetailView.as_view(model=contactForm, template_name='personal/index.html'))]