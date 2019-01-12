from django.conf.urls import url, include
# from rest_framework import routers

# from . import api
from . import views


# router = routers.DefaultRouter()
# router.register(r'event', api.EventViewSet)
# router.register(r'checkin', api.CheckInViewSet)
# router.register(r'url', api.UrlViewSet)
# router.register(r'file', api.FileViewSet)
# router.register(r'album', api.AlbumViewSet)
# router.register(r'albumimage', api.AlbumImageViewSet)
# router.register(r'poll', api.PollViewSet)
# router.register(r'choice', api.ChoiceViewSet)
# router.register(r'post', api.PostViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    # url(r'^api/v1/', include(router.urls)),
    url(r'^$', views.index , name='index'),
)

urlpatterns += (
    # urls for Group(Category)
    url(r'^club/category/$', views.GroupListView.as_view(), name='club_category_list'),
    url(r'^club/category/create/$', views.GroupCreateView.as_view(), name='club_category_create'),
    url(r'^club/category/detail/(?P<pk>\S+)/$', views.GroupDetailView.as_view(), name='club_category_detail'),
    url(r'^club/category/update/(?P<pk>\S+)/$', views.GroupUpdateView.as_view(), name='club_category_update'),
)

urlpatterns += (
    # urls for Event
    url(r'^club/event/$', views.EventListView.as_view(), name='club_event_list'),
    url(r'^club/event/create/$', views.EventCreateView.as_view(), name='club_event_create'),
    url(r'^club/event/detail/(?P<token>[0-9a-f-]+)/$', views.EventDetailView.as_view(), name='club_event_detail'),
    url(r'^club/event/update/(?P<token>[0-9a-f-]+)/$', views.EventUpdateView.as_view(), name='club_event_update'),
)

urlpatterns += (
    # urls for CheckIn
    url(r'^club/checkin/$', views.CheckInListView.as_view(), name='club_checkin_list'),
    url(r'^club/checkin/create/$', views.CheckInCreateView.as_view(), name='club_checkin_create'),
    url(r'^club/checkin/detail/(?P<token>[0-9a-f-]+)/$', views.CheckInDetailView.as_view(), name='club_checkin_detail'),
    url(r'^club/checkin/update/(?P<token>[0-9a-f-]+)/$', views.CheckInUpdateView.as_view(), name='club_checkin_update'),
)

urlpatterns += (
    # urls for Url
    url(r'^club/url/$', views.UrlListView.as_view(), name='club_url_list'),
    url(r'^club/url/create/$', views.UrlCreateView.as_view(), name='club_url_create'),
    url(r'^club/url/detail/(?P<token>[0-9a-f-]+)/$', views.UrlDetailView.as_view(), name='club_url_detail'),
    url(r'^club/url/update/(?P<token>[0-9a-f-]+)/$', views.UrlUpdateView.as_view(), name='club_url_update'),
)

urlpatterns += (
    # urls for File
    url(r'^club/file/$', views.FileListView.as_view(), name='club_file_list'),
    url(r'^club/file/create/$', views.FileCreateView.as_view(), name='club_file_create'),
    url(r'^club/file/detail/(?P<token>[0-9a-f-]+)/$', views.FileDetailView.as_view(), name='club_file_detail'),
    url(r'^club/file/update/(?P<token>[0-9a-f-]+)/$', views.FileUpdateView.as_view(), name='club_file_update'),
)

urlpatterns += (
    # urls for Album
    url(r'^club/album/$', views.AlbumListView.as_view(), name='club_album_list'),
    url(r'^club/album/create/$', views.AlbumCreateView.as_view(), name='club_album_create'),
    url(r'^club/album/detail/(?P<token>[0-9a-f-]+)/$', views.AlbumDetailView.as_view(), name='club_album_detail'),
    url(r'^club/album/update/(?P<token>[0-9a-f-]+)/$', views.AlbumUpdateView.as_view(), name='club_album_update'),
)

urlpatterns += (
    # urls for AlbumImage
    url(r'^club/albumimage/$', views.AlbumImageListView.as_view(), name='club_albumimage_list'),
    url(r'^club/albumimage/create/$', views.AlbumImageCreateView.as_view(), name='club_albumimage_create'),
    url(r'^club/albumimage/detail/(?P<token>[0-9a-f-]+)/$', views.AlbumImageDetailView.as_view(), name='club_albumimage_detail'),
    url(r'^club/albumimage/update/(?P<token>[0-9a-f-]+)/$', views.AlbumImageUpdateView.as_view(), name='club_albumimage_update'),
)

urlpatterns += (
    # urls for Poll
    url(r'^club/poll/$', views.PollListView.as_view(), name='club_poll_list'),
    url(r'^club/poll/create/$', views.PollCreateView.as_view(), name='club_poll_create'),
    url(r'^club/poll/detail/(?P<token>[0-9a-f-]+)/$', views.PollDetailView.as_view(), name='club_poll_detail'),
    url(r'^club/poll/update/(?P<token>[0-9a-f-]+)/$', views.PollUpdateView.as_view(), name='club_poll_update'),
)

urlpatterns += (
    # urls for Choice
    url(r'^club/choice/$', views.ChoiceListView.as_view(), name='club_choice_list'),
    url(r'^club/choice/create/$', views.ChoiceCreateView.as_view(), name='club_choice_create'),
    url(r'^club/choice/detail/(?P<token>[0-9a-f-]+)/$', views.ChoiceDetailView.as_view(), name='club_choice_detail'),
    url(r'^club/choice/update/(?P<token>[0-9a-f-]+)/$', views.ChoiceUpdateView.as_view(), name='club_choice_update'),
)

urlpatterns += (
    # urls for Post
    url(r'^club/post/$', views.PostListView.as_view(), name='club_post_list'),
    url(r'^club/post/create/$', views.PostCreateView.as_view(), name='club_post_create'),
    url(r'^club/post/detail/(?P<token>[0-9a-f-]+)/$', views.PostDetailView.as_view(), name='club_post_detail'),
    url(r'^club/post/update/(?P<token>[0-9a-f-]+)/$', views.PostUpdateView.as_view(), name='club_post_update'),
)

