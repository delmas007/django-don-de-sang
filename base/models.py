import textwrap
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.template.defaultfilters import slugify

groupee =(
    'Abobo',
    'Adjamé',
    'Anyama',
    'Attécoubé',
    'Bingerville',
    'Cocody',
    'Koumassi',
    'Marcory',
    'Plateau',
    'Port bouët',
    'Treichville',
    'Yopougon',
)

sang = (
    ('O+','O+'),
    ("O-","O-"),
    ("A+","A+"),
    ("A-","A-"),
    ("B+","B+"),
    ("B-","B-"),
    ('AB+','AB+'),
    ('AB-','AB-'),
)
# Create your models here.
class Commune(models.Model):
    nom = models.CharField(max_length=250)
    class Meta:
        verbose_name = 'commune'

    def __str__(self):
        return self.nom
    
class MyUserManager(BaseUserManager):
    def create_user(self, email,password=None):
        if not email:
            raise ValueError("Vous devez entrer un mail")
        
        user = self.model(
            email = self.normalize_email(email)
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email,password=None):
        user = self.create_user(email=email,password=password)
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user

class Hopital(models.Model):
    nom = models.CharField(max_length=250)
    commune = models.ForeignKey(Commune,on_delete=models.SET_NULL,null=True)
    image = models.ImageField(blank=True,null=True, upload_to='hopital')
    slug = models.SlugField(max_length=255,blank=True)
    Aplus = models.BooleanField(default=False)
    Amoins = models.BooleanField(default=False)
    Bplus = models.BooleanField(default=False)
    Bmoins = models.BooleanField(default=False)
    Oplus = models.BooleanField(default=False)
    Omoins = models.BooleanField(default=False)
    ABplus = models.BooleanField(default=False)
    ABmoins = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nom
    # ,self.commune,self.id
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom)
        super().save(*args, **kwargs)
    
class Membre(AbstractBaseUser):
    nom = models.CharField(max_length=250,verbose_name='nom')
    prenom = models.CharField(max_length=250)
    email = models.EmailField(
        unique=True,
        max_length=255,
        blank=False
    )
    contact = models.CharField(blank=False,max_length=250)
    commune = models.ForeignKey(Commune,on_delete=models.SET_NULL,null=True,blank=True)
    hopital = models.OneToOneField(Hopital,on_delete= models.SET_NULL, null=True)
    groupe = models.CharField(blank=False,max_length=3,choices=sang)
    permanent = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    admins = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    # definir un ou des champs oblogatoires
    # REQUIRED_FIELDS = ['age']
    objects = MyUserManager()
    
    def has_perm(self,perm ,obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    class Meta:
        verbose_name = 'membre'

    def __str__(self):
        return self.nom,self.commune,self.groupe,self.permanent
    

    
class SiteDeDon(models.Model):
    nom = models.CharField(max_length=250)
    commune = models.ForeignKey(Commune,on_delete=models.SET_NULL,null=True)
    coordonnee = models.CharField(max_length=1000)
    image = models.ImageField(blank=True,null=True, upload_to='site',)
    
    class Meta:
        verbose_name = 'site'

    def __str__(self):
        return self.nom
    
