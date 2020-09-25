from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    # este print te muestra el tipo de metodo de envio de datos que usa la pagina
    # print("Tipo de petición: {}".format(request.method))

    contac_Form = ContactForm()
    if request.method == 'POST':
        contac_Form = ContactForm(data=request.POST)
        if contac_Form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Enviamos el correo y redireccionamos

            email = EmailMessage(
                "La Caffetiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n {}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["jaferrer10@hotmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                #Todo ha salido bien, redireccionemos a ok
                return redirect(reverse('contact') + '?ok')

            except:
                #Algo ha salido mal, redireccionemos a fail
                  return redirect(reverse('contact') + '?fail')

    return render(request, "contact/contact.html", {'form': contac_Form})
