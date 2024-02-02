const updateRecipeButtons = document.getElementsByClassName("btn-edit");
const recipeForm = document.getElementById("recipeForm");
//const updateRecipeModal = new bootstrap.Modal(document.getElementById("updateRecipeModal"));
const deleteRecipeButtons = document.getElementsByClassName("btn-delete-recipe");
const deleteRecipeModal = new bootstrap.Modal(document.getElementById("deleteRecipeModal"));
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
        console.log("Edit button clicked!");
        let recipeId = e.target.getAttribute("data-recipe_id");
        let updateUrl = e.target.getAttribute("data-update_url");
        console.log("Recipe ID:", recipeId);
        console.log("Update URL:", updateUrl);

        // Set the form action dynamically
        recipeForm.setAttribute("action", updateUrl);
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
        let recipeId = e.target.getAttribute("data-recipe_id");
        deleteRecipeConfirm.href = `delete_recipe/${recipeId}`;
        deleteRecipeModal.show();
    });
}

console.log("updateRecipeButtons:", updateRecipeButtons);
console.log("recipeForm:", recipeForm);
console.log("deleteRecipeModal:", deleteRecipeModal);
console.log("deleteRecipeConfirm:", deleteRecipeConfirm);