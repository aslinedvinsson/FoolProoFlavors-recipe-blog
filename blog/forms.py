from django import forms
from .models import Comment
from .models import RecipeRating


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class RatingForm(forms.ModelForm):
    class Meta:
        model = RecipeRating
        fields = ['reciperating']
    def clean_reciperating(self):
        reciperating = self.cleaned_data.get('reciperating')
        if not 1 <= reciperating <= 10:
            raise forms.ValidationError('Rating must be between 1 and 10.')
        return reciperating

