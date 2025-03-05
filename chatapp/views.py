from django.shortcuts import render, redirect
from chat.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import  api_view

@api_view(['POST'])
def demo(request):
    if request.method == "POST":
        username = request.data["username"]

        r = Room()
        r.room_name = username
        r.save()

        return Response({"username": [username, "data saved succesfully!"]})
    return Response({"message": "This is a post request"})



# ?this fcn is to check only api testing only

# from django.views.decorators.csrf import csrf_exempt

# @api_view(['POST', 'GET'])
# @csrf_exempt
# def Login(request):

#     if request.method == 'POST':
#         username = request.data["username"]
#         password = request.data["password"]

        
#         if not User.objects.filter(username = username).exists():
#             return Response({"message":"Invalid Username! Enter correct username."})
        
#         user = authenticate(username = username, password = password)
        
#         if user is None:
#             return Response({"message":"Invalid Credentials! Try Again.."})
            
#         else:
#             login(request, user)
#             return Response({"message":"userloggedIn succesfully"})

#     return Response({"message":"Please input data"})



def Login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        if not User.objects.filter(username = username).exists():
            messages.info(request, "Invalid Username! Enter correct username.")
            return redirect('/login/')
        
        user = authenticate(username = username, password = password)
        
        if user is None:
            messages.info(request, "Invalid Credentials! Try Again.")
            return redirect('/login/')
            
        else:
            login(request, user)
            return redirect('../')

    return render(request, 'login.html')


def Logout(request):
    logout(request)
    return redirect('/login/')

def signup(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('firstname')
        # number = request.POST.get('number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        user = User.objects.filter(username__icontains = username)
    
        if user.exists():
            messages.info(request, "This Username is already registered with other user. Try different username.")
            return redirect('/signup/')


        user = User.objects.create(
            first_name = first_name,
            username = username,
            email = email
        )
        
        if password == password2:
            print(password, password2, password == password2)
            user.set_password(password)
            user.save()
            messages.info(request, "User created seccusfully.")
        else:
            messages.info(request, "Entered Wrong Password! Re-confirm your password.")
            return redirect('/signup/')

        return redirect('/login/')

    return render(request, 'signup.html')

# def dp(request, username):
#         image = UploadDp.objects.filter(user = username).values()
#         location = image[0]['dp']
        
#         if image.exists():
#             print(image[0]['dp'])

        
#             if request.method == 'POST':
#                 profile = UploadDp()
#                 profile.dp = request.FILES['profile_pic']
#                 profile.user = username
#                 profile.save()

#             return redirect("home")

#         params= {"loc": location}    
#         return render(request,'dp.html', params)
