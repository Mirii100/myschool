from django.shortcuts import render
from myschool.models import Unit
from .models import Payment
# Create your views here.
def paymentDashboard(request):
    return render(request,'payment.html')


def payment_list(request):
    # Retrieve all payments or filter based on some criteria (e.g., user)
    payments = Payment.objects.filter(user=request.user)
    units = Unit.objects.filter(user=request.user)
    return render(request, 'payment.html', {'payments': payments,'units': units})
