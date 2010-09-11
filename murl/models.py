from django.db import models,IntegrityError
from django.contrib.auth.models import User

from datetime import datetime

class MUrl(models.Model):
    murl = models.SlugField(unique=True)
    url = models.URLField(verify_exists=False)
    publication = models.DateTimeField(default=datetime.now())
    clicks = models.IntegerField(default=0)
    owner = models.ForeignKey(User)

    def click(self, commit = False):
        self.clicks += 1
        if commit:
            self.save()

    class Meta:
        ordering = ['-publication']
