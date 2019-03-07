from django.contrib import admin
from django import forms
from .models import Event, CheckIn, Url, File, Album, AlbumImage, Poll, Choice, Post,ChoiceRecord,Category

class CategoryAdminForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = ['name', 'editer','viewer']
    
admin.site.register(Category, CategoryAdmin)

class EventAdminForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'


class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm
    list_display = ['name', 'token', 'created', 'last_updated', 'date', 'checkcode']

admin.site.register(Event, EventAdmin)


class CheckInAdminForm(forms.ModelForm):

    class Meta:
        model = CheckIn
        fields = '__all__'


class CheckInAdmin(admin.ModelAdmin):
    form = CheckInAdminForm
    list_display = ['token', 'created', 'last_updated', 'nid']


admin.site.register(CheckIn, CheckInAdmin)


class UrlAdminForm(forms.ModelForm):

    class Meta:
        model = Url
        fields = '__all__'


class UrlAdmin(admin.ModelAdmin):
    form = UrlAdminForm
    list_display = ['name', 'token', 'created', 'last_updated', 'link']


admin.site.register(Url, UrlAdmin)


class FileAdminForm(forms.ModelForm):

    class Meta:
        model = File
        fields = '__all__'


class FileAdmin(admin.ModelAdmin):
    form = FileAdminForm
    list_display = ['name', 'token', 'created', 'last_updated', 'file']


admin.site.register(File, FileAdmin)


class AlbumAdminForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = '__all__'


class AlbumAdmin(admin.ModelAdmin):
    form = AlbumAdminForm
    list_display = ['name', 'token', 'created', 'last_updated']


admin.site.register(Album, AlbumAdmin)


class AlbumImageAdminForm(forms.ModelForm):

    class Meta:
        model = AlbumImage
        fields = '__all__'


class AlbumImageAdmin(admin.ModelAdmin):
    form = AlbumImageAdminForm
    list_display = ['token', 'created', 'last_updated', 'img']


admin.site.register(AlbumImage, AlbumImageAdmin)


class PollAdminForm(forms.ModelForm):

    class Meta:
        model = Poll
        fields = '__all__'


class PollAdmin(admin.ModelAdmin):
    form = PollAdminForm
    list_display = ['name', 'token', 'created', 'last_updated', 'context', 's_date', 'e_date']


admin.site.register(Poll, PollAdmin)


class ChoiceAdminForm(forms.ModelForm):

    class Meta:
        model = Choice
        fields = '__all__'


class ChoiceAdmin(admin.ModelAdmin):
    form = ChoiceAdminForm
    list_display = ['name', 'token', 'created', 'last_updated']


admin.site.register(Choice, ChoiceAdmin)


class PostAdminForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ['name', 'token', 'created', 'last_updated', 'context']


admin.site.register(Post, PostAdmin)


class ChoiceRecordAdminForm(forms.ModelForm):

    class Meta:
        model = ChoiceRecord
        fields = '__all__'


class ChoiceRecordAdmin(admin.ModelAdmin):
    form = ChoiceRecordAdminForm
    list_display = ['created', 'last_updated']
    readonly_fields = ['created', 'last_updated']

admin.site.register(ChoiceRecord, ChoiceRecordAdmin)


