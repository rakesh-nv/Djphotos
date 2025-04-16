from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class TweetForm(forms.ModelForm):     
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        

class UserRegisterView(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = UserCreationForm.Meta.model
        fields = ('username', 'email', 'password1', 'password2')
        success_url = reverse_lazy('login')
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    # def clean_email(self):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
