from django.forms import ModelForm
from main.models import ReviewEntry

class ReviewForm(ModelForm):
    class Meta:
        model = ReviewEntry
        fields = ["name", "review", "rating"]