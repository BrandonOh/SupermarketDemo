from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Item

class AddItem(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Item Name'}),label="")
    inv = forms.ImageField(required=True, widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'0'}),label="")
    sale = forms.DecimalField(required=True, widget=forms.NumberInput(attrs={'class':'form-control','max':'1.00','step':'.01', 'placeholder':'0.00'}),label="")
    desc = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Description'}),label="")
    price = forms.DecimalField(required=True, widget=forms.NumberInput(attrs={'class':'form-control','step':'.01', 'placeholder':'0.00'}),label="")
    food_type = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Item Type'}),label="")
    food_image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class':'form-control'}),label="")

    class Meta:
        model = Item
        exclude = ("user",)