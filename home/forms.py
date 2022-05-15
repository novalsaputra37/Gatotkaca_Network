from django import forms
from .models import ContactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = "__all__"

        widgets = {
            'name' : forms.TextInput(
                attrs={
                    'id' : 'name',
                    'class' : 'form-control valid',
                    'placeholder' : 'Enter your name',
                    'name' : 'name',
                }
            ),
            'phone' : forms.TextInput(
                attrs={
                    'id' : 'phone',
                    'class' : 'form-control valid',
                    'placeholder' : 'Enter your phone',
                    'name' : 'phone',
                }
            ),
            'email' : forms.EmailInput(
                attrs={
                    'id' : 'email',
                    'class' : 'form-control valid',
                    'placeholder' : 'Enter your email',
                    'name' : 'email',
                }
            ),
            'subject' : forms.TextInput(
                attrs={
                    'id' : 'subject',
                    'class' : 'form-control valid',
                    'placeholder' : 'Enter your subject',
                    'name' : 'subject',
                }
            ),
            'message' : forms.Textarea(
                attrs={
                    'id' : 'message',
                    'class' : 'form-control valid',
                    'placeholder' : 'Enter your message',
                    'name' : 'message',
                }
            ),
        }