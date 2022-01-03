from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',            
        }
    
    def __init__(self, *args, **kwards):
        super(CustomUserCreationForm, self). __init__()

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
