from django import forms
from .models import Signup
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile,Testimonial,MyUser
from django.contrib.auth.models import User
class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ['title', 'name', 'email', 'phone_number', 'course_type', 
                  'confirm_type', 'contact_hours', 'agree_terms']
        labels = {
            'title': 'Title',
            'name': 'Your Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'course_type': 'Course Type',
            'confirm_type': 'Confirmation Type',
            'contact_hours': 'Preferred Contact Hours',
            'agree_terms': 'I agree to the terms and conditions'
        }



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile  # Your model here
        fields = ['title', 'name', 'email', 'phone_number', 'course_type', 'confirm_type', 'contact_hours', 'agree_terms']

        labels = {
            'title': 'Title',
            'name': 'Your Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
                'course_type': 'Course Type',
                'confirm_type': 'Confirmation Type',
                'contact_hours': 'Preferred Contact Hours',
                'agree_terms': 'I agree to the terms and conditions'}
        agree_to_terms = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'terms-checkbox'}),
        label="I agree to the terms and condition "
    )
        

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    agree_to_terms = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'terms-checkbox'}),
        label="I agree to the terms' "
    )


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'profession', 'message', 'image']

    # You can add validation or custom widgets if needed
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    profession = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your Profession'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Testimonial'}))
    image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}))



class MySignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

class MyUserProfileForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['phone_number', 'course_type', 'confirm_type', 'contact_hours','profile_image', 'agree_terms']



class MyLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'form-control'
        }), 
        label="Username"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control'
        }), 
        label="Password"
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        if username and password:
            self.user_cache = authenticate(
                username=username,
                password=password
            )
            if self.user_cache is None:
                raise forms.ValidationError(
                    "Please enter a correct username and password."
                )
        return self.cleaned_data


class ContactForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['contact']



