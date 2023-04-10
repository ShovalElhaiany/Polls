from django import forms
from django.core import validators
from .models import Question, Choice
from django.contrib.auth.models import User


class QuestionForm(forms.ModelForm):
    question_text = forms.CharField(
        label='Question Text', max_length=200, validators=[])

    """Another field that creates validation,
    In addition there is an example of using a widget"""
    # pub_date = forms.DateTimeField(label='Date Published', input_formats=[
    #                                '%Y-%m-%d %h:%m:%s'], widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime'}))

    class Meta:
        model = Question
        fields = '__all__'

    def clean(self):
        super().clean()

        """Another way to define validators,
        This way is shown in the models file"""
        # CURSES = ('dumbass', 'moron')
        # for curse in CURSES:
        #     if curse in self.cleaned_data['question_text']:
        #         self.add_error('question_text', 'second added error')
        #         raise forms.ValidationError('Bed word detected')

        return self.cleaned_data


class ChoiceForm(forms.ModelForm):

    """Another field that creates validation or settings"""
    # choice_text = forms.CharField(label='Answer text', max_length=200)
    # votes = forms.IntegerField(label='Number of votes', initial=0)
    # question = forms.ModelChoiceField(queryset=Question.objects.all())

    class Meta:
        model = Choice
        fields = '__all__'

        """List of exceptions if all fields are selected"""
        # exclude = ['votes']

        labels = {
            'choice_text': 'Answer text',
            'votes': 'Number of votes'
        }
        error_messages = {
            'choice_text': {'required': 'this is way to long'}
        }

    def clean(self):
        CURSES = ['dumbass', 'moron']
        super().clean()
        errors = []
        for curse in CURSES:
            if curse in self.cleaned_data['choice_text']:
                errors.append(forms.ValidationError('Bed word detected'))
        if self.cleaned_data['votes'] < 0:
            errors.append(ValueError('Votes mostbe 0 or higher'))

        if len(errors) > 0:
            raise errors
        return self.cleaned_data


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name',
                  'last_name', 'email', 'is_active']


class LoginForm(forms.Form):
    username = forms.CharField(label='User name', required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': ('Current Password')
        }),
        error_messages={
            'required': ('Please enter your current password.')
        })
