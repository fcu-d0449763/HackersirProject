from .forms import AlbumForm, AlbumImageForm, CheckInForm, ChoiceForm, \
    EventForm, FileForm, PollForm, PostForm, UrlForm,GroupForm,ChoiceRecordForm,ChoiceFormSet,CategoryForm
from .models import Album, AlbumImage, CheckIn, Choice, Event, File, Poll, \
    Post, Url,ChoiceRecord,Category
from django.contrib.auth.models import Group,User
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.shortcuts import render,get_object_or_404, get_list_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect


# TODO:所有都是登入後才能瀏覽
# TODO:所有與Group有關都要綁 Group 新增、修改、刪除 
# TODO:EventCheckInView
# TODO:EventUrlView
# TODO:EventFileInView
# TODO:EventPollInView
# TODO:除了evertlist 其餘列表都限定admin才能看
# FIXME:POLL重新設計

def index(request):
    return render(request, 'index.html')

class GroupListView(ListView):
    model = Group


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm

    # 新增分類後，轉跳到分類列表
    def get_success_url(self):
        return reverse('club_permissions_list')

class GroupDetailView(DetailView):
    model = Group


class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupForm

    def get_success_url(self):
        return reverse('club_permissions_detail', args=(self.object.pk,))


class CategoryListView(ListView):
    model = Category


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm


class CategoryDetailView(DetailView):
    model = Category


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm






class EventListView(ListView):
    model = Event


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    
    def get_form(self, form_class=None):
        form = super(EventCreateView, self).get_form(form_class)
        #form.fields['category'].queryset = Group.objects.filter(user=self.request.user)
        group = Group.objects.filter(user=self.request.user)
        print(group)
        form.fields['category'].queryset = Category.objects.filter(editer=group)
        return form

# Done:只能新增有那個Group(分類)權限的

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

    ## TODO:打卡流程建議
    ## 如果沒有登入就直接輸入學號
    ## 如果學號跟資料庫的使用者相符
    ## USER = 找到的使用者
    ## 如果學號找不到
    ## NID = 學號 ; user = NULL
    
    # def get_form(self, form_class=None):
    #     if form_class is None:
    #         form_class = self.get_form_class()
    #     form = super(CheckInCreateView, self).get_form(form_class)
    #     # the actual modification of the form
    #     form.instance.user = self.request.user
    #     return form
    def get_form(self, form_class=None):
        form = super(CheckInCreateView, self).get_form(form_class)
        form.fields['user'].queryset = User.objects.filter(username=self.request.user.username)
        return form

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

from django import forms
class PollCreateView(CreateView):
    model = Poll
    form_class = PollForm

    # 將事件鎖定在token，並且不用選取
    def get_form(self, form_class=None):
        form = super(PollCreateView, self).get_form(form_class)
        #form.fields['event'] = forms.ModelChoiceField(queryset=Event.objects.filter(token=self.kwargs['token']), initial=0)
        #form.fields['event'].widget.attrs['readonly'] = True
        form.fields['event'] = forms.ModelChoiceField(queryset=Event.objects.filter(token=self.kwargs['token']), initial=0,widget=forms.Select(attrs={'readonly':'True'}))
        return form



    def get_context_data(self, **kwargs):
        context = super(PollCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = ChoiceFormSet(self.request.POST, instance=self.object)
        else:
            context['formset'] = ChoiceFormSet(instance=self.object)
        #context['formset'] = ChoiceFormSet(queryset=Poll.objects.none())
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        if form.is_valid():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
        return super(PollCreateView, self).form_valid(form)

        #     return HttpResponseRedirect('thanks/')
        # else :
        #     return self.render_to_response(self.get_context_data(form = form))
    # def post(self, request, *args, **kwargs):
    #     formset = ChoiceFormSet(request.POST)
    #     if formset.is_valid():
    #         return self.form_valid(formset)

    # def form_valid(self, formset):
    #     formset.save()
    #     return HttpResponseRedirect('/')

    # def form_invalid(self, formset):
    #     return self.render_to_response(self.get_context_data(formset=formset))

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

class ChoiceRecordListView(ListView):
    model = ChoiceRecord


class ChoiceRecordCreateView(CreateView):
    model = ChoiceRecord
    form_class = ChoiceRecordForm

    # DONE:已經投過就不能再投了

    def get_error_url(self):
        return reverse("club_poll_detail", kwargs={"token": self.kwargs['token']})

    def get(self, request, *args, **kwargs):
        poll = Poll.objects.filter(token=self.kwargs['token']).first()
        user = User.objects.filter(username=self.request.user.username).first()
        choice= Choice.objects.filter(poll=poll)
        if ChoiceRecord.objects.filter(choice=choice,User=user).exists():
            messages.warning(self.request, '已經重複投票')
            return HttpResponseRedirect(self.get_error_url())
        else:
            return super(ChoiceRecordCreateView, self).get(self, request, *args, **kwargs)


    def get_form(self, form_class=None):
        form = super(ChoiceRecordCreateView, self).get_form(form_class)
        form.fields['User'] = forms.ModelChoiceField(queryset=User.objects.filter(username=self.request.user.username), initial=0,widget=forms.Select(attrs={'readonly':'True'}))
        #form.fields['user'].queryset = User.objects.filter(username=self.request.user.username)
        poll = Poll.objects.filter(token=self.kwargs['token']).first()
        form.fields['choice'].queryset = Choice.objects.filter(poll=poll)
        return form

class ChoiceRecordDetailView(DetailView):
    model = ChoiceRecord


class ChoiceRecordUpdateView(UpdateView):
    model = ChoiceRecord
    form_class = ChoiceRecordForm