
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from pycep_correios import WebService, get_address_from_cep


class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=500)
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2',]

    def clean_nome(self):
        pessoa = self.cleaned_data['usarname']
        if User.objects.filter(usarname=pessoa).exists():
            raise ValidationError("Nome de usuário {} já está em uso.".format(pessoa))
        return pessoa

    def clean_email(self):
        e = self.cleaned_data['email']
        if User.objects.filter(email=e).exists():
            raise ValidationError("O email {} já está em uso.".format(e))
        return e

