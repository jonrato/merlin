from django.http.response import HttpResponseRedirect
from common.forms import SignUpForm
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import SignUpForm
from django.urls import reverse_lazy

from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UserForm, ProfileForm
from django.contrib.auth.models import User
from userprofile.models import Profile

from django.contrib import messages

class ProfilePay(LoginRequiredMixin, TemplateView):
    template_name = 'payments/order_history.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard-perfil.html'

class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'profile-update-upload.html'

    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data,file_data, instance=request.user)
        profile_form = ProfileForm(post_data,file_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            #messages.sucess(request, "Your Profile was sucess updated")
            return HttpResponseRedirect(reverse_lazy('dashboard-perfil'))
        
        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'cadastro.html'

