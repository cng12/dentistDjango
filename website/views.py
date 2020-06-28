from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html', {})


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            message_name,
            message,
            message_email,
            [''],
        )

        return render(request, 'contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})


def applying(request):
    return render(request, 'applying.html', {})


def community(request):
    return render(request, 'community.html', {})


def jobs(request):
    return render(request, 'jobs.html', {})


def appointment(request):
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_date = request.POST['your-date']
        your_message = request.POST['your-message']

        return render(request, 'appointment.html', {
            'your_schedule': your_schedule,
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_address': your_address,
            'your_date': your_date,
            'your_message': your_message,

        }
                      )
    else:
        return render(request, 'home.html', {})



