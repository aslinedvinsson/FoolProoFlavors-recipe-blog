from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment
from .models import RecipeRating
from .models import RecipePost
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field


# Code CommentForm inspired by CodeInstitute Walkthrough 'I think, therefor I
# blog'
class CommentForm(forms.ModelForm):
    """
    Form for submitting comments with a customizable textarea. Initializes with
    a textarea for the 'body' field, setting a placeholder. Utilizes crispy
    forms for layout customization.

    Attributes:
    - body: CharField with a Textarea widget for comment input.

    Meta:
    - model: The Comment model this form is associated with.
    - fields: Tuple specifying the 'body' field to be included in the form.
    """
    body = forms.CharField(label='', required=False, widget=forms.Textarea(
        attrs={'placeholder': 'Enter your comment here...'}))
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Field('body',),)
    class Meta:
        model = Comment
        fields = ('body',)


class RatingForm(forms.ModelForm):
    """
    Form for submitting ratings for recipes, with validation for rating values.

    Initializes with a number input for 'reciperating', enforcing a rating
    scale of 1 to 10. Includes custom validation to ensure the rating falls
    within the specified range.

    Attributes:
    - reciperating: IntegerField with a NumberInput widget, placeholder
    indicating the rating scale.

    Meta:
    - model: RecipeRating model this form is associated with.
    - fields: List containing 'reciperating' to specify the included field.
    """
    reciperating = forms.IntegerField(label='', required=True,
    widget=forms.NumberInput(attrs={'placeholder': 'Rate 1 to 10'}))

    def __init__(self, *args, **kwargs):
        super(RatingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Field('reciperating', type='number', min=1, max=10),)

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
    """
    Form for creating or updating RecipePost entries with enhanced text fields.

    Incorporates Summernote widgets for 'ingredients' and 'instructions'
    fields to provide rich text editing features. Includes an optional hidden
    field for managing the ID of an existing cloud-hosted image.

    Meta:
    - model: RecipePost, the model to which the form is linked.
    - fields: List of fields included in the form, including text, choice, and
    image fields with specific widgets for rich text fields.
    """
    existing_image_public_id = forms.CharField(widget=forms.HiddenInput,
    required=False)

    class Meta:
        model = RecipePost
        fields = ['title', 'excerpt', 'ingredients', 'instructions',
        'meal_type', 'effort', 'food_image', 'image_alt']
        widgets = {
            'ingredients': SummernoteWidget(),
            'instructions': SummernoteWidget(),
        }

