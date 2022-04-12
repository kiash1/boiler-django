from django.db import models
from django.utils import timezone
from apps.base.utils import generate_random_key


class AuthToken(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    user = models.ForeignKey('auth.user', related_name='auth_token', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.key:
            self.key = generate_random_key()
        if not self.created_at:
            self.created_at = timezone.now()

        super(AuthToken, self).save(*args, **kwargs)