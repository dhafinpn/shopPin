from django.db import models
import uuid

class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    name = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    review = models.TextField()
    rating = models.IntegerField()

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5
