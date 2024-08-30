from django.forms import ModelForm

from django import forms
from .models import Product, Stock, StockMovement, Unit, Vendor 
from django.contrib.auth.models import User


class UnitForm(ModelForm):
          class Meta:
                  model=Unit
                  fields='__all__'

class StockMovementForm(ModelForm):
     class Meta:
          model=StockMovement
          fields='__all__'

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'unit', 'price', 'opening_stock', 'description', 'status']




class UserForm(forms.ModelForm):
    status = forms.BooleanField(required=False, label="Active")
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Hash the password before saving
        user.is_active = self.cleaned_data["status"]
        if commit:
            user.save()
        return user