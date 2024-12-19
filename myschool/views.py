from django.shortcuts import render,redirect,get_object_or_404
from . models import Signup,UserProfile,Testimonial,courses,Document
from .form import SignupForm,UserProfileForm,LoginForm,TestimonialForm,DocumentForm,MyUserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from .utils import read_pdf, read_docx 
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.




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
        form = SignupForm(request.POST, request.FILES)  # Include request.FILES for handling file uploads
        form1 = UserProfileForm(request.POST)
        
        # Check if a user already exists with the given email
        email = request.POST.get('email')
        if Signup.objects.filter(email=email).exists():
            # Add an error message or redirect to a different page
            form.add_error('email', 'An account with this email already exists.')
        elif form.is_valid() and form1.is_valid():
            # Save the form data to the database
            form.save()
            form1.save()  # Make sure to save the UserProfileForm data as well
            return redirect('login')  # Redirect to the login page after successful signup
    else:
        form = SignupForm()
        form1 = UserProfileForm()

    return render(request, 'signup.html', {'form': form, 'form1': form1})

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



# for  doc

def document_view(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = DocumentForm()
    
    documents = Document.objects.all()
    return render(request, 'document.html', {'form': form, 'documents': documents})



def process_document(request, doc_id):
    doc = get_object_or_404(Document, id=doc_id)
    file_path = doc.file.path
    content = ""

    # Check file type and extract content
    if file_path.endswith(".pdf"):
        content = read_pdf(file_path)
    elif file_path.endswith(".docx"):
        content = read_docx(file_path)
    else:
        content = "Unsupported file format."

    return render(request, 'document_content.html', {'content': content, 'document': doc})


from django.contrib.auth.models import User
from .form import MySignupForm, MyUserProfileForm

def create_user_view(request):
    if request.method == 'POST':
        print("POST data:", request.POST)  # Debug line
        print("FILES:", request.FILES)     # Debug line
        
        form = MySignupForm(request.POST)
        profile_form = MyUserProfileForm(request.POST, request.FILES)
        
        if form.is_valid() and profile_form.is_valid():
            try:
                # Create User instance
                user = User.objects.create_user(
                    username=form.cleaned_data['email'],  # Using email as username
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                )
                user.save()
                print(f"User created: {user.id}")  # Debug line
                
                # Save MySignup instance
                signup = form.save(commit=False)
                signup.save()
                print(f"Signup saved: {signup.id}")  # Debug line
                
                # Save MyUserProfile instance
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                print(f"Profile saved: {profile.id}")  # Debug line
                
                # Log the user in
                login(request, user)
                messages.success(request, 'Your account has been created successfully!')
                return redirect('homepage')
                
            except Exception as e:
                print(f"Error during save: {str(e)}")  # Debug line
                messages.error(request, f'Error creating account: {str(e)}')
        else:
            print("Form errors:", form.errors)  # Debug line
            print("Profile form errors:", profile_form.errors)  # Debug line
            messages.error(request, 'Please correct the errors below.')
    else:
        form = MySignupForm()
        profile_form = MyUserProfileForm()
    
    return render(request, 'user.html', {
        'form': form,
        'profile_form': profile_form
    })