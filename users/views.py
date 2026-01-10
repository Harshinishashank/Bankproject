from django.shortcuts import render
from .models import User
from django.contrib.auth.hashers import make_password
from .models import User

# Create your views here.

def account_opening(request):
    if request.method == 'POST':
        # Process the form data here (not implemented)
        username = request.POST.get('username')
        password =  request.POST.get('password')
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        role = request.POST.get('role')
        # You would typically save the user data to the database here
        print(f"Account created for username: {username}")

        # 1. Manually hash the password
        # This turns '12345' into 'pbkdf2_sha256$600000$random_hash...'
        hashed_password = make_password(password)

        if User.objects.filter(username=username).exists():
            print("Username already exists.")
            return render(request, 'users/error.html')

        #writing to database
        user = User.objects.create_user(
            username=username,
            password=hashed_password,
            first_name=fname,
            last_name=lname,
            email=email,
            phone=phone,
            role=role
        )
    return render(request,'users/account_opening.html')
