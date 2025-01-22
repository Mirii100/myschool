from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
urlpatterns = [
path('',views.paymentDashboard ,name='home'),
path('payments/', views.payment_list, name='payment_list'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)