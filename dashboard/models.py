from django.db import models
from django.contrib.auth.models import User



class SharingModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    write = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {str(self.read)} - {str(self.write)}'

class NoteModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False, blank=False)
    notes = models.TextField(null=False, blank=False)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.owner.username}'