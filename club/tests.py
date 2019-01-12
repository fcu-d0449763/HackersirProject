import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Event, CheckIn, Url, File, Album, AlbumImage, Poll, Choice, Post
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_event(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["token"] = "token"
    defaults["checkcode"] = "checkcode"
    defaults.update(**kwargs)
    if "category" not in defaults:
        defaults["category"] = create_django_contrib_auth_models_group()
    return Event.objects.create(**defaults)


def create_checkin(**kwargs):
    defaults = {}
    defaults["token"] = "token"
    defaults["nid"] = "nid"
    defaults.update(**kwargs)
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    if "event" not in defaults:
        defaults["event"] = create_event()
    return CheckIn.objects.create(**defaults)


def create_url(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["token"] = "token"
    defaults["link"] = "link"
    defaults.update(**kwargs)
    if "event" not in defaults:
        defaults["event"] = create_event()
    return Url.objects.create(**defaults)


def create_file(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["token"] = "token"
    defaults["file"] = "file"
    defaults.update(**kwargs)
    if "event" not in defaults:
        defaults["event"] = create_event()
    return File.objects.create(**defaults)


def create_album(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["token"] = "token"
    defaults.update(**kwargs)
    if "event" not in defaults:
        defaults["event"] = create_event()
    return Album.objects.create(**defaults)


def create_albumimage(**kwargs):
    defaults = {}
    defaults["img"] = "img"
    defaults.update(**kwargs)
    if "album" not in defaults:
        defaults["album"] = create_album()
    return AlbumImage.objects.create(**defaults)


def create_poll(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["context"] = "context"
    defaults["s_date"] = "s_date"
    defaults["e_date"] = "e_date"
    defaults.update(**kwargs)
    if "event" not in defaults:
        defaults["event"] = create_event()
    return Poll.objects.create(**defaults)


def create_choice(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["context"] = "context"
    defaults["votes"] = "votes"
    defaults.update(**kwargs)
    if "poll" not in defaults:
        defaults["poll"] = create_poll()
    return Choice.objects.create(**defaults)


def create_post(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["context"] = "context"
    defaults.update(**kwargs)
    if "event" not in defaults:
        defaults["event"] = create_event()
    return Post.objects.create(**defaults)


class EventViewTest(unittest.TestCase):
    '''
    Tests for Event
    '''
    def setUp(self):
        self.client = Client()

    def test_list_event(self):
        url = reverse('club_event_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_event(self):
        url = reverse('club_event_create')
        data = {
            "name": "name",
            "token": "token",
            "checkcode": "checkcode",
            "category": create_django_contrib_auth_models_group().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_event(self):
        event = create_event()
        url = reverse('club_event_detail', args=[event.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_event(self):
        event = create_event()
        data = {
            "name": "name",
            "token": "token",
            "checkcode": "checkcode",
            "category": create_django_contrib_auth_models_group().pk,
        }
        url = reverse('club_event_update', args=[event.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CheckInViewTest(unittest.TestCase):
    '''
    Tests for CheckIn
    '''
    def setUp(self):
        self.client = Client()

    def test_list_checkin(self):
        url = reverse('club_checkin_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_checkin(self):
        url = reverse('club_checkin_create')
        data = {
            "token": "token",
            "nid": "nid",
            "user": create_django_contrib_auth_models_user().pk,
            "event": create_event().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_checkin(self):
        checkin = create_checkin()
        url = reverse('club_checkin_detail', args=[checkin.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_checkin(self):
        checkin = create_checkin()
        data = {
            "token": "token",
            "nid": "nid",
            "user": create_django_contrib_auth_models_user().pk,
            "event": create_event().pk,
        }
        url = reverse('club_checkin_update', args=[checkin.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class UrlViewTest(unittest.TestCase):
    '''
    Tests for Url
    '''
    def setUp(self):
        self.client = Client()

    def test_list_url(self):
        url = reverse('club_url_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_url(self):
        url = reverse('club_url_create')
        data = {
            "name": "name",
            "token": "token",
            "link": "link",
            "event": create_event().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_url(self):
        url = create_url()
        url = reverse('club_url_detail', args=[url.token,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_url(self):
        url = create_url()
        data = {
            "name": "name",
            "token": "token",
            "link": "link",
            "event": create_event().pk,
        }
        url = reverse('club_url_update', args=[url.token,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class FileViewTest(unittest.TestCase):
    '''
    Tests for File
    '''
    def setUp(self):
        self.client = Client()

    def test_list_file(self):
        url = reverse('club_file_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_file(self):
        url = reverse('club_file_create')
        data = {
            "name": "name",
            "token": "token",
            "file": "file",
            "event": create_event().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_file(self):
        file = create_file()
        url = reverse('club_file_detail', args=[file.token,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_file(self):
        file = create_file()
        data = {
            "name": "name",
            "token": "token",
            "file": "file",
            "event": create_event().pk,
        }
        url = reverse('club_file_update', args=[file.token,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class AlbumViewTest(unittest.TestCase):
    '''
    Tests for Album
    '''
    def setUp(self):
        self.client = Client()

    def test_list_album(self):
        url = reverse('club_album_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_album(self):
        url = reverse('club_album_create')
        data = {
            "name": "name",
            "token": "token",
            "event": create_event().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_album(self):
        album = create_album()
        url = reverse('club_album_detail', args=[album.token,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_album(self):
        album = create_album()
        data = {
            "name": "name",
            "token": "token",
            "event": create_event().pk,
        }
        url = reverse('club_album_update', args=[album.token,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class AlbumImageViewTest(unittest.TestCase):
    '''
    Tests for AlbumImage
    '''
    def setUp(self):
        self.client = Client()

    def test_list_albumimage(self):
        url = reverse('club_albumimage_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_albumimage(self):
        url = reverse('club_albumimage_create')
        data = {
            "img": "img",
            "album": create_album().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_albumimage(self):
        albumimage = create_albumimage()
        url = reverse('club_albumimage_detail', args=[albumimage.token,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_albumimage(self):
        albumimage = create_albumimage()
        data = {
            "img": "img",
            "album": create_album().pk,
        }
        url = reverse('club_albumimage_update', args=[albumimage.token,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class PollViewTest(unittest.TestCase):
    '''
    Tests for Poll
    '''
    def setUp(self):
        self.client = Client()

    def test_list_poll(self):
        url = reverse('club_poll_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_poll(self):
        url = reverse('club_poll_create')
        data = {
            "name": "name",
            "context": "context",
            "s_date": "s_date",
            "e_date": "e_date",
            "event": create_event().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_poll(self):
        poll = create_poll()
        url = reverse('club_poll_detail', args=[poll.token,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_poll(self):
        poll = create_poll()
        data = {
            "name": "name",
            "context": "context",
            "s_date": "s_date",
            "e_date": "e_date",
            "event": create_event().pk,
        }
        url = reverse('club_poll_update', args=[poll.token,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ChoiceViewTest(unittest.TestCase):
    '''
    Tests for Choice
    '''
    def setUp(self):
        self.client = Client()

    def test_list_choice(self):
        url = reverse('club_choice_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_choice(self):
        url = reverse('club_choice_create')
        data = {
            "name": "name",
            "context": "context",
            "votes": "votes",
            "poll": create_poll().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_choice(self):
        choice = create_choice()
        url = reverse('club_choice_detail', args=[choice.token,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_choice(self):
        choice = create_choice()
        data = {
            "name": "name",
            "context": "context",
            "votes": "votes",
            "poll": create_poll().pk,
        }
        url = reverse('club_choice_update', args=[choice.token,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class PostViewTest(unittest.TestCase):
    '''
    Tests for Post
    '''
    def setUp(self):
        self.client = Client()

    def test_list_post(self):
        url = reverse('club_post_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_post(self):
        url = reverse('club_post_create')
        data = {
            "name": "name",
            "context": "context",
            "event": create_event().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_post(self):
        post = create_post()
        url = reverse('club_post_detail', args=[post.token,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_post(self):
        post = create_post()
        data = {
            "name": "name",
            "context": "context",
            "event": create_event().pk,
        }
        url = reverse('club_post_update', args=[post.token,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


