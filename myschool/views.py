from django.shortcuts import render,redirect
from . models import Signup,UserProfile,Testimonial,courses,CoursesCategory,Book,Project,Instructor,Unit
from .form import SignupForm,UserProfileForm,LoginForm,TestimonialForm,MySignupForm, MyUserProfileForm,MyLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User

from django.contrib import messages  # Import messages framework
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .form import ContactForm
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


from django.contrib.auth import logout


from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect

def success_page(request):
    return render(request, 'index.html')  # Create this template
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
        

        

        return redirect("homepage")

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
                UserProfile.objects.get_or_create(user=user)
                login(request, user)
                # Check if the user has a UserProfile, and create one if not
               
                    
                
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
    try:
        user_profile = request.user.userprofile
        # Print debug information
        print(f"User Profile Course: {user_profile.course}")
        print(f"User Profile Course Type: {user_profile.course_type}")
        user_course = user_profile.course
        # Try filtering by both course and course_type
        units = Unit.objects.filter(course=user_course)
        print(f"Found {units.count()} units")
        all_units = Unit.objects.all()
        print("All Units:", [(unit.unit_name, unit.course) for unit in all_units])
        print(f"Total units in database: {all_units.count()}")
        print("Available units:", [(u.unit_name, u.course) for u in all_units])
        return render(request, 'dashboard.html', 
                {
            'username': request.user.username,
            'user': user,
            'units': units,
            'all_units': all_units,
            'user_profile': user_profile,
            })
    except UserProfile.DoesNotExist:
        messages.error(request, "User profile not found")
        return redirect('mylogin')




@login_required
def faq(request):
    return render(request, 'faq.html')

@login_required
def academic_guide(request):
    return render(request, 'academic_guide.html')

@login_required
def unit_registration(request):
    return render(request, 'unit_registration.html')

@login_required
def lecturer_evaluation(request):
    return render(request, 'lecturer_evaluation.html')

@login_required
def course_change(request):
    return render(request, 'course_change.html')

@login_required
def lms(request):
    # This could redirect to your LMS system
    return render(request, 'lms.html')

# Fee-related views
@login_required
def fee_statement(request):
    user_profile = request.user.myuser
    context = {
        'total_billed': user_profile.total_billed,
        'total_paid': user_profile.total_paid,
        'fee_balance': user_profile.fee_balance,
        'transactions': user_profile.fee_transactions.all()  # Assuming related name
    }
    return render(request, 'fee_statement.html', context)

@login_required
def payment_receipts(request):
    receipts = request.user.myuser.fee_transactions.filter(status='completed')
    return render(request, 'payment_receipts.html', {'receipts': receipts})

@login_required
def make_payment(request):
    if request.method == 'POST':
        # Add payment processing logic here
        pass
    return render(request, 'make_payment.html')

@login_required
def confirm_payment(request):
    if request.method == 'POST':
        # Add payment confirmation logic here
        pass
    return render(request, 'confirm_payment.html')

# Phone number management views
@login_required
def edit_phone_number(request):
    if request.method == 'POST':
        new_phone = request.POST.get('phone_number')
        if new_phone:
            request.user.myuser.phone_number = new_phone
            request.user.myuser.save()
            messages.success(request, 'Phone number updated successfully.')
        return redirect('dashboard')
    return render(request, 'edit_phone.html')

@login_required
def confirm_phone_number(request):
    if request.method == 'POST':
        # Add phone confirmation logic here
        pass
    return render(request, 'confirm_phone.html')

@login_required
def edit_contact(request):
    user = request.user
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to a page like dashboard after saving
    else:
        form = ContactForm(instance=user)
    
    return render(request, 'payment.html', {'form': form})