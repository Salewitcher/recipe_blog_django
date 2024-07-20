
from django.core.mail import send_mail
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    def signup(self, request, user):
        # Send a custom welcome email
        send_mail(
            'Welcome to Our Site!',
            'Hi {},\n\nThank you for signing up at our site! We are excited to have you with us.'.format(user.username),
            'sashestojkoski@gmail.com',
            [user.email],
            fail_silently=False,
        )
        return user
