from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

from libs import kippt

from .models import KipptUser

USERNAME_HELP_TEXT = 'Use your Kippt username'
API_TOKEN_HELP_TEXT = 'You can find it \
<a href="https://kippt.com/developers/#apikey">here</a>'


class KipptUserCreationForm(forms.ModelForm):

    class Meta:
        model = KipptUser
        fields = ('username', 'api_token')

    def __init__(self, *args, **kwargs):
        super(KipptUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['api_token'].label = 'API Token'
        self.fields['username'].help_text = USERNAME_HELP_TEXT
        self.fields['api_token'].help_text = API_TOKEN_HELP_TEXT

    def clean_api_token(self):
        username = self.cleaned_data.get('username')
        api_token = self.cleaned_data.get('api_token')

        kippt_client = kippt.Client(username, api_token)
        user = kippt_client.account()

        if not user:
            raise forms.ValidationError('Invalid API Token')

        return api_token

    def save(self, commit=True):
        user = super(KipptUserCreationForm, self).save(commit=False)
        user.set_password(None)

        if commit:
            user.save()

        return user


class KipptUserSetupForm(forms.ModelForm):
    list_id = forms.ChoiceField(label='Your lists')

    class Meta:
        model = KipptUser
        fields = ('list_id',)

    def __init__(self, *args, **kwargs):
        super(KipptUserSetupForm, self).__init__(*args, **kwargs)

        kippt_client = self.instance.kippt_client()
        meta, lists = kippt_client.getLists()

        LIST_CHOICES = [('', 'Choose a list to store feed items')]

        for kippt_list in lists:
            LIST_CHOICES.append((kippt_list['id'], kippt_list['title']))

        self.fields['list_id'].choices = LIST_CHOICES


class KipptUserAuthForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    api_token = forms.CharField(label='API Token', widget=forms.PasswordInput)

    error_messages = {
        'invalid_login': ('Please enter a correct %(username)s and API Token. '
                          'Note that both fields may be case-sensitive.'),
        'inactive': 'This account is inactive.',
    }

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super(KipptUserAuthForm, self).__init__(*args, **kwargs)

        del self.fields['password']
        self.fields['username'].help_text = USERNAME_HELP_TEXT
        self.fields['api_token'].help_text = API_TOKEN_HELP_TEXT

    def clean(self):
        username = self.cleaned_data.get('username')
        api_token = self.cleaned_data.get('api_token')

        if username and api_token:
            self.user_cache = authenticate(username=username,
                                           api_token=api_token)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'] % {
                        'username': self.username_field.verbose_name
                    })
            elif not self.user_cache.is_active:
                raise forms.ValidationError(self.error_messages['inactive'])
        return self.cleaned_data
