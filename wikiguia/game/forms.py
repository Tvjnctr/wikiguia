from django import forms
from .models import Game

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('name','description','description_short','release_date','is_visible','image','carousel_image',)
        widgets = {
            'name' : forms.TextInput(attrs={
                'class' : 'input_form_box'
            }),
            'description' : forms.Textarea(attrs={
                'class' : 'input_form_box'
            }),
            'description_short' : forms.Textarea(attrs={
                'class' : 'input_form_box'
            }),
            'release_date' : forms.DateInput(attrs={
                'class' : 'input_form_box'
            }),
            'is_visible' : forms.CheckboxInput(attrs={
                'class' : 'input_form_box'
            }),            
            'image' : forms.FileInput(attrs={
                'class' : 'input_form_box'
            }),
            'carousel_image' : forms.FileInput(attrs={
                'class' : 'input_form_box'
            }),            
        }
