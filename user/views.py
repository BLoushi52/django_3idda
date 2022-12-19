from rest_framework.generics import CreateAPIView
from .serializers import  UserCreateSerializer, UserLoginSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from user.forms import UpdateUserForm, UserLogin, UserRegister
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages


##### API #####
class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        my_data = request.data
        serializer = UserLoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)




##### HTML #####


def home(request: HttpRequest):
    return render(request, "home.html")
    

def user_register(request):
    form = UserRegister()
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)

            return redirect("home")
    context = {
        "form": form,
    }
    return render(request, "register.html", context)


def login_user(request):
    form = UserLogin()
    if request.method == "POST":
        form = UserLogin(request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                # Where you want to go after a successful login
                return redirect("home")

    context = {
        "form": form,
    }
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    return redirect("home")



@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='profile')
    else:
        user_form = UpdateUserForm(instance=request.user)

    context = {
        "form": user_form,
    }
    return render(request, "edit_profile.html", context)

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('home')

   