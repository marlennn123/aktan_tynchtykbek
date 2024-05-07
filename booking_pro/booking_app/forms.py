from allauth.account.forms import SignupForm
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import *
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class CustomSignupForm(SignupForm):
    phone_number = PhoneNumberField(label='Phone Number', widget=PhoneNumberPrefixWidget(initial='KG'))

    def save(self, request):

        user = super(CustomSignupForm, self).save(request)
        number = self.cleaned_data['phone_number']
        user.phone_number = self.cleaned_data['phone_number']
        print(type(number), user.phone_number)
        user.save()
        return user
