from itertools import count
from django.shortcuts import render,redirect
from base.forms import UserRegistrationForm,ConnexionForm,HopitalForm
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from don import settings
from base.models import Hopital,Commune,Membre
from django.views.generic import UpdateView,DetailView
from django.shortcuts import resolve_url
from django.views.decorators.csrf import csrf_protect
# Create your views here.

@csrf_protect
def inscription(request):
    context = {}
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base:connexion')
        else:
            context['errors'] = form.errors
    
    form = UserRegistrationForm()
    context['form']=form
    return render(request,'base/inscription.html',context=context)

# @csrf_protect
class Connexion(LoginView):
    template_name = 'base/connection.html'
    form_class = ConnexionForm
    
    def get_success_url(self) -> str:
        b = super().get_success_url()
        if self.request.user.admins == True:
            return reverse('base:bienvenue')
        elif self.request.user.admins == False:
            return b

@login_required       
def bienvenue(request):
    return render(request,('base/bienvenue.html'))
    
    
# @csrf_protect   
class Deconnexion(LogoutView):
    pass

@login_required   
def HopitalR(request):
    if request.method == 'POST':
        sang = int(request.POST['no'])
        hop = Hopital.objects.all()
        for i in hop :
            if i.id == sang:
                hope = i
                return render(request,'base/hopital.html',{'hop':hop,"sang":sang,'hope':hope})
        return render(request,'base/hopital.html',{'hop':hop,"sang":sang})
    
    hop = Hopital.objects.all()
    return render(request,'base/hopital.html',{'hop':hop})  

@login_required
def Demande(request):
    if request.method == 'POST':
        commune = Commune.objects.all()
        memb = Membre.objects.all()
        com = request.POST['commune']
        grou = request.POST['groupe']
        tab =[]
        for i in memb:
            if str(i.commune) == com and str(i.groupe) == grou and i.permanent == True:
                tab.append(i)
        if tab:
            return render(request,'base/demande.html',{'commune':commune,'c':tab})
        else:
            b= True
            return render(request,'base/demande.html',{'commune':commune,'b':b})
         
    commune = Commune.objects.all()
    return render(request,'base/demande.html',{'commune':commune})

# @csrf_protect
class Administrateur(LoginRequiredMixin,UpdateView):
    model = Hopital
    template_name = 'base/admin.html'
    form_class = HopitalForm
    success_url = reverse_lazy('base:bienvenue')
    
    
    
