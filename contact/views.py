from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']

            recipients = ['910806663@qq.com']

            send_mail(subject = name, message = message, from_email = email, recipient_list = recipients)
            return HttpResponseRedirect(reverse('contact:thanks'))
    else:
        form = ContactForm()
        return render(request, 'contact/contact.html', {'form': form})

def thanks(request):
    return render(request, 'contact/thanks.html')
