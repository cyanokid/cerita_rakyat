from django import forms
from django.forms import ModelForm
from .models import Story, Profile
from django.contrib.auth.models import User

class StoryForm(ModelForm):
    class Meta:
        model = Story
        fields = ('username', 'email', 'title', 'content')
        labels =  {
            'username' : 'Penulis',
            'email' : 'Email Anda *Tidak akan ditunjukkan pada paparan', 
            'title' : 'Tajuk' , 
            'content' : 'Cerita Anda', 
        }

        #to put css boostrap
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}), 
            'title' : forms.TextInput(attrs={'class':'form-control'}), 
            'content' : forms.Textarea(attrs={'class':'form-control'}), 
        }

class StoryFormUser(ModelForm):
    class Meta:
        model = Story
        fields = ('title', 'content')
        labels =  {
            'title' : 'Tajuk' , 
            'content' : 'Cerita Anda', 
        }

        #to put css boostrap
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}), 
            'content' : forms.Textarea(attrs={'class':'form-control'}), 
        }

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_bio', 'profile_image',) # add , to make a tuple
        labels =  {
            'profile_bio' : 'Bio Profil:',
            'profile_image' : 'Imej Profil:',
        }
  
        #to put css boostrap
        widgets = {
            'profile_bio' : forms.TextInput(attrs={'class':'form-control'}),
            
        }

class UpdateUserForm(ModelForm):
    #widget are used to apply boostrap
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'email')
        labels =  {
            'username' : 'Kata Nama',
            'email' : 'Email', 
        }

    #yang ni kita tambah sebab tiada pada field yang kita tambah.
    #yang ni object yang dah built in, jadi tinggal tambah widgetnya sahaja.
    def __init__(self, *args, **kwargs):
	    super(UpdateUserForm, self).__init__(*args, **kwargs)

	    self.fields['username'].widget.attrs['class'] = 'form-control'