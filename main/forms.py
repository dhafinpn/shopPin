from django.forms import ModelForm
from main.models import ReviewEntry
from django.utils.html import strip_tags

class ReviewForm(ModelForm):
    class Meta:
        model = ReviewEntry
        fields = ["name", "review", "rating"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_review(self):
        review = self.cleaned_data["review"]
        return strip_tags(review)