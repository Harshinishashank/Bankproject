from django.shortcuts import render
# Create your views here.
def signup(request):
    if request.method == "POST":
        email = request.POST.get("email")
        print(email)
        password = request.POST.get("psw")
        confirm_password = request.POST.get("psw-repeat")
        print(email,password,confirm_password)
        return render(request,'user_accounts/signup.html')
    return render(request,'user_accounts/signup.html')