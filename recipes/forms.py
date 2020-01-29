from django import forms
from .models import Product


class Add_recipe_form(forms.ModelForm):
        
    class Meta:
        model = Product
        fields = (
            
            'uploaded_by','name', 'description', 'price', 'image',
            'recipe_category_name', 'cousine', 'preparation_time',
            'recipe_how_to_serve', 'preparation_method_1','preparation_method_2',
            'preparation_method_3','preparation_method_4','preparation_method_5','ingredient_1',
            'ingredient_2','ingredient_3','ingredient_4','ingredient_5',
            'ingredient_6','ingredient_7','ingredient_8','ingredient_9',
            'ingredient_10',
            
    )

    
    
