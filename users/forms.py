
from django import forms
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    def signup(self, request, user):
        # Save additional profile information if provided
        user.save()
        return user
