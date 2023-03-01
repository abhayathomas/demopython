from tkinter import Place

from django.shortcuts import render
from .models import Place, Team


def demo(request):
    obj1=Place.objects.all()
    obj2=Team.objects.all()
    return render(request,"index.html",{'result1':obj1,'result2':obj2})
