from django.forms import ModelForm

from content.models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
