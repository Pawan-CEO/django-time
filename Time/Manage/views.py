from django.shortcuts import render
from Manage.models import Manage
def projects(r):
    res=render(r,'Manage/projects.html')
    return res
def team(rr):
    res=render(rr,'Manage/team.html')
    return res
def clients(rrr):
    manage=Manage.objects.all()
    data={'manage':manage}
    res=render(rrr,'Manage/clients.html',data)
    return res
def tags(rrrr):
    res=render(rrrr,'Manage/tags.html')
    return res
def settings(rrrrr):
    res=render(rrrrr,'Manage/settings.html')
    return res
