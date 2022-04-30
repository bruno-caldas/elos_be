# -*- coding: utf-8 -*-
from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
    nome = forms.CharField(label='Your name', max_length=100, help_text="Help text here")
    porte = forms.CharField(label='Your name', max_length=1, help_text="Help text here")
    idade = forms.IntegerField(label='Your name',help_text="Help text here")
