from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index ,name='homepage'),
    path('courses/',views.course ,name='courses'),
    path('instructors/',views.instructors ,name='instructors'),
    path('login/',views.login ,name='login'),
    
    path('signup/',views.signup ,name='signup'),
    path('testmonials/',views.testmonies ,name='testmonials'),
    path('ctestmonials/',views.create_testimonial ,name='ctestmonials'),
    path('enroll',views.join ,name='enroll'),
    path('student_details',views.student,name='student_details'),
    path('about',views.about,name='about'),
    path('contacts',views.contact,name='contacts'),
    path('student_details',views.student,name='student_details'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
