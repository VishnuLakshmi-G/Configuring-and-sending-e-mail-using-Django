from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render

# Home page view
def home(request):
    return render(request, 'home.html')

# Send email view
def send_email(request):
    if request.method == 'POST':
        subject = 'Welcome Party - reg.'
        message = 'Greetings!!! Welcome to the Department of Information Technology.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['vishnulakshmig2004@gmail.com']  # Receiver email

        # Sending email
        send_mail(subject, message, email_from, recipient_list, fail_silently=False)

        return render(request, 'sendMail.html', {'success': True})

    return render(request, 'sendMail.html')
