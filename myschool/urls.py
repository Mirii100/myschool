from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('',views.index ,name='homepage'),
    path('courses/',views.course ,name='courses'),
    path('instructors/',views.instructors ,name='instructors'),
   path('log/', LogoutView.as_view(next_page='homepage'), name='logo'),
    path('logout/', views.logout_view, name='logout'),
     path('mylogin/', views.login_view, name='mylogin'),
     path('dashboard/', views.dashboard, name='dashboard'),
     path('mysignup/', views.mysignup, name='mysignup'),
    path('books/',views.getbooks ,name='books'),
    path('projects/',views.ongoingProjects ,name='projects'),
     path('success/', views.success_page, name='success_page'),
    path('testmonials/',views.testmonies ,name='testmonials'),
    path('ctestmonials/',views.create_testimonial ,name='ctestmonials'),
    path('enroll',views.join ,name='enroll'),
    path('student_details/',views.student,name='student_details'),
    path('about',views.about,name='about'),
    path('contacts',views.contact,name='contacts'),
    path('join',views.dashboard,name='join'),




    
    # Quick Help and Links
    path('faq/', views.faq, name='faq'),
    path('academic-guide/', views.academic_guide, name='academic_guide'),
    path('unit-registration/', views.unit_registration, name='unit_registration'),
    path('lecturer-evaluation/', views.lecturer_evaluation, name='lecturer_evaluation'),
    path('course-change/', views.course_change, name='course_change'),
    path('lms/', views.lms, name='lms'),
    
    # Fee Management
    path('fee-statement/', views.fee_statement, name='fee_statement'),
    path('payment-receipts/', views.payment_receipts, name='payment_receipts'),
    path('make-payment/', views.make_payment, name='make_payment'),
    path('confirm-payment/', views.confirm_payment, name='confirm_payment'),
    
    # Phone Management
    path('edit-phone/', views.edit_phone_number, name='edit_phone'),
    path('confirm-phone/', views.confirm_phone_number, name='confirm_phone'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
