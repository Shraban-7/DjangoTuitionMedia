from django.shortcuts import render

from .contactForms import ContactForm
from .models import Contact
from django.views.generic import CreateView
# Create your views here.

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact/contact.html'