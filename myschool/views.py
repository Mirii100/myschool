from django.shortcuts import render,redirect
from . models import Signup,UserProfile,Testimonial,courses,CoursesCategory,Book,Project,Instructor
from .form import SignupForm,UserProfileForm,LoginForm,TestimonialForm,MySignupForm, MyUserProfileForm,MyLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User

from django.contrib import messages  # Import messages framework


from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logging out


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

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
    context={'testimonials':testimonials,'testimonial':testmony,'sign':sign}
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
        profile_form = MyUserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Create User
            user = user_form.save()
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            # Create UserProfile
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # Log the user in
            login(request, user)
            return redirect('mylogin')  # Redirect to dashboard after successful registration

    else:
        user_form = MySignupForm()
        profile_form = MyUserProfileForm()

    return render(request, 'signup.html', {'user_form': user_form, 'profile_form': profile_form})


def login_view(request):
    if request.method == 'POST':
        form = MyLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome {user.username}! You have successfully logged in.")
                print("Redirecting to dashboard...")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid username or password. Please try again.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = MyLoginForm()

    return render(request, 'login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'username': request.user.username})

