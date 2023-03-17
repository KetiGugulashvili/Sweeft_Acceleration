from django.db import models
from django.utils import timezone
from random import choice
from string import ascii_letters, digits


class Url(models.Model):
    long_url = models.URLField(max_length=250)
    shortened_part = models.CharField(max_length=7, unique=True, blank=True)
    time_of_creation = models.DateTimeField(auto_now_add=True)
    times_accessed = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.long_url} to {self.shortened_part}'

    def save(self, *args, **kwargs):
        if not self.shortened_part:
            available_chars = ascii_letters + digits

            def create_shortened_url():
                random_code = "".join([choice(available_chars) for _ in range(7)])
                if Url.objects.filter(shortened_part=random_code).exists():
                    return create_shortened_url()
                return random_code
            self.shortened_part = create_shortened_url()

        super().save(*args, **kwargs)


    """Needs scheduler (celery, APScheduler etc) for everyday automatic checking and deletion"""
    @staticmethod
    def delete_old_urls():
        old = Url.objects.filter(time_of_creation__lt=timezone.now()-timezone.timedelta(days=30))
        old.delete()
