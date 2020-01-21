from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput({'class':'form-control','placeholder':"¿Cómo te llamas?", 'min_lenght':3, 'max_lenght':100}))
    email = forms.EmailField(label="Correo", required=True, widget=forms.EmailInput({'class':'form-control','placeholder':'Escribe tu correo electrónico', 'min_lenght':3, 'max_lenght':100}))
    content = forms.CharField(label="Mensaje", required=True, widget=forms.Textarea({'class':'form-control','rows':3,'placeholder':'¿Qué nos quieres decir?', 'min_lenght':10, 'max_lenght':1000}))
