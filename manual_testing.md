# Manual Testing

[Go to README](README.md)

**TEST CASE**|**PRE-CONDITION**|**ACTUAL RESULT**|**PASS/FAIL**
-----|-----|-----|-----
Add a new recipe to the blog|User logged in|Is adding the new recipe|✅ PASS
Update an existing recipe|User logged in and owns a recipe|Is updating the recipe, but there is an unused field for current image and information about the current image is provided below.|PASS/FAIL 
Delete an existing recipe|User logged in and owns a recipe|Is deleting the recipe|✅ PASS
Rate someone else's recipe|User logged in|Is displaying the new rating|✅ PASS
Rate your own recipe|User logged in|Is displaying the number that the user entered, but the rating is not submitted|PASS/FAIL 
Write a comment on own recipe|User logged in and owns a recipe|Comment is displayed under the user's own recipe,  but if the page is refreshed, another identical comment is posted.|PASS/FAIL 
Create a new user account|User not logged in|Is the account created|✅ PASS
Log into an existing account|User not logged in|Is the user logged in|✅ PASS
Log out of an account|User logged in|Is the user logged out|✅ PASS
Click on the Home link|Any user online|Is the home page displayed|✅ PASS
Click on the Add Recipe link|User logged in|Is the Add Recipe page displayed|✅ PASS
Click on the Login link|User not logged in|Is the login page displayed|✅ PASS
Click on the Register link|User not logged in|Is the registration page displayed|✅ PASS
Click on the Logout link|User logged in|Is the user logged out and redirected|PASS
Ensure copyright text is displayed correctly|Any user online|Is the correct copyright text displayed|✅ PASS
Click on the Facebook icon|Any user online|Is the user redirected correctly to Facebook|✅ PASS
Click on the Twitter icon|Any user online|Is the user redirected correctly to Twitter|✅ PASS
Click on the Instagram icon|Any user online|Is the user redirected correctly to Instagram|✅ PASS
Click on the YouTube icon|Any user online|Is the user redirected correctly to YouTube|✅ PASS
Ensure recipe details are displayed correctly|Any user online|Are the details correct and visible|✅ PASS
Ensure average rating is displayed|Any user online|Is the average rating visible|✅ PASS
Check update button visibility|User logged in and owns recipe|Is the update button visible|✅ PASS
Check delete button visibility|User logged in and owns recipe|Is the delete button visible|✅ PASS
Ensure the recipe image is displayed|Any user online|Is the correct image or placeholder visible|✅ PASS
Display the number of comments|Any user online|Is the comment count correct|✅ PASS
Check visibility of comments|Any user online|Are comments visible|✅ PASS
Trigger delete recipe modal|User logged in and owns recipe|Does the confirmation modal appear|✅ PASS
Trigger delete comment modal|User logged in and owns comment|Does the confirmation modal appear|✅ PASS
Ensure all text content is correctly displayed|User navigates to the About page|Content displays as expected|✅ PASS
Check the layout of the About page|User navigates to the About page|Layout is consistent and functional|✅ PASS
Ensure images are loaded and relevant|User navigates to the About page|Images load correctly|✅ PASS
Test navigation link to the About page|User is on the Home page|Redirection to About page is successful|✅ PASS
Check that the About page is responsive on different devices|User accesses the website on various devices|The page is responsive across devices|✅ PASS
Ensure contact form is functional and visible|User navigates to the About page|Contact form works as intended|✅ PASS
