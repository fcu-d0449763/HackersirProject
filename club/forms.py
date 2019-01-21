from django import forms
from .models import (
    Event,
    CheckIn,
    Url,
    File,
    Album,
    AlbumImage,
    Poll,
    Choice,
    Post,
    ChoiceRecord,
    Category,
)
from django.contrib.auth.models import Group, User
import datetime
import random, string
from django.forms.models import inlineformset_factory
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import User, Group,Permission


# 管理員 先編輯 權限名單 再去新增分類
class GroupForm(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        widget=FilteredSelectMultiple("permissions", is_stacked=False),
        queryset=Permission.objects.all(),
        help_text='此為權限列表，可直接修改model的權限'
    )
    users = forms.ModelMultipleChoiceField(
        widget=FilteredSelectMultiple("users", is_stacked=False),
        queryset=User.objects.all(),
        help_text='此為名單'
    )
    class Meta:
        model = Group
        fields = ["name", "permissions"]
        css = {"all": ("/static/admin/css/widgets.css",)}
        js = ("/admin/jsi18n",)
        help_texts = {
            "name": "請在此輸入權限名單名稱"
        }



    def __init__(self, *args, **kwargs):
        if kwargs.get("instance"):
            initial = kwargs.setdefault("initial", {})
            initial["users"] = [t.pk for t in kwargs["instance"].user_set.all()]
        forms.ModelForm.__init__(self, *args, **kwargs)

    def save(self):
        instance = forms.ModelForm.save(self)
        instance.user_set.clear()
        instance.user_set.add(*self.cleaned_data["users"])
        return instance


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "editer", "viewer"]


class EventForm(forms.ModelForm):
    code = "".join(random.choice(string.digits) for x in range(5))
    date = forms.DateField(initial=datetime.date.today)
    checkcode = forms.CharField(initial=code)

    class Meta:
        model = Event
        fields = ["category", "name", "date", "checkcode"]


class CheckInForm(forms.ModelForm):
    class Meta:
        model = CheckIn
        fields = ["nid", "user", "event"]


class UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ["event","name", "link"]


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ["name", "file", "event"]


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["name", "event"]


class AlbumImageForm(forms.ModelForm):
    class Meta:
        model = AlbumImage
        fields = ["img", "album"]


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ["name", "poll"]


# 新增投票選項


class PollForm(forms.ModelForm):
    s_date = forms.DateField(initial=datetime.date.today)
    e_date = forms.DateField(initial=datetime.date.today)

    class Meta:
        model = Poll
        fields = ["event", "name", "context", "s_date", "e_date"]


# 新增投票

ChoiceFormSet = inlineformset_factory(
    parent_model=Poll,
    model=Choice,
    form=ChoiceForm,
    can_delete=False,
    extra=1,
    max_num=1000,
)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["name", "event", "context"]


# event
class ChoiceRecordForm(forms.ModelForm):
    class Meta:
        model = ChoiceRecord
        fields = ["User", "choice"]

