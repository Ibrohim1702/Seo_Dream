from django.shortcuts import render

from sayt.models import Contact


# Create your views here.


def index(requests):
    ctx = {}
    if requests.POST:
        name = requests.POST.get('name')
        surname = requests.POST.get('surname')
        subject = requests.POST.get('subject')
        message = requests.POST.get('message')
        email = requests.POST.get('email')
        Contact.objects.create(
            name=name, message=message, surname=surname, email=email, subject=subject
        )

        ctx = {
            "contact": index,
        }
    return render(requests, "index.html", ctx)