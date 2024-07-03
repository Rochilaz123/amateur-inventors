

const editModal = new bootstrap.Modal(document.getElementById("editModal"));
const editIdeaButtons = document.getElementsByClassName("btn-edit-idea");
const title = document.getElementById("title").innerText;
const purpose = document.getElementById("purpose").innerText;
const details = document.getElementById("details").innerText;
const issues = document.getElementById("issues");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteIdeaModal = new bootstrap.Modal(document.getElementById("deleteIdeaModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteIdeaButtons = document.getElementsByClassName("btn-delete-idea");
const deleteConfirm = document.getElementById("deleteConfirm");
const closeButtons = document.getElementsByClassName("btn-close");

// Edit Idea

function populateModal(title, purpose, details, issues) {
    console.log("populateModal working")
    document.getElementById('id_title').value = title;
    document.getElementById('id_purpose').value = purpose;
    document.getElementById('id_details').value = details;
    document.getElementById('id_issues').value = issues;
  }

for (let button of editIdeaButtons) {
  button.addEventListener("click", (e) =>
    editModal.show(),
    populateModal(title, purpose, details, issues));

    // for (let button of closeButtons) {
    //   button.addEventListener("click", (e) =>
    //   editModal(hide));
    // }                            // This button for closing the modal isn't working at the moment
  }

// Edit Comment

const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `commentText` input/textarea with the comment's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    commentText.value = commentContent;
    submitButton.innerText = "Update"; // this doesn't seem to be working
    commentForm.setAttribute("action", `edit_comment/${commentId}`);
  });
}

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    deleteConfirm.href = `delete_comment/${commentId}`;
    deleteModal.show();
  });
}

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated idea's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteIdeaModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteIdeaButtons) {
  button.addEventListener("click", (e) => {
    let ideaId = e.target.getAttribute("idea_id");
    console.log(ideaId);
    deleteIdeaConfirm.href = `delete_idea/${ideaId}`;
    deleteIdeaModal.show();
  });
}