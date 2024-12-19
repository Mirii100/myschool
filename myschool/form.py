from django import forms
from .models import Signup,Document,MyUserProfile
from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile,Testimonial

from django import forms
from django.contrib.auth.models import User
from .models import Signup,MySignup

class SignupForm(forms.ModelForm):
    # Add password and confirm_password fields for validation
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    
    class Meta:
        model = Signup  # Assuming Signup model is the one storing user data
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

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        
        return cleaned_data


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




class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'file']


class MyUserProfileForm(forms.ModelForm):
    class Meta:
        model = MyUserProfile
        fields = ['profile_picture', 'address', 'phone_number', 'date_of_birth', 'bio']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'bio': forms.Textarea(attrs={'rows': 4}),
        }

class MySignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = MySignup
        fields = ['title', 'name', 'email', 'phone_number', 'course_type',
                 'confirm_type', 'contact_hours', 'agree_terms']
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
   

