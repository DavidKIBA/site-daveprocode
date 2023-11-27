from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

# Create your views here.

def contact_page(request):
    message = ""
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            message = messages.success(request, 'votre message a été envyer avec succes nous allons vous répondre pas mail dans maximum 2 jours')
            return redirect('contact')
     
    context ={'contact_form': contact_form, 'message': message}
    return render(request, 'other_page/contact.html', context)
