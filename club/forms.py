from django import forms
from .models import Event, CheckIn, Url, File, Album, AlbumImage, Poll, Choice, Post
from django.contrib.auth.models import Group,User
import datetime
import random, string

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'permissions']

    users = forms.ModelMultipleChoiceField(queryset=User.objects.all())

    # Overriding __init__ here allows us to provide initial
    # data for 'users' field
    def __init__(self, *args, **kwargs):
        # Only in case we build the form from an instance
        # (otherwise, 'users' list should be empty)
        if kwargs.get('instance'):
            # We get the 'initial' keyword argument or initialize it
            # as a dict if it didn't exist.                
            initial = kwargs.setdefault('initial', {})
            # The widget for a ModelMultipleChoiceField expects
            # a list of primary key for the selected data.
            initial['users'] = [t.pk for t in kwargs['instance'].user_set.all()]
        forms.ModelForm.__init__(self, *args, **kwargs)

    def save(self):
        instance = forms.ModelForm.save(self)
        instance.user_set.clear()
        instance.user_set.add(*self.cleaned_data['users'])
        return instance



class EventForm(forms.ModelForm):
    code = ''.join(random.choice(string.digits) for x in range(5))
    date = forms.DateField(initial=datetime.date.today)
    checkcode = forms.CharField(initial=code)
    class Meta:
        model = Event
        fields = ['category','name','date','checkcode', ]


class CheckInForm(forms.ModelForm):
    class Meta:
        model = CheckIn
        fields = [ 'nid', 'user', 'event']


class UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ['name', 'token', 'link', 'event']


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'token', 'file', 'event']


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'token', 'event']


class AlbumImageForm(forms.ModelForm):
    class Meta:
        model = AlbumImage
        fields = ['img', 'album']


class PollForm(forms.ModelForm):
    s_date = forms.DateField(initial=datetime.date.today)
    e_date = forms.DateField(initial=datetime.date.today)
    class Meta:
        model = Poll
        fields = ['name', 'context', 's_date', 'e_date', 'event']


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['name', 'context', 'votes', 'poll']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'context', 'event']


