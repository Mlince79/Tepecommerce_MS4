from django import forms
from .models import Contact

class ContactForm(forms.Form):

    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject'
                  'message')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Full Name',
            'email': 'Email Address',
            'subject': 'Subject',
            'message': 'Message',
        }

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'