# Generated by Django 4.2.9 on 2024-02-15 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_recipepost_food_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipepost',
            name='effort',
            field=models.CharField(choices=[('bad_day_comfort_food', 'Bad day comfort food'), ('trying_a_healthy_day', 'Trying a healthy day'), ('im_in_a_hurry', "I'm in a hurry"), ('i_have_time_but_no_brains', 'I have time but no brains'), ('too_far_until_payday', 'Too far until payday')], default='Bad day comfort food', max_length=50),
        ),
        migrations.AlterField(
            model_name='recipepost',
            name='meal_type',
            field=models.CharField(choices=[('chicken', 'Chicken'), ('fish', 'Fish'), ('meat', 'Meat'), ('vegetarian', 'Vegetarian'), ('vegan', 'Vegan'), ('pasta', 'Pasta'), ('seafood', 'Seafood'), ('salad', 'Salad'), ('soup', 'Soup'), ('sandwich', 'Sandwich'), ('breakfast', 'Breakfast'), ('dessert', 'Dessert')], default='Vegan', max_length=50),
        ),
    ]