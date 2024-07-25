from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

#To add field in UserCreationForm
class RegisterUserForm(UserCreationForm):
    #widget are used to apply boostrap
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels =  {
            'username' : 'Kata Nama',
            'email' : 'Email', 
            'password1' : 'Kata Laluan' , 
            'password2' : 'Pengesahan Kata Laluan', 
        }

    #yang ni kita tambah sebab tiada pada field yang kita tambah.
    #yang ni object yang dah built in, jadi tinggal tambah widgetnya sahaja.
    def __init__(self, *args, **kwargs):
	    super(RegisterUserForm, self).__init__(*args, **kwargs)

	    self.fields['username'].widget.attrs['class'] = 'form-control'
	    self.fields['password1'].widget.attrs['class'] = 'form-control'
	    self.fields['password2'].widget.attrs['class'] = 'form-control'