from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Contacts
from django.contrib import messages
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request have been submitted successfully')
            return redirect('contact')
        else:
            messages.error(request, 'There was a problem submitting your message.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'pages/contact.html', {'form':form})
