from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models 
from django.contrib.auth.models import User, Group
import uuid

class Event(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    token = models.UUIDField(db_index=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    date = models.DateField()
    checkcode = models.CharField(max_length=5)

    # Relationship Fields
    category = models.ForeignKey(
        Group,
        on_delete=models.CASCADE, related_name="groups"
    )

    class Meta:
        ordering = ('category','date',)

    def __str__(self):
        return u'%s %s-%s' % (self.date,self.category,self.name)

    def get_absolute_url(self):
        return reverse('club_event_detail', args=(self.token,))


    def get_update_url(self):
        return reverse('club_event_update', args=(self.token,))


class CheckIn(models.Model):

    # Fields
    token = models.UUIDField(db_index=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    nid = models.CharField(max_length=30,null=True,blank=True)

    # Relationship Fields
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE, related_name="users", null=True
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE, related_name="checkin_events"
    )

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return u'%s' % self.user.get_username()

    def get_absolute_url(self):
        return reverse('club_checkin_detail', args=(self.token,))


    def get_update_url(self):
        return reverse('club_checkin_update', args=(self.token,))


class Url(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    token = models.UUIDField(db_index=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    link = models.URLField()

    # Relationship Fields
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE, related_name="url_events"
    )

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('club_url_detail', args=(self.token,))


    def get_update_url(self):
        return reverse('club_url_update', args=(self.token,))


class File(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    token = models.UUIDField(db_index=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    file = models.FileField(upload_to="upload/files/")

    # Relationship Fields
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE, related_name="file_events"
    )

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('club_file_detail', args=(self.token,))


    def get_update_url(self):
        return reverse('club_file_update', args=(self.token,))


class Album(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    token = models.UUIDField(db_index=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE, related_name="album_events"
    )

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('club_album_detail', args=(self.token,))


    def get_update_url(self):
        return reverse('club_album_update', args=(self.token,))


class AlbumImage(models.Model):

    # Fields
    token = models.UUIDField(db_index=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    img = models.ImageField(upload_to="upload/images/")

    # Relationship Fields
    album = models.ForeignKey(
        'club.Album',
        on_delete=models.CASCADE, related_name="albums"
    )

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('club_albumimage_detail', args=(self.token,))


    def get_update_url(self):
        return reverse('club_albumimage_update', args=(self.token,))


class Poll(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    token = models.UUIDField(db_index=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    context = models.TextField(max_length=100)
    s_date = models.DateTimeField()
    e_date = models.DateTimeField()

    # Relationship Fields
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE, related_name="poll_events"
    )

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('club_poll_detail', args=(self.token,))


    def get_update_url(self):
        return reverse('club_poll_update', args=(self.token,))


class Choice(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    token = models.UUIDField(db_index=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    context = models.TextField(max_length=100)
    votes = models.IntegerField(default=0)

    # Relationship Fields
    poll = models.ForeignKey(
        'club.Poll',
        on_delete=models.CASCADE, related_name="polls"
    )

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('club_choice_detail', args=(self.token,))


    def get_update_url(self):
        return reverse('club_choice_update', args=(self.token,))


class Post(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    token = models.UUIDField(db_index=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    context = models.TextField(max_length=100)

    # Relationship Fields
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE, related_name="post_events", null=True
    )

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('club_post_detail', args=(self.token,))


    def get_update_url(self):
        return reverse('club_post_update', args=(self.token,))


