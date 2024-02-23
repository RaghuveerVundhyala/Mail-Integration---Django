from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail


def sendmail(request):
    if request.method == "POST" and 'Approved' in request.POST:
        subject = 'Leave Status'
        message = f'Hi Raghu, your leave has approved'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['reciever mail', ]
        send_mail(subject, message, email_from, recipient_list)
        return HttpResponse("Email sent successfully.")
    elif request.method == "POST" and 'Rejected' in request.POST:

        subject = 'Leave Status'
        message = f'Hi Raghu, your leave has rejected'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['reciever mail', ]
        send_mail(subject, message, email_from, recipient_list)
        print('rejected')

    return render(request, 'send_email.html')

