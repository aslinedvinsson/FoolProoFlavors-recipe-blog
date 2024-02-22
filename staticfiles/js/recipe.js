document.addEventListener("DOMContentLoaded", function() {
    const deleteRecipeModalEl = document.querySelector("#deleteRecipeModal");
    //const deleteRecipeModal = new bootstrap.Modal(deleteRecipeModalEl);
    const deleteRecipeModal = bootstrap.Modal.getOrCreateInstance(deleteRecipeModalEl);
    const deleteRecipeConfirm = document.getElementById("deleteRecipeConfirm");
    const deleteRecipeButtons = document.getElementsByClassName("delete_button_recipe");

    startUpdateFunctionality();
    if (deleteRecipeButtons.length > 0) {
        console.log(bootstrap.Modal);
        startDeleteFunctionality(deleteRecipeButtons, deleteRecipeModal, deleteRecipeConfirm);
    }
});

function startUpdateFunctionality() {
    const updateRecipeButtons = document.getElementsByClassName("update_button_recipe");
    for (let button of updateRecipeButtons) {
        button.addEventListener("click", (e) => {
            let updateUrl = e.target.getAttribute("data-update_url");
            window.location.href = updateUrl;
        });
    }
}

function startDeleteFunctionality(deleteRecipeButtons, deleteRecipeModal, deleteRecipeConfirm) {
    for (let button of deleteRecipeButtons) {
        button.addEventListener("click", (e) => {
            e.preventDefault();
            let recipeSlug = e.target.getAttribute("data-recipepost_slug");
            deleteRecipeConfirm.href = `/delete_recipe/${recipeSlug}/`;
            deleteRecipeModal.show();
        });
    }
}














/*
// Inspired by the CodeInstitute Walkthrough 'I think, therefore I blog'
document.addEventListener("DOMContentLoaded", function() {
    const updateRecipeButtons = document.getElementsByClassName("update_button_recipe");
    const deleteRecipeButtons = document.getElementsByClassName("delete_button_recipe");
    //const deleteRecipeModal = new bootstrap.Modal(document.getElementById("deleteRecipeModal"));
    const deleteRecipeConfirm = document.getElementById("deleteRecipeConfirm");

    // const deleteRecipeModalEl = document.getElementById("deleteRecipeModal");
    const deleteRecipeModalEl = document.querySelector("#deleteRecipeModal");


    //const deleteRecipeModalEl = document.querySelector("#deleteRecipeModal");
    const deleteRecipeModal = bootstrap.Modal.getOrCreateInstance(deleteRecipeModalEl);




    /**
     * Initializes edit functionality for the provided edit buttons.
     *
     * For each button in the `editRecipeButtons` collection:
     * - Retrieves the associated recipe's ID upon click.
     * - Opens the edit modal (`editRecipeModal`) to allow editing.


    // Edit functionality
    for (let button of updateRecipeButtons) {
        button.addEventListener("click", (e) => {
            let updateUrl = e.target.getAttribute("data-update_url");
            window.location.href = updateUrl; // Redirect to update_recipe.html
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


    // Deletion functionality
    for (let button of deleteRecipeButtons) {
        button.addEventListener("click", (e) => {
            e.preventDefault();
            let recipeSlug = e.target.getAttribute("data-recipepost_slug");
            deleteRecipeConfirm.href = `/delete_recipe/${recipeSlug}/`;
            deleteRecipeModal.show();
        });
    }
});


*/