from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.shortcuts import render


def acceuil(request):
    return render(request,'don/acceuil.html')