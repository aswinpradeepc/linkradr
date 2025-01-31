from django.db import models
from django.conf import settings
import string
import random
from django.utils import timezone

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

class URLShortener(models.Model):
    actual_url = models.URLField()
    shortened_url = models.CharField(max_length=15, unique=True,  db_index=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, related_name='shortened_urls')
    created_at = models.DateTimeField(default=timezone.now)
    click_count = models.PositiveIntegerField(default=0)
    last_accessed = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "URL Shorteners"
        unique_together = ('actual_url', 'user')

    def increment_clicks(self):
        self.click_count += 1
        self.last_accessed = timezone.now()
        self.save()

    def save(self, *args, **kwargs):
        if not self.shortened_url:
            self.shortened_url = generate_short_url()
            while URLShortener.objects.filter(shortened_url=self.shortened_url).exists():
                self.shortened_url = generate_short_url()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.shortened_url} -> {self.actual_url}'