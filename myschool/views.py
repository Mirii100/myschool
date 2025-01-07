from django.shortcuts import render,redirect
from . models import Signup,UserProfile,Testimonial,courses,CoursesCategory,Book,Project,Instructor,Unit
from .form import SignupForm,UserProfileForm,LoginForm,TestimonialForm,MySignupForm, MyUserProfileForm,MyLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User

from django.contrib import messages  # Import messages framework
from django.contrib.auth import authenticate, login
from django.contrib import messages


from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


from django.contrib.auth import logout


from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect


def logout_view(request):
    # Get username before logout to use in message
    username = request.user.username
    # Perform logout
    logout(request)
    # Add success message
    messages.success(request, f"Goodbye {username}! You have been successfully logged out.")
    # Redirect to login page
    return redirect('mylogin')

def index(request):
    testimonials = Testimonial.objects.all()
    testimonial = Testimonial.objects.filter(status=True)
    form = courses.COURSE_CHOICES
    return render(request, 'index.html',{'testimonials':testimonials,'form':form,'testimonial':testimonial})


def instructors(request):
    OurInstructor=Instructor.objects.all()
    context={'Ourinstructors':OurInstructor}

    return render(request,"instructors.html",context)

def student(request):
    sign=Signup.objects.all()
    return render(request,"index.html",{"sign":sign})

#for enloring to a course 
def join(request):
    testimonials = Testimonial.objects.filter(status=True) 
    testmony=Testimonial.objects.all()
    sign=Signup.objects.all()
    context={'testimonials':testimonials,'testimonial':testmony,'sign':sign,'username': request.user.username}
    return render(request,"base.html",context)


# for courses
def testmonies(request):
    testimonials = Testimonial.objects.filter(status=True) 
    testmony=Testimonial.objects.all() # Display only active testimonials
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the new testimonial to the database
            return redirect('testmonials')  # Redirect to the testimonial page
    else:
        form = TestimonialForm()

    return render(request, 'testimonial.html', {'form': form, 'testimonials': testimonials,'testimonial':testmony})
    

def about(request):
    return render(request,"about.html")
def course(request):
    categories=CoursesCategory.objects.all()
    form = courses.COURSE_CHOICES
    forms=courses.image
    return render(request,"ourcourses.html",{'form':form,'forms':forms,'categories':categories})
def contact(request):
    return render(request,"contact.html")


def getbooks(request):
    books=Book.objects.all()
    context={'books':books}
    return render(request,"books.html",context)
def ongoingProjects(request):
    projects=Project.objects.all()
    context={'projects':projects}
    return render(request,"project.html",context)

@login_required
def create_testimonial(request):
    testimonials = Testimonial.objects.all()
    form = TestimonialForm()
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

    return render(request, "testimonial.html",{"testimonials": testimonials,'form': form})


def mysignup(request):
    if request.method == 'POST':
        user_form = MySignupForm(request.POST)
        profile_form = MyUserProfileForm(request.POST,request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            # Saving the profile form and linking to the user
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            # Logging the user in after successful signup
            login(request, user)
            messages.success(request, f"Registration successful! Welcome, {user.username}.")
            return redirect('mylogin')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        user_form = MySignupForm()
        profile_form = MyUserProfileForm()

    return render(request, 'signup.html', {'user_form': user_form, 'profile_form': profile_form})



def login_view(request):
    if request.method == 'POST':
        form = MyLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Check if the user has a UserProfile, and create one if not
                if not hasattr(user, 'userprofile'):
                    UserProfile.objects.create(user=user)
                    
                
                messages.success(request, f"Welcome {user.username}! You have successfully logged in.")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid username or password. Please try again.")
        else:
            print("Form errors:", form.errors)
            messages.error(request, "Please correct the errors below.")
    else:
        form = MyLoginForm()

    return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):
    user = request.user
    user_profile = request.user.userprofile
    user_course = user_profile.course

    units = Unit.objects.filter(course=user_course)
    return render(request, 'dashboard.html', {'username': request.user.username,'user': user,'units': units})


