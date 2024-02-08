from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment
from .models import RecipeRating
from .models import RecipePost




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
        print(f"Cleaned Rating: {reciperating}")
        if not 1 <= reciperating <= 10:
            raise forms.ValidationError('Rating must be between 1 and 10.')
        return reciperating

class RecipePostForm(forms.ModelForm):
    existing_image_public_id = forms.CharField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = RecipePost
        fields = ['title', 'excerpt', 'ingredients', 'instructions', 'meal_type', 'effort', 'food_image', 'image_alt']
        widgets = {
            'ingredients': SummernoteWidget(),
            'instructions': SummernoteWidget(),
        }

