from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    """
    Form for creating and updating reviews
    """
    class Meta:
        model = Review
        fields = ['rating', 'title', 'comment']
        widgets = {
            'rating': forms.RadioSelect(choices=[(i, i) for i in range(1, 6)]),
            'comment': forms.Textarea(attrs={'rows': 4}),
        } 