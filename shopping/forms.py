from django import forms
from shopping.models import Category,Product

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude=('vcnt','lcnt' ,'created_at','updated_at')
