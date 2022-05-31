from gc import get_objects
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from blog.models import Profile
from blog.models import Profile
from .forms import SignUpForm, EditProfileForm, CreateProfileForm

#-------------------------------------------------------------------------------------------------#

class UserRegister(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy ('login')

#-------------------------------------------------------------------------------------------------#

class UserProfileEdit(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/profile_edit.html'
    success_url = reverse_lazy ('home')

    def get_object(self):
        return self.request.user

#-------------------------------------------------------------------------------------------------#

class PasswordChangesView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy ('password_success')

#-------------------------------------------------------------------------------------------------#

def password_success(request):
    return render(request,'registration/password_success.html', {})

#-------------------------------------------------------------------------------------------------#

class ProfilePage(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data (self , *args , **kwargs):
        # users = Profile.objects.all()
        context = super(ProfilePage,self).get_context_data(*args,**kwargs)

        user_page = get_object_or_404(Profile, id= self.kwargs['pk'])

        context [ "user_page" ] = user_page
        return context

#-------------------------------------------------------------------------------------------------#

class EditProfilePage(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = [ 'biographie', 'profile_pic', 'twitter', 'facebook', 'website' ]
    success_url = reverse_lazy ('home')

#-------------------------------------------------------------------------------------------------#

class CreateProfilePage(CreateView):
    model = Profile
    form_class= CreateProfileForm
    template_name = 'registration/create_profile_page.html'
    # fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)