//Inspired by the CodeInstitute Walkthrough 'I think, therefor I blog'
const updateRecipeButtons = document.getElementsByClassName(
    "update_button_recipe");
const recipePostForm = document.getElementById("recipePostForm");
const deleteRecipeButtons = document.getElementsByClassName(
    "delete_button_recipe");
const deleteRecipeModal = new bootstrap.Modal(document.getElementById(
    "deleteRecipeModal"));
const deleteRecipeConfirm = document.getElementById("deleteRecipeConfirm");

/**
 * Initializes edit functionality for the provided edit buttons.
 *
 * For each button in the `editRecipeButtons` collection:
 * - Retrieves the associated recipe's ID upon click.
 * - Opens the edit modal (`editRecipeModal`) to allow editing.
 */

for (let button of updateRecipeButtons) {
    button.addEventListener("click", (e) => {
        let updateUrl = e.target.getAttribute("data-update_url");
         // Redirect to update_recipe.html
         window.location.href = updateUrl;
    });
}


/**
* Initializes deletion functionality for the provided delete buttons.
*
* For each button in the `deleteRecipeButtons` collection:
* - Retrieves the associated recipe's ID upon click.
* - Updates the `deleteRecipeConfirm` link's href to point to the
* deletion endpoint for the specific recipe.
* - Displays a confirmation modal (`deleteRecipeModal`) to prompt
* the user for confirmation before deletion.
*/


for (let button of deleteRecipeButtons) {
    button.addEventListener("click", (e) => {
        e.preventDefault();
        let recipeSlug = e.target.getAttribute("data-recipepost_slug");
        deleteRecipeConfirm.href = `/delete_recipe/${recipeSlug}/`;
        deleteRecipeModal.show();
    });
}



