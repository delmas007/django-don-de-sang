from cProfile import label
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms

from base.models import Membre,Hopital,Commune

class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'type':"email",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"name@example.com",
        })
        self.fields['nom'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"nom",
        })
        self.fields['prenom'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"prenom",
        })
        self.fields['password1'].widget.attrs.update({
            'type':"Password",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingPassword",
            'placeholder':"Password",
        })
        self.fields['password2'].widget.attrs.update({
            'type':"Password",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingPassword",
            'placeholder':"Confirme Password",
        })
        self.fields['contact'].widget.attrs.update({
            'type':"tel",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingPassword",
            'placeholder':"0779562248",
            'pattern':"[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}"
        })
        self.fields['permanent'].widget.attrs.update({
            'type':"checkbox",
            'class':"form-check-input",
            'name':"newsletter",
            'id':"newsletter",
            #'value':"False"
        })
        self.fields['groupe'].widget.attrs.update({
            'name':"country",
            'class':"form-select text-danger",
            'id':"country",
            #'value':"False"
        })
        self.fields['commune'].widget.attrs.update({
            'name':"country",
            'class':"form-select text-danger",
            'id':"country",
            #'value':"False"
        })
        

    class Meta:
        model = Membre
        fields = ('email','nom','prenom','contact','commune','groupe','permanent')
        
class ConnexionForm(AuthenticationForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'type':"email",
            'class':"form-control ",
            'style':"color: black;",
            'id':"floatingInput",
            'placeholder':"name@example.com",
        })
        self.fields['password'].widget.attrs.update({
            'type':"Password",
            'class':"form-control ",
            'style':"color: black;",
            'id':"floatingPassword",
            'placeholder':"Password",
        })
        
class HopitalForm(forms.ModelForm):
    
    class Meta:
        model = Hopital
        fields = ['Aplus','Amoins','Bplus','Bmoins','Oplus','Omoins','ABplus','ABmoins']
        labels = {'Aplus':'A+','Amoins':'A-','Bplus':'B+','Bmoins':'B-','Oplus':'O+','Omoins':'O-','ABplus':'AB+','ABmoins':'AB-'}
        widgets = {
            'Aplus': forms.CheckboxInput(attrs={"name":"newsletter", "id":"newsletter","class":"form-check-input position-absolute top-0 end-50"}),
            'Amoins': forms.CheckboxInput(attrs={"name":"newsletter", "id":"newsletter","class":"form-check-input position-absolute top-0 end-50"}),
            'Bplus': forms.CheckboxInput(attrs={"name":"newsletter", "id":"newsletter","class":"form-check-input position-absolute top-0 end-50"}),
            'Bmoins': forms.CheckboxInput(attrs={"name":"newsletter", "id":"newsletter","class":"form-check-input position-absolute top-0 end-50"}),
            'Oplus': forms.CheckboxInput(attrs={"name":"newsletter", "id":"newsletter","class":"form-check-input position-absolute top-0 end-50"}),
            'Omoins': forms.CheckboxInput(attrs={"name":"newsletter", "id":"newsletter","class":"form-check-input position-absolute top-0 end-50"}),
            'ABplus': forms.CheckboxInput(attrs={"name":"newsletter", "id":"newsletter","class":"form-check-input position-absolute top-0 end-50"}),
            'ABmoins': forms.CheckboxInput(attrs={"name":"newsletter", "id":"newsletter","class":"form-check-input position-absolute top-0 end-50"}),
        }
