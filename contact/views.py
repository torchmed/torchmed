from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import EmailForm

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

def email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():

            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']

            message = """
            Name: %s

            Message: %s

            """ % (form.cleaned_data['name'], form.cleaned_data['message'])

            try:
                send_mail(subject, message, from_email, ['raony@torchmed.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')        
    else:
        form = EmailForm()

    return render(request, "contact/email.html", {'form': form})

def thanks(request):
    return render(request, "contact/thanks.html")
