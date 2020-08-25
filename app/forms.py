from django import forms

class SampleForm(forms.Form):
    name=forms.CharField(max_length=200,required=True,label="Name :")
    email=forms.EmailField(max_length=100,required=True,label="Email :")
    pwd=forms.CharField(max_length=200,required=True,label="Password :",widget=forms.PasswordInput(attrs={'placeholder':"Password"}))
    profile_pic=forms.ImageField(max_length=200,required=True,label="Profile Pic :")
