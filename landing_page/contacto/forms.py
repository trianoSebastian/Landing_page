from django import forms 

class FormularioContacto(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

    def __str__(self):
        return f'Mensaje de: {self.email}'