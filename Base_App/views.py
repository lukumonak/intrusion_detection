from django.shortcuts import render



def AlertViews(request):
    return render(request, 'alert.html', {'alert_message': 'Suspicious activity detected from IP: 192.168.1.25. Immediate action recommended!'})


def SafeViews(request):
    return render(request, 'safe.html', {'message': 'No suspicious activity detected. System is secure.'})


def HomeViews(request):
    return render(request, 'home.html')


