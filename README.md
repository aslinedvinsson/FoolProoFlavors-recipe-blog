# FoolProoFlavors

# FoolProoFlavors: Easy-to-Follow Recipes to Rescue Your Dinner Routine on Bored Days
Foolprooflavors is a recipe blog, for recipes that actually are used and cooked. The blog presents en uppsjö av recipes contributed by fellow lazy people. The users can create an account and when logged in, they can post, edit and delete recipes. The users can also comment on their own and others recipes and rate other's recipes. The recipes should include ingredients, instructions, mealtype, effort and an image. The admin approves the recipeposts and comments before publishing. The users can read about the community behind the recipe idea and contact the admin through a message form and the message is saved in the database.

***/// bild av am i responsive

The live link can be found here - [Foolprooflavors](https://foolproflavorsrecipeapp-92d4f04278dd.herokuapp.com/)

## Table of Contents////

- [FoolProoFlavors](#foolprooflavors)
  * [User Experience (UX)](#user-experience-ux)
    + [User Stories](#user-stories)
    + [Design](#design)
      - [Colour Scheme](#colour-scheme)
      - [Imagery](#imagery)
      - [Fonts](#fonts)
      - [Wireframes](#wireframes)
  * [Agile Methodology](#agile-methodology)
  * [Data Model](#data-model)
  * [Testing](#testing)
  * [Security Features and Defensive Design](#security-features-and-defensive-design)
    + [User Authentication](#user-authentication)
    + [Form Validation](#form-validation)
    + [Database Security](#database-security)
    + [Custom error pages:](#custom-error-pages-)
  * [Features](#features)
    + [Header](#header)
    + [Footer](#footer)
    + [Home Page](#home-page)
    + [Recipe Detail Page](#recipe-detail-page)
    + [Add Recipe Form](#add-recipe-form)
    + [Update Recipe Form](#update-recipe-form)
    + [Delete Recipe](#delete-recipe)
    + [Error Pages](#error-pages)
    + [Future Features](#future-features)
  * [Deployment - Heroku](#deployment---heroku)
  * [Languages](#languages)
  * [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
  * [Credits](#credits)
  * [Acknowledgments](#acknowledgments)


## User Experience

A visitor to Foolprooflavors would be someone who is most likely an adult who thinks cooking is a hastle, are creative in other ways but when it comes to cooking their imagination stops. when it comes to cooking they are bored and lazy and at the same time they want easy, cheap, healthy, fast and of course great tasting recipes.

### User Stories ******/////lägg in userstories

For detailed acceptance criteria and tasks associated with each user story, please visit the GitHub repository [here](hhttps://github.com/users/aslinedvinsson/projects/5)

#### EPIC | Sign up/Log in
- User Story: As a new user, I want to be able to register an account with my email.
- User Story: As a registered user I can log in using my credentials

#### EPIC | Recipe posts ///
-

#### EPIC | CRUD functionality for recipe posts
- User Story: As a user, I want to interact in a comment section for recipe posts.
- User Story: Story: As an admin, I want to be able to approve or disapprove comments on recipe posts.
- User Story:Story: As an admin, I want tools to approve or disapprove recipe posts before publication.
- User Story: As a user, I want to be able to view detailed recipe post content.
- User Story: As a user, I want to be able to create and submit a new recipe post.
- User Story: As a user, I want to be able to editing my submitted recipe posts.
- User Story: As a user, I want to delete my own recipe posts when needed.

#### EPIC | User interction (comments, rating) ////
- User Story:
- User Story:
- User Story:


#### EPIC | About page ////
- User Story:
- User Story:
- User Story:

#### EPIC | Site Administration omformulera ////
- User Story:
- User Story:
- User Story:

#### User stories not yet implemented lägg in userstories////
- User Story:
- User Story:
- User Story:




### Design

The website boasts a straightforward and uncluttered design, deliberately chosen to support its mission: to foster a sense of confidence and community among users, and to ignite a passion for cooking in their everyday lives.

#### Colour Scheme
Colour palette from Coolors

![Colour Palette](docs/readme_images/colour_scheme.png) ****////lägg till bild på färg

The website showcases a simple design, with a deliberate emphasis on red and white colors to embody its vision. These colors are selected not only to create an atmosphere that calms the users but also to boost their confidence in the kitchen. The goal is to make the act of cooking feel less like a chore and more like an enjoyable activity, ultimately cultivating a desire to eat and enjoy food.

#### Images
The static images are the one for the About page and a default image of food if no image is uploaded when adding och editing a recipe post. The users choose their own images to upload suitable for the recipe post.

////lägg in små images

#### Fonts ****//////


#### Wireframes//////

<details>

 <summary>Home page</summary>

![Home Page](docs/wireframes/home_wireframe.png)
</details>

<details>

<summary>Recipe page</summary>
![Recipe page](docs/wireframes/recipe_wireframe.png)
</details>


<details>

<summary>Add Recipe</summary>

![Add Recipe](docs/wireframes/addrecipe_wireframe.png)
</details>

<details>

<summary>Edit Recipe</summary>

![Update Recipe](docs/wireframes/addrecipe_wireframe.png)
</details>

<details>

<summary>Add Recipe</summary>

![Delete Recipe](docs/wireframes/addrecipe_wireframe.png)
</details>

<details>

<summary>About page</summary>

![Delete Recipe](docs/wireframes/about_wireframe.png)
</details>




## Agile Methodology

The development process was managed through GitHub projects, utilizing an agile methodology. Refer to the project board link for more details. [here](hhttps://github.com/users/aslinedvinsson/projects/5)

In the GitHub project, there are seven big tasks called Epics. Each smaller task, known as a User Story, has a GitHub Issue linked to an Epic. Every User Story includes clear criteria to show when it's done. These criteria are divided into smaller tasks to help complete the User Story. The MoSCoW method is used to decide which tasks are top priority and which ones can be done later in agile project management.

*****Add printscreen on kanban board/////

## Data Model

**About model**
The About model is taken from the CodeInstitute Walkthrough 'I think, therefor I blog', and is slightly modified. The 'About Us' entry is composed of a title, detailed content, a timestamp for the last update, and an image.  The model is a singular section managed by administrators.

**ContactRequest model**
The ContactRequest model is taken from the CodeInstitute Walkthrough 'I think, therefor I blog', and is slightly modified. The model is designed to collect questions or messages from site visitors. It stores the sender's name, email address, and message content. It also includes a read status to track if the contact request has been addressed.  The model is a singular section managed by administrators.

**RecipePost Model**
The RecipePost model is a partly customed model through the combination of the CodeInstitute Walkthrough 'I think, therefor I blog' and [Django Recipe Sharing Tutorial](https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy)
 Acts as the central entity, with each instance representing a unique recipe. It includes attributes such as title, ingredients, instructions, and a CloudinaryField for image storage. The user attribute is a ForeignKey linking to Django's User model, having a one-to-many relationship from User to RecipePost (a user can author multiple recipes, but each recipe has a single author).

**Comment Model**
The comment model is taken from the CodeInstitute Walkthrough 'I think, therefor I blog'. Model to store user comments on recipes, it has a many-to-one relationship with RecipePost via a ForeignKey. This setup allows multiple comments to be associated with a single recipe. There is also a ForeignKey back to the User model, indicating which user posted the comment, thus implementing a one-to-many relationship from User to Comment.

**RecipeRating Model**
Custom model. Provides a mechanism for users to rate recipes, incorporating a numerical reciperating field. It maintains a dual ForeignKey setup: one linking to RecipePost and another to User. This creates a many-to-one relationship from RecipeRating to both RecipePost and User, enabling multiple ratings per recipe and per user.

The ERD below details the database schema.
*****////
![Database Schema](docs/readme_images/database_schema.png)

## Testing

Testing and results can be found [here](/TESTING.md)

## Security Features and Defensive Design ****

### User Authentication****/////


### Form Validation
Should a form be submitted with incorrect or missing information, it will not proceed, and the user will receive a notification identifying the field that triggered the error.

### Database Security
The env.py file securely stores the database URL and secret key to safeguard against unauthorized database access, a setup established prior to the initial push to GitHub.

To enhance site security, Cross-Site Request Forgery (CSRF) tokens have been implemented across all forms.

### Custom error pages:***////


## Features

### Header

![header](docs/readme_images/features/header.png)

**Logo**////
-

**Navigation Bar**/////

![Navigation bar](docs/readme_images/features/navbar.png)




### Footer

![Footer](docs/readme_images/features/footer.png)

The footer contains links to social media platforms including Facebook, Instagram, Twitter, and YouTube. These links, when clicked, open in a new browser tab to ensure users remain on the site.

### Home Page /////
![Home page](docs/readme_images/features/home.png)




### User Account Pages
Django allauth was implemented to facilitate the creation of Sign Up, Log In, and Log Out features. Users are notified through success messages upon successfully logging in or logging out.

**Register**

![Sign up](docs/readme_images/features/signup.png)

**Log In**

![Log in](docs/readme_images/features/login.png)

**Log Out**

![Log out](docs/readme_images/features/logout.png)


### Recipe Detail Page
**Recipe Details page**//////

![Recipe]](docs/readme_images/features/recipe_details.png)

- The page show a title and image of the recipe, ingredients and instruction. The recipe contributor also choos meal type and level of effort in a roll down menu.

**Recipe rating section**
Logged-in users can rate recipes on a scale of 1 to 10. Each time a user rates a recipe, an average rating is calculated based on the total number of ratings from all users for that specific recipe, and the displayed rating is updated accordingly. Users are not allowed to rate their own submitted recipes.

**Comments Section**

![Add, edit and delete comment](docs/readme_images/features/comment.png)

Below every recipe, all logged-in users can read previously published comments, and they have the ability to add new ones, as well as edit and delete their own previous comments. When a comment is added or updated, the admin must approve and publish it before it becomes visible to other users. The user who added or updated the comment can see their draft comment in a greyish color.



### Add Recipe Form

![Add recipe](docs/readme_images/features/add_recipe.png)

Logged-in users can add a recipe by clicking the corresponding link in the navigation bar.
The 'Ingredients' and 'Instructions' form fields feature a WYSIWYG editor named Summernote, enabling users to format their content with bullet points, headings, and more.
Users have the option to upload a photo with their recipe. In the absence of a photo upload, a default image will be used as the recipe's image.
Through a dropdown menu, users choose mealtype and effort of cooking.
Omitting essential details such as the recipe's Title, Ingredients, or Instructions triggers an error message, highlighting the missing information.
Attempting to add a recipe without being logged in—by triggers a error message that user needs to log in.
Upon successful addition, the user is greeted with a message confirming that the recipe has been added successfully and awaiting admin to publish the recipe.

### Update Recipe Form

![Update recipe](docs/readme_images/features/update_recipe.png)

Logged-in users who authored a recipe can opt to update it by selecting the update button located on the recipe detail page.
The update button is not shown if the user is not the aurthor of the recipe.
Upon initiating an update, the form will be pre-filled with the recipe's existing content.
After successfully updating a recipe, users will receive a notification confirming the update's success and awaiting admin to publish the recipe.

### Delete Recipe

 ![Delete recipe](docs/readme_images/features/delete_recipe.png)

Logged-in users who are the authors of a recipe have the option to delete it by clicking the delete button on the recipe's detail page.
A prompt will appear, asking the user to confirm the deletion or cancel the action.
Upon successful deletion, the user will be notified with a message confirming that the recipe has been deleted.

### About page
![About page](docs/readme_images/features/about.png)

**Contact form**
![Contact form](docs/readme_images/features/contact_form.png)

### Error Pages///////

Custom Error Pages were created to give the user more information on the error and to guide them back to the site.

![header](docs/readme_images/features/403_error.png)

- 400 Bad Request - The Easy Eater is unable to handle this request.
- 403 Page Forbidden - Looks like you're trying to access forbidden content. Please log out and sign in to the correct account.
- 404 Page Not Found - The page you're looking for doesn't exist.
- 500 Server Error - The Easy Eater is currently unable to handle this request

### Future Features
The following user stories were scoped out of the project due to time constraints and labelled as "Could Have" or "Won't have" on the project board in Github. It is intended that these user stories will be implemented at a later date.

- Story: As a user I want a profile page for managing recipes and personal information.
- Story: As a user, I want a search interface for recipes.
- Story: As a user I can share my favorite recipes on social media platforms.
- Story: As a user, I want a frontend section for the dispalyed featured recipes.
- Story: As a user, I want to receive notifications for comments and ratings on my recipes.


## Deployment - Heroku

Deploying a web page to Heroku from a GitHub repository involves several steps:

**Setting Up the Heroku App:**
First, sign in or register at Heroku.
Click "New" in the top right corner on the dashboard, then choose "Create New App" from the dropdown.
Name your app uniquely and meaningfully.
Choose your preferred region.
Finalize by clicking "Create App".

**Integrating the Postgres Database:**
Navigate to the Resources tab, search for Postgres in the add-ons search bar, and select Heroku Postgres.
In the Settings Tab, under Config Vars, locate and copy the DATABASE_URL.

**Configuring the Environment and settings.py:**
In your development environment, create an env.py file in the root directory.
Insert the DATABASE_URL and a SECRET_KEY of your choice into env.py.
Modify settings.py to import env.py and configure SECRET_KEY and DATABASE_URL settings.
Disable the default database config.
Commit your changes and run migrations.
Include the Cloudinary URL in env.py.
Register cloudinary libraries to your installed apps.
Configure STATIC files settings: URLs, storage paths, directories, and Cloudinary storage settings.
Update ALLOWED_HOSTS in settings.py to include your Heroku app domain and 'localhost'.

**Preparing Required Files and Directories:**
Generate a requirements.txt file.
Create media, static, and templates directories within the root directory.
Add a "Procfile" in the root with the content: web: gunicorn your_project_name.wsgi.

**Configuring Heroku Environment Variables:**
Set the following in Heroku's Config Vars:
SECRET_KEY
CLOUDINARY_URL
PORT: 8000
DISABLE_COLLECTSTATIC: 1

**Deployment Process:**
Ensure DEBUG is set to False in Django's settings.
In Heroku's dashboard, go to the Deploy tab, link your GitHub repository, and select the branch to deploy.
Choose between automatic deployments upon repo updates or manual deployment.
After deployment, click "View" to see your live site.

The site is now live and operational.


## Languages

- Python
- HTML
- CSS
- Javascript

## Frameworks - Libraries - Programs Used
- [Django](https://www.djangoproject.com/): Main python framework used in the development of this project
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html): authentication library used to create the user accounts
- [PostgreSQL](https://www.postgresql.org/) was used as the database for this project.
- [Heroku](https://dashboard.heroku.com/login) - was used as the cloud based platform to deploy the site on.
- [Balsamiq](https://balsamiq.com/) - Used to generate Wireframe images.
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - Used for overall development and tweaking, including testing responsiveness and performance.
- [Font Awesome](https://fontawesome.com/) - Used for icons in information bar.
- [GitHub](https://github.com/) - Used for version control and agile tool.
- [Google Fonts](https://fonts.google.com/) - Used to import and alter fonts on the page.
- [W3C](https://www.w3.org/) - Used for HTML & CSS Validation.
- [Code Institute's PEP8](https://pep8ci.herokuapp.com/) - used to validate all the Python code
- [Jshint](https://jshint.com/) - used to validate javascript
- [Color Space](https://mycolor.space/) - Used to create colour palette.
- [Unsplash](https://unsplash.com/) - Used for rendering free images.
- [Favicon](https://favicon.io/) - Used to create the favicon.
- [Lucidchart](https://lucid.app/) - used to create the database schema design
- [Summernote](https://summernote.org/): A WYSIWYG editor to allow users to edit their posts
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) used to manage Django Forms
- [Cloudinary](https://cloudinary.com/): the image hosting service used to upload images
- [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/): CSS Framework for developing responsiveness and styling


## Credits
Photo by <a href="https://unsplash.com/@hermez777?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Hermes Rivera</a> on <a href="https://unsplash.com/photos/vegetable-dish-in-white-ceramic-bowl-Ww8eQWjMJWk?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>

Photo by <a href="https://unsplash.com/@thoughtcatalog?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Thought Catalog</a> on <a href="https://unsplash.com/photos/sliced-green-avocado-fruit-9aOswReDKPo?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>

Photo by <a href="https://unsplash.com/@eliottreyna?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Eliott Reyna</a> on <a href="https://unsplash.com/photos/three-men-and-laughing-two-women-walking-side-by-side-jCEpN62oWL4?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>

- [Django Docs](https://docs.djangoproject.com/en/4.0/)
- [Bootstrap 4.6 Docs](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- [Stack Overflow](https://stackoverflow.com/)
- [Django Recipe Sharing Tutorial](https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy)
- [Code Institute - Blog Walkthrough Project](https://github.com/Code-Institute-Solutions/Django3blog)

Readme inspired by Pedro Cristo https://github.com/PedroCristo/portfolio_project_4/ and Alison O'Keeffe https://github.com/AliOKeeffe/PP4_My_Meal_Planner

## Acknowledgments

**************//////










