from django.shortcuts import render
from django. views import View
# Create your views here.
class Landing(View):
    def get(self,request):
        return render(request,"App1/landing.html")

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.views import View
from django.shortcuts import render, redirect

class login_page(View):
    template_name = 'App1/Login_page.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Log the user in.
            login(request, form.get_user())
            # Redirect to a success page.
            return redirect('Home')  # Change 'home' to the actual URL name of your home page.
        return render(request, self.template_name, {'form': form})

from django.views import View
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

class Register_page(View):
    template_name = 'App1/Register_page.html'

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # You can customize the redirect URL after registration
            return redirect('login_page')
        return render(request, self.template_name, {'form': form})


from django.contrib.auth import logout

class LogoutView(View):
    def get(self, request):
        logout(request)
        # Redirect to the landing page or any other desired page after logout
        return redirect('Landing')  # Change 'landing' to the actual URL name of your landing page
