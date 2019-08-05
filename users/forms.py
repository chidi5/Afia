from allauth.account.signals import user_signed_up
from allauth.socialaccount.models import SocialAccount
from django import forms
from django.dispatch import receiver
from .models import User
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserChangeForm
from django_countries.fields import CountryField


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def signup(self, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save(using=self._db)
        return user
    '''
    @receiver(user_signed_up)
    def populate_profile(self, user, **kwargs):
        socialaccount_obj = SocialAccount.objects.filter(provider='google', user_id=self.user.id)
        user.image = "not available"
        if len(socialaccount_obj):
            user.image = socialaccount_obj[0].extra_data['picture']
        user.save(using=self._db)
        return user
    '''


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'display_name',
            'first_name',
            'last_name',
            'image',
            'country',
            'location',
        ]
        exclude = [
            'password',
        ]
        widgets = {'country': forms.Select(attrs={'class': "form-control"})}
