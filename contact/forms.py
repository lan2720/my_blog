from django import forms 

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 30, label = 'Name') 
    email = forms.EmailField(label = 'Message') 
    message = forms.CharField(widget=forms.Textarea, label = 'Email Address') 
    
