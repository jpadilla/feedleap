from django import forms

from kippt import Kippt

from .models import KipptUser


class KipptUserConnectForm(forms.ModelForm):

    class Meta:
        model = KipptUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(KipptUserConnectForm, self).__init__(*args, **kwargs)

        self.fields['username'].label = 'Kippt Username'
        self.fields['username'].help_text = ''
        self.fields['password'].label = 'Kippt Password'
        self.fields['password'].widget = forms.PasswordInput()

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        kippt = Kippt(username, password=password)
        user = kippt.account()

        if 'message' in user:
            raise forms.ValidationError(user['message'])

        self.cleaned_data['api_token'] = user['api_token']

        return self.cleaned_data

    def save(self, commit=True):
        user, created = KipptUser.objects.get_or_create(
            username=self.cleaned_data['username'],
        )

        user.api_token = self.cleaned_data['api_token']
        user.save()

        if created:
            user.set_password(None)

        return user, created


class KipptUserSetupForm(forms.ModelForm):
    list_id = forms.ChoiceField(label='Default list')

    class Meta:
        model = KipptUser
        fields = ('list_id',)

    def __init__(self, *args, **kwargs):
        super(KipptUserSetupForm, self).__init__(*args, **kwargs)

        kippt = self.instance.kippt_client()
        meta, lists = kippt.lists()

        LIST_CHOICES = [('', 'Choose a list to store feed items')]

        for kippt_list in lists:
            LIST_CHOICES.append((kippt_list['id'], kippt_list['title']))

        self.fields['list_id'].choices = LIST_CHOICES
