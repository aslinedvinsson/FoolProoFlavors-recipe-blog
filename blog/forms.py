from django import forms
from .models import Comment
from .models import RecipeRating
from .models import RecipePost
from PIL import Image



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

"""

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
"""

class RecipePostForm(forms.ModelForm):
    existing_image_public_id = forms.CharField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = RecipePost
        fields = ['title', 'excerpt', 'ingredients', 'instructions', 'meal_type', 'effort', 'food_image', 'image_alt']

    def save(self, commit=True):
        instance = super().save(commit=False)
        existing_image_public_id = self.cleaned_data.get('existing_image_public_id')
        if existing_image_public_id:
            instance.food_image = existing_image_public_id
        if 'food_image' in self.changed_data:  # Check if food_image is being updated
            image = instance.food_image
            with Image.open(image.path) as img:
                # Resize the image
                img.thumbnail((500, 500))
                img.save(image.path)
        if commit:
            instance.save()
        return instance

    #def __init__(self, *args, **kwargs):
     #   super(RecipePostForm, self).__init__(*args, **kwargs)