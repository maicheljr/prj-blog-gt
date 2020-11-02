from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import EmailMessage, send_mail
from django.conf import settings



# def email(request):
#     subject = 'Thank you for registering to our site'
#     message = ' it  means a world to us '
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = ['receiver@gmail.com',]
#     send_mail( subject, message, email_from, recipient_list )
#     return redirect('redirect to a new page')

def contact(request):
    send = False
    template_name = 'contact/contact.html'

    send = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        #enviar email
        nome = request.POST.get('nome','')
        email = request.POST.get('email','')
        message = request.POST.get('mensagem','')

        email = EmailMessage(
            "BLog-GT",
            "De {} <{}> Escreveu: \n \n {}".format(nome,email,message),
            "não-responder@inbox.mailtrap.io",
            ["maicheljr@gmail.com"],
            reply_to=[email]
        )
        try:
            email.send()
            send = True
        except:
            send = False

    context = {
        'form':form,
        'success':send
    }

    return render(request,template_name=template_name,context=context)



