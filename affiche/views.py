from django.shortcuts import render,redirect

# Create your views here.

def information(request):
    return render(request,'affiche/information.html')
    

def pourquoi(request):
    return render(request,'affiche/pourquoi.html')

def test(request):
    if request.method == 'POST':
        return redirect('affiche:reussite')
    return render(request,'affiche/test.html')

def site(request):
    return render(request,'affiche/site.html')

def reussite(request):
    return render(request,'affiche/reussite.html')