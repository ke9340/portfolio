from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2 or len(name) > 30:
            raise forms.ValidationError("Name should be between 2 and 30 characters.")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if "@" not in email or "." not in email:
            raise forms.ValidationError("Enter a valid email address.")
        return email
