from django import forms
from .models import Game

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('name','description','description_short','data_lore','data_weapons','data_achievements','data_playtime','data_easter_eggs',
                  'data_enemies','release_date','is_visible','image','carousel_image',)
        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
            'description_short': 'Descripción breve',
            'data_lore': 'Info. del Juego - Historia',
            'data_weapons': 'Info. del Juego - Armas',
            'data_achievements': 'Info. del Juego - Logros',
            'data_playtime': 'Info. del Juego - Duración',
            'data_easter_eggs': 'Info. del Juego - Ocultos',
            'data_enemies': 'Info. del Juego - Enemigos',
            'release_date': 'Fecha de Lanzamiento',
            'is_visible': 'Publicar al crear',
            'image': 'Imagen',
            'carousel_image': 'Imagen para Carousel (opcional)',
        }
        widgets = {
            'name' : forms.TextInput(attrs={
                'placeholder' : 'Ingresa el nombre del juego',
                'class' : 'input_form_box',
                'rows': 1,  
                'cols': 40
            }),
            'description' : forms.Textarea(attrs={
                'placeholder' : 'Descripción del juego',
                'class' : 'input_form_box',
                'rows': 1,  
                'cols': 40 
            }),
            'description_short' : forms.Textarea(attrs={
                'placeholder' : 'Maximo 2 lineas',
                'class' : 'input_form_box',
                'rows': 1,  
                'cols': 40  
            }),
            'data_lore' : forms.Textarea(attrs={
                'placeholder' : 'Resumen de la historia',
                'class' : 'input_form_box',
                'rows': 1,  
                'cols': 40  
            }),
            'data_weapons' : forms.Textarea(attrs={
                'placeholder' : 'Datos - Armas del juego',
                'class' : 'input_form_box',
                'rows': 1,  
                'cols': 40  
            }),
            'data_achievements' : forms.Textarea(attrs={
                'placeholder' : 'Datos - Logros del juego',
                'class' : 'input_form_box',
                'rows': 1,  
                'cols': 40  
            }),
            'data_playtime' : forms.Textarea(attrs={
                'placeholder' : 'Datos - Duración del juego',
                'class' : 'input_form_box',
                'rows': 1,  
                'cols': 40  
            }),
            'data_easter_eggs' : forms.Textarea(attrs={
                'placeholder' : 'Datos - Ocultos del juego',
                'class' : 'input_form_box',
            }),
            'data_enemies' : forms.Textarea(attrs={
                'placeholder' : 'Datos - Enemigos del juego',
                'class' : 'input_form_box',
            }),
            'release_date' : forms.DateInput(format='%Y-%m-%d', attrs={
                'class' : 'input_form_box',
                'type': 'date'
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