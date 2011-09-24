from django.template.response import TemplateResponse
from django.core.mail import send_mail

def index(request):
    context = {}
    context['submitted'] = False

    if request.method == 'POST':
        subject = 'Pony From isaacbythewood.com'
        message = request.POST['message']
        sender = 'Robot <robot@bythewood.me>'
        recipient = ['isaac@bythewood.me']
        send_mail(subject, message, sender, recipient)
        context['submitted'] = True

    return TemplateResponse(request, 'core/index.html', context)

def bluescreen(request):
    return TemplateResponse(request, 'core/bluescreen.html')
