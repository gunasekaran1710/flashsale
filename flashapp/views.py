from django.shortcuts import render, redirect
from .models import FlashSale
from django.utils import timezone


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        request.session['username'] = username
        return redirect('flashsales')
    return render(request, 'login.html')

# def flashsales_view(request):
#     if 'username' not in request.session:
#         return redirect('login')

#     now = timezone.now()
#     sales = FlashSale.objects.filter(start_time__lte=now, end_time__gte=now)
#     return render(request, 'flashsales.html', {'sales': sales, 'username': request.session['username']})
def flashsales_view(request):
    if 'username' not in request.session:
        return redirect('login')

    now = timezone.now()
    sales = FlashSale.objects.filter(start_time__lte=now, end_time__gte=now)
    return render(request, 'flashsales.html', {
        'sales': sales,
        'username': request.session['username']
    })
