from django.db import models
from django.contrib.auth.models import User


class Specialization(models.Model):
    specialization_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)  # E.g., "Software Engineer"
    description = models.TextField(blank=True, null=True)  # Detailed description of the specialization
    field = models.CharField(
        max_length=50,
        choices=[
            ('Engineering', 'Engineering'),
            ('Science', 'Science'),
            ('Arts', 'Arts'),
            ('Business', 'Business'),
            ('Technology', 'Technology'),
        ],
        default='Technology'
    )  # Broader field of specialization
    popular_courses = models.TextField(blank=True, null=True)  # JSON or text for common courses in this field

    def __str__(self):
        return self.name


class Signup(models.Model):
    TITLE_CHOICES = [
        ('mr', 'Mr.'),
        ('mrs', 'Mrs.'),
        ('ms', 'Ms.'),
        ('dr', 'Dr.'),
        ('prof', 'Prof.'),
    ]

    COURSE_CHOICES = [
    # Computer Science and Technology
    ('cs', 'Computer Science'),
    ('ai', 'Artificial Intelligence'),
    ('ml', 'Machine Learning'),
    ('ds', 'Data Science'),
    ('web_dev', 'Web Development'),
    ('app_dev', 'Mobile Application Development'),
    ('cybersec', 'Cyber Security'),
    ('ethical_hacking', 'Ethical Hacking'),
    ('software_dev', 'Software Development'),
    ('networking', 'Computer Networking'),
    ('cloud_computing', 'Cloud Computing'),
    ('iot', 'Internet of Things (IoT)'),
    ('blockchain', 'Blockchain Technology'),
    ('devops', 'DevOps'),

    # Business and Commerce
    ('bcom', 'Commerce'),
    ('mba', 'Master of Business Administration'),
    ('accounting', 'Accounting and Finance'),
    ('marketing', 'Marketing'),
    ('hrm', 'Human Resource Management'),
    ('entrepreneurship', 'Entrepreneurship'),
    ('economics', 'Economics'),

    # Arts and Humanities
    ('literature', 'English Literature'),
    ('history', 'History'),
    ('philosophy', 'Philosophy'),
    ('psychology', 'Psychology'),
    ('sociology', 'Sociology'),
    ('political_science', 'Political Science'),
    ('linguistics', 'Linguistics'),
    ('fine_arts', 'Fine Arts'),
    ('music', 'Music'),
    ('film_studies', 'Film Studies'),
    ('design', 'Graphic Design'),

    # Science and Mathematics
    ('math', 'Mathematics'),
    ('physics', 'Physics'),
    ('chemistry', 'Chemistry'),
    ('biology', 'Biology'),
    ('geology', 'Geology'),
    ('statistics', 'Statistics'),
    ('environmental_science', 'Environmental Science'),
    ('biotech', 'Biotechnology'),
    ('astrophysics', 'Astrophysics'),

    # Engineering
    ('mech_eng', 'Mechanical Engineering'),
    ('civil_eng', 'Civil Engineering'),
    ('elec_eng', 'Electrical Engineering'),
    ('elec_comm_eng', 'Electronics and Communication Engineering'),
    ('chemical_eng', 'Chemical Engineering'),
    ('aero_eng', 'Aerospace Engineering'),
    ('biomed_eng', 'Biomedical Engineering'),
    ('robotics', 'Robotics Engineering'),

    # Health and Medical
    ('medicine', 'Medicine'),
    ('nursing', 'Nursing'),
    ('pharmacy', 'Pharmacy'),
    ('dentistry', 'Dentistry'),
    ('physiotherapy', 'Physiotherapy'),
    ('public_health', 'Public Health'),

    # Law and Governance
    ('law', 'Law'),
    ('criminology', 'Criminology'),
    ('forensics', 'Forensic Science'),
    ('international_relations', 'International Relations'),
    ('public_admin', 'Public Administration'),

    # Miscellaneous
    ('education', 'Education'),
    ('sports_science', 'Sports Science'),
    ('hospitality', 'Hospitality Management'),
    ('tourism', 'Tourism and Travel'),
    ('culinary_arts', 'Culinary Arts'),
    ('journalism', 'Journalism and Mass Communication'),
    ('fashion_design', 'Fashion Design'),
    ('animation', 'Animation'),
    ('agriculture', 'Agriculture'),
    ('marine_biology', 'Marine Biology'),
    ('veterinary', 'Veterinary Science'),
    ('ai_ml', 'Artificial Intelligence & Machine Learning'),
]


    CONTACT_HOURS_CHOICES = [
       ('4am-5am', '4:00 AM - 5:00 AM'),
    ('5am-6am', '5:00 AM - 6:00 AM'),
    ('6am-7am', '6:00 AM - 7:00 AM'),
    ('7am-8am', '7:00 AM - 8:00 AM'),
    ('8am-9am', '8:00 AM - 9:00 AM'),
    ('9am-10am', '9:00 AM - 10:00 AM'),
    ('10am-11am', '10:00 AM - 11:00 AM'),
    ('11am-12pm', '11:00 AM - 12:00 PM'),
    ('12pm-1pm', '12:00 PM - 1:00 PM'),
    ('1pm-2pm', '1:00 PM - 2:00 PM'),
    ('2pm-3pm', '2:00 PM - 3:00 PM'),
    ('3pm-4pm', '3:00 PM - 4:00 PM'),
    ('4pm-5pm', '4:00 PM - 5:00 PM'),
    ('5pm-6pm', '5:00 PM - 6:00 PM'),
    ('6pm-7pm', '6:00 PM - 7:00 PM'),
    ('7pm-8pm', '7:00 PM - 8:00 PM'),
    ('8pm-9pm', '8:00 PM - 9:00 PM'),
    ('9pm-10pm', '9:00 PM - 10:00 PM'),
    ('10pm-11pm', '10:00 PM - 11:00 PM'),
    ('11pm-12am', '11:00 PM - 12:00 AM'),
    ]

    CONFIRM_TYPE_CHOICES = [
        ('by_phone', 'By Phone'),
        ('by_email', 'By Email'),
    ]

    title = models.CharField(max_length=10, choices=TITLE_CHOICES, verbose_name="Title")
    name = models.CharField(max_length=255, verbose_name="Full Name")
    email = models.EmailField(unique=True, verbose_name="Email")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")
    course_type = models.CharField(max_length=50, choices=COURSE_CHOICES, verbose_name="Course Type")
    confirm_type = models.CharField(max_length=20, choices=CONFIRM_TYPE_CHOICES, verbose_name="Confirmation Type")
    contact_hours = models.CharField(max_length=20, choices=CONTACT_HOURS_CHOICES, verbose_name="Contact Hours")
    agree_terms = models.BooleanField(default=False, verbose_name="Agree to Terms and Conditions")
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True, verbose_name="Profile Image") 
    def __str__(self):
        return f"{self.name} - {self.email}  {self.title} - {self.phone_number}, {self.agree_terms}"



class UserProfile(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    course_type = models.CharField(max_length=100)
    confirm_type = models.CharField(max_length=100)
    contact_hours = models.CharField(max_length=50)
    agree_terms = models.BooleanField(default=False)

    def __str__(self):
        return self.name



class Testimonial(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)  # Allow null value
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    message = models.TextField()
    image = models.ImageField(upload_to='testimonials/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, default='active') 

    def __str__(self):
        return f'{self.name} {self.status} {self.message} {self.image} {self.user}'
class courses(models.Model):


    COURSE_CHOICES = [
    # Computer Science and Technology
    ('cs', 'Computer Science'),
    ('ai', 'Artificial Intelligence'),
    ('ml', 'Machine Learning'),
    ('ds', 'Data Science'),
    ('web_dev', 'Web Development'),
    ('app_dev', 'Mobile Application Development'),
    ('cybersec', 'Cyber Security'),
    ('ethical_hacking', 'Ethical Hacking'),
    ('software_dev', 'Software Development'),
    ('networking', 'Computer Networking'),
    ('cloud_computing', 'Cloud Computing'),
    ('iot', 'Internet of Things (IoT)'),
    ('blockchain', 'Blockchain Technology'),
    ('devops', 'DevOps'),

    # Business and Commerce
    ('bcom', 'Commerce'),
    ('mba', 'Master of Business Administration'),
    ('accounting', 'Accounting and Finance'),
    ('marketing', 'Marketing'),
    ('hrm', 'Human Resource Management'),
    ('entrepreneurship', 'Entrepreneurship'),
    ('economics', 'Economics'),

    # Arts and Humanities
    ('literature', 'English Literature'),
    ('history', 'History'),
    ('philosophy', 'Philosophy'),
    ('psychology', 'Psychology'),
    ('sociology', 'Sociology'),
    ('political_science', 'Political Science'),
    ('linguistics', 'Linguistics'),
    ('fine_arts', 'Fine Arts'),
    ('music', 'Music'),
    ('film_studies', 'Film Studies'),
    ('design', 'Graphic Design'),

    # Science and Mathematics
    ('math', 'Mathematics'),
    ('physics', 'Physics'),
    ('chemistry', 'Chemistry'),
    ('biology', 'Biology'),
    ('geology', 'Geology'),
    ('statistics', 'Statistics'),
    ('environmental_science', 'Environmental Science'),
    ('biotech', 'Biotechnology'),
    ('astrophysics', 'Astrophysics'),

    # Engineering
    ('mech_eng', 'Mechanical Engineering'),
    ('civil_eng', 'Civil Engineering'),
    ('elec_eng', 'Electrical Engineering'),
    ('elec_comm_eng', 'Electronics and Communication Engineering'),
    ('chemical_eng', 'Chemical Engineering'),
    ('aero_eng', 'Aerospace Engineering'),
    ('biomed_eng', 'Biomedical Engineering'),
    ('robotics', 'Robotics Engineering'),

    # Health and Medical
    ('medicine', 'Medicine'),
    ('nursing', 'Nursing'),
    ('pharmacy', 'Pharmacy'),
    ('dentistry', 'Dentistry'),
    ('physiotherapy', 'Physiotherapy'),
    ('public_health', 'Public Health'),

    # Law and Governance
    ('law', 'Law'),
    ('criminology', 'Criminology'),
    ('forensics', 'Forensic Science'),
    ('international_relations', 'International Relations'),
    ('public_admin', 'Public Administration'),

    # Miscellaneous
    ('education', 'Education'),
    ('sports_science', 'Sports Science'),
    ('hospitality', 'Hospitality Management'),
    ('tourism', 'Tourism and Travel'),
    ('culinary_arts', 'Culinary Arts'),
    ('journalism', 'Journalism and Mass Communication'),
    ('fashion_design', 'Fashion Design'),
    ('animation', 'Animation'),
    ('agriculture', 'Agriculture'),
    ('marine_biology', 'Marine Biology'),
    ('veterinary', 'Veterinary Science'),
    ('ai_ml', 'Artificial Intelligence & Machine Learning'),
]
    course_type = models.CharField(max_length=50, choices=COURSE_CHOICES, verbose_name="Course Type")
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True, verbose_name="Profile Image")
    title = models.CharField(max_length=100, choices=COURSE_CHOICES, verbose_name="Title") 
    name = models.CharField(max_length=255, verbose_name="comp",default='cs')
    def __str__(self):
        return f"  {self.title} - {self.image}, {self.name}"
    
class CoursesCategory(models.Model):
    title = models.CharField(max_length=100)
    COURSE_category=['Computer Science and Technology','Business and Commerce','Arts and Humanities',
                     'Science and Mathematics','Engineering','Health and Medical','Law and Governance','Miscellaneous']
    
    #course=models.ForeignKey(courses,on_delete=models.CASCADE,default='cs',to_field='course_type',unique=True,null=True)
    #m=models.OneToOneField(courses,unique=True,to_field='course_type',null=True,on_delete=models.CASCADE)



class Instructor(models.Model):
    # Basic Information
    instructor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    # Professional Information
    specialization = models.ManyToManyField('Specialization', related_name='instructors')
    experience = models.IntegerField()  # Years of experience
    qualification = models.CharField(max_length=100)
    employment_type = models.CharField(
        max_length=20,
        choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Freelance', 'Freelance')],
        default='Full-time'
    )

    # Availability
    available_hours = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    # Ratings and Feedback
    rating = models.FloatField(default=0.0)  # Scale: 1.0 to 5.0
    reviews = models.TextField(blank=True, null=True)  # JSON or text for student reviews

    # Courses Taught
    courses = models.ManyToManyField('Signup', related_name='COURSE_CHOICES')
    # Profile Details
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='instructors/profile_pictures/', blank=True, null=True)
    social_links = models.JSONField(blank=True, null=True)  # Store social links as a JSON object

    # Additional Information
    date_joined = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)  # Active or Inactive status

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.specialization})"
    



class Book(models.Model):
    # Basic Information
    title = models.CharField(max_length=255)  # Title of the book
    author = models.CharField(max_length=255)  # Author's name
    isbn = models.CharField(max_length=13, unique=True)  # ISBN (13 characters)
    publication_date = models.DateField()  # Date of publication
    publisher = models.CharField(max_length=255, blank=True, null=True)  # Publisher name

    # Book Details
    genre = models.CharField(max_length=100)  # Genre (e.g., Fiction, Non-fiction, Fantasy)
    language = models.CharField(max_length=50, default="English")  # Language of the book
    description = models.TextField(blank=True, null=True)  # Description or summary of the book

    # Availability & Stock
    total_copies = models.PositiveIntegerField()  # Total copies available
    available_copies = models.PositiveIntegerField()  # Copies currently available for issue

    # Media
    cover_image = models.ImageField(upload_to="book_covers/", blank=True, null=True)  # Path to cover image
    pdf_file = models.FileField(upload_to="book_pdfs/", blank=True, null=True)  # Path to book PDF file

    # Additional Information
    added_on = models.DateTimeField(auto_now_add=True)  # Timestamp for when the book was added
    updated_on = models.DateTimeField(auto_now=True)  # Timestamp for the last update

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']  # Default ordering by title




class Project(models.Model):
    # Basic Information
    name = models.CharField(max_length=255)  # Project name
    description = models.TextField(blank=True, null=True)  # Detailed description of the project
    client_name = models.CharField(max_length=255, blank=True, null=True)  # Client name or organization
    start_date = models.DateField()  # Project start date
    end_date = models.DateField(blank=True, null=True)  # Project end date (optional)
    status = models.CharField(
        max_length=50, 
        choices=[('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Completed', 'Completed')],
        default='Not Started'
    )  # Current status of the project

    # Financial Information
    budget = models.DecimalField(max_digits=10, decimal_places=2)  # Total project budget
    expenses = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Current expenses

    # Team & Contributors
    project_manager = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)  # Project manager
    team_members = models.ManyToManyField('auth.User', related_name='project_team_members', blank=True)  # Team members

    # Timeline & Progress Tracking
    progress_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  # Progress as a percentage
    milestones = models.TextField(blank=True, null=True)  # Key milestones or phases

    # Documentation & Files
    project_files = models.FileField(upload_to='project_documents/', blank=True, null=True)  # File associated with the project
    related_links = models.TextField(blank=True, null=True)  # Links to external resources or documentation

    # Additional Information
    created_on = models.DateTimeField(auto_now_add=True)  # Timestamp for when the project was created
    updated_on = models.DateTimeField(auto_now=True)  # Timestamp for the last update to the project
    archived = models.BooleanField(default=False)  # Archive flag for completed/old projects

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['start_date']  # Default ordering by start date



