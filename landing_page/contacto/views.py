from django.shortcuts import render
from .forms import FormularioContacto
# from s6r_odoo import OdooConnection
from .models import Mensajes

def contacto(request):
    if request.method == 'POST':
        form = FormularioContacto(request.POST)
        if form.is_valid():
            try:
                # aqui se guardan los datos en la bd
                mensaje = Mensajes.objects.create(
                    nombre = form.cleaned_data['name'],
                    email = form.cleaned_data['email'],
                    mensaje = form.cleaned_data['message'],
                )
                return render(request,'contacto/gracias.html')
            except Exception as e:
                return render(request,'contacto/error.html',{'error_message':str(e)})
        else: 
            return render(request,'contacto/contacto.html',{'form':form})
            # manejar errores
    else:
        form = FormularioContacto()
    return render(request,'contacto/contacto.html',{'form':form})

# def conexion_odoo(request):
#     odoo_cli = OdooConnection()
#     partners = odoo_cli.read_search('res.partner',[])
#     context = {'partners':partners}
#     return render(request, 'conexion_odoo.html',context)
