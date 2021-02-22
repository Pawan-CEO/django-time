from django.conf.urls import url
from Manage import views

urlpatterns=[
    url('projects',views.projects),
    url('team',views.team),
    url('clients',views.clients),
    url('tags',views.tags),
    url('settings',views.settings),
]