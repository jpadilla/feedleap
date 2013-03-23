from django import forms

from libs import kippt

from .models import KipptUser


class KipptUserCreationForm(forms.ModelForm):

    class Meta:
        model = KipptUser
        fields = ('username', 'api_token')

    def clean_api_token(self):
        username = self.cleaned_data.get('username')
        api_token = self.cleaned_data.get("api_token")

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
