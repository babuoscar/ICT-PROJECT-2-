from django import forms 
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model=Message
        fields=['name','email','tel','message']
        labels={'name':'Name','email':'Email','tel':'Phone number','message':'Message'}
