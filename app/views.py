from django.shortcuts import render, redirect
from .models import Donor

# HOME
def select_role(request):
    return render(request, 'selectrole.html')

def home(request):
    return render(request, 'main1.html')


# DONOR REGISTER
def donor_register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email').strip()
        password = request.POST.get('password').strip()
        address = request.POST.get('address')

        if Donor.objects.filter(email=email).exists():
            return render(request, 'register.html', {
                'error': 'Email already registered!'
            })

        Donor.objects.create(
            name=name,
            mobile=mobile,
            email=email,
            password=password,
            address=address
        )

        return redirect('/donor-login/')

    return render(request, 'register.html')


# DONOR LOGIN
def donor_login(request):
    if request.method == "POST":
        email = request.POST.get('email').strip()
        password = request.POST.get('password').strip()

        try:
            user = Donor.objects.get(email=email)

            if user.password == password:
                
                # ADD THIS LINE HERE
                request.session['user'] = user.name

                return redirect('/home/')
            else:
                return render(request, 'donerlogin.html', {'error': 'Wrong Password'})

        except Donor.DoesNotExist:
            return render(request, 'donerlogin.html', {'error': 'User not found'})

    return render(request, 'donerlogin.html')
def logout_view(request):
    request.session.flush()
    return redirect('/')
# ORG LOGIN
def org_login(request):
    return render(request, 'organizationlogin.html')


# ORG REGISTER  (THIS WAS MISSING)
def org_register(request):
    return render(request, 'organizating.html')


# OTHER PAGES
def donate(request):
    return render(request, 'donate.html')

def request_page(request):
    return render(request, 'request.html')

def about(request):
    return render(request, 'aboutus.html')