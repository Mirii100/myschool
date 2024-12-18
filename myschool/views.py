from django.shortcuts import render,redirect
from . models import Signup,UserProfile,Testimonial,courses
from .form import SignupForm,UserProfileForm,LoginForm,TestimonialForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.


from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logging out


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def index(request):
    testimonials = Testimonial.objects.all()
    form = Signup.COURSE_CHOICES
    return render(request, 'index.html',{'testimonials':testimonials,'form':form})


def instructors(request):
    return render(request,"instructors.html")

def student(request):
    return render(request,"index.html")

#for enloring to a course 
def join(request):
    return render(request,"base.html")


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        form1 = UserProfileForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            return redirect('homepage')  # Redirect to another page after saving
    else:
        form = SignupForm()
        form1 = UserProfileForm()
    
    
    
    
    return render(request, 'signup.html', {'form': form,'form1': form1})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Check if user agrees to the terms
            if not form.cleaned_data['agree_to_terms']:
                form.add_error('agree_to_terms', 'You must agree to the terms and conditions')
                return render(request, 'login.html', {'form': form})

            # Authenticate the user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)  # Log the user in
                return redirect('homepage')  # Redirect to the homepage after successful login
            else:
                form.add_error(None, 'Invalid username or password')  # Add error for invalid credentials
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
    
# for courses
def testmonies(request):
    testimonials = Testimonial.objects.filter(status=True)  # Display only active testimonials
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the new testimonial to the database
            return redirect('ctestmonials')  # Redirect to the testimonial page
    else:
        form = TestimonialForm()

    return render(request, 'testimonial.html', {'form': form, 'testimonials': testimonials})
    

def about(request):
    return render(request,"about.html")
def course(request):
    form = courses.COURSE_CHOICES
    return render(request,"ourcourses.html",{'form':form})
def contact(request):
    return render(request,"contact.html")

from django.shortcuts import render, redirect
from .models import Testimonial
from django.contrib.auth.decorators import login_required

@login_required
def create_testimonial(request):
    testimonials = Testimonial.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        profession = request.POST.get("profession")
        message = request.POST.get("message")
        image = request.FILES.get("image")

        # Create the testimonial with the logged-in user
        Testimonial.objects.create(
            user=request.user,  # Ensures the user is set
            name=name,
            profession=profession,
            message=message,
            image=image
        )
        

        

        return redirect("success_page")

    return render(request, "testimonial.html",{"testimonials": testimonials})

