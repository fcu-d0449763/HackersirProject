from .forms import AlbumForm, AlbumImageForm, CheckInForm, ChoiceForm, \
    EventForm, FileForm, PollForm, PostForm, UrlForm,GroupForm
from .models import Album, AlbumImage, CheckIn, Choice, Event, File, Poll, \
    Post, Url
from django.contrib.auth.models import Group
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.shortcuts import render,get_object_or_404, get_list_or_404, redirect
from django.urls import reverse


def index(request):
    return render(request, 'index.html')

class GroupListView(ListView):
    model = Group


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm

    # 新增分類後，轉跳到分類列表
    def get_success_url(self):
        return reverse('club_category_list')

class GroupDetailView(DetailView):
    model = Group


class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupForm

    def get_success_url(self):
        return reverse('club_category_detail', args=(self.object.pk,))

class EventListView(ListView):
    model = Event


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm


class EventDetailView(DetailView):
    model = Event

    def get_object(self):
        return Event.objects.filter(token=self.kwargs['token']).first()

class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm

    def get_object(self):
        return Event.objects.filter(token=self.kwargs['token']).first()

class CheckInListView(ListView):
    model = CheckIn


class CheckInCreateView(CreateView):
    model = CheckIn
    form_class = CheckInForm

    ## 如果沒有登入就直接輸入學號
    ## 如果學號跟資料庫的使用者相符
    ## USER = 找到的使用者
    ## 如果學號找不到
    ## NID = 學號 ; user = NULL
    


class CheckInDetailView(DetailView):
    model = CheckIn

    def get_object(self):
        return CheckIn.objects.filter(token=self.kwargs['token']).first()

class CheckInUpdateView(UpdateView):
    model = CheckIn
    form_class = CheckInForm

    def get_object(self):
        return CheckIn.objects.filter(token=self.kwargs['token']).first()

class UrlListView(ListView):
    model = Url


class UrlCreateView(CreateView):
    model = Url
    form_class = UrlForm


class UrlDetailView(DetailView):
    model = Url

    def get_object(self):
        return Url.objects.filter(token=self.kwargs['token']).first()

class UrlUpdateView(UpdateView):
    model = Url
    form_class = UrlForm

    def get_object(self):
        return Url.objects.filter(token=self.kwargs['token']).first()

class FileListView(ListView):
    model = File


class FileCreateView(CreateView):
    model = File
    form_class = FileForm


class FileDetailView(DetailView):
    model = File

    def get_object(self):
        return File.objects.filter(token=self.kwargs['token']).first()

class FileUpdateView(UpdateView):
    model = File
    form_class = FileForm

    def get_object(self):
        return File.objects.filter(token=self.kwargs['token']).first()

class AlbumListView(ListView):
    model = Album


class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm


class AlbumDetailView(DetailView):
    model = Album

    def get_object(self):
        return Album.objects.filter(token=self.kwargs['token']).first()

class AlbumUpdateView(UpdateView):
    model = Album
    form_class = AlbumForm

    def get_object(self):
        return Album.objects.filter(token=self.kwargs['token']).first()

class AlbumImageListView(ListView):
    model = AlbumImage


class AlbumImageCreateView(CreateView):
    model = AlbumImage
    form_class = AlbumImageForm


class AlbumImageDetailView(DetailView):
    model = AlbumImage

    def get_object(self):
        return AlbumImage.objects.filter(token=self.kwargs['token']).first()

class AlbumImageUpdateView(UpdateView):
    model = AlbumImage
    form_class = AlbumImageForm

    def get_object(self):
        return AlbumImage.objects.filter(token=self.kwargs['token']).first()

class PollListView(ListView):
    model = Poll


class PollCreateView(CreateView):
    model = Poll
    form_class = PollForm


class PollDetailView(DetailView):
    model = Poll

    def get_object(self):
        return Poll.objects.filter(token=self.kwargs['token']).first()

class PollUpdateView(UpdateView):
    model = Poll
    form_class = PollForm

    def get_object(self):
        return Poll.objects.filter(token=self.kwargs['token']).first()

class ChoiceListView(ListView):
    model = Choice


class ChoiceCreateView(CreateView):
    model = Choice
    form_class = ChoiceForm


class ChoiceDetailView(DetailView):
    model = Choice

    def get_object(self):
        return Choice.objects.filter(token=self.kwargs['token']).first()

class ChoiceUpdateView(UpdateView):
    model = Choice
    form_class = ChoiceForm

    def get_object(self):
        return Choice.objects.filter(token=self.kwargs['token']).first()

class PostListView(ListView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm


class PostDetailView(DetailView):
    model = Post

    def get_object(self):
        return Post.objects.filter(token=self.kwargs['token']).first()

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm

    def get_object(self):
        return Post.objects.filter(token=self.kwargs['token']).first()
