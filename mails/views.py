from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

# Create your views here.
def send_email(mail):
    content = {'mail': mail}
    template = get_template('mails/correo.html')
    content = template.render(content)
    
    email = EmailMultiAlternatives(
        'Un Correo de prueba',
        'Ejemplo de envio de correo desde django',
        settings.EMAIL_HOST_USER,
        [mail]
    )

    email.attach_alternative(content, 'text/html')
    email.send()

def index(request):
    if request.method == 'POST':
        print('Envio de Correo!!')
        
        mail = request.POST.get('mail')
        send_email(mail)

    return render(request, 'mails/index.html', {})