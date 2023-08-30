from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AddItem

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register_item(request):
    form = AddItem()
    return render(request,'register_item.html',{'form':form})