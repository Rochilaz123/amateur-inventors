const editModal = new bootstrap.Modal(document.getElementById("editModal"));
const editIdeaButtons = document.getElementsByClassName("btn-edit-idea");
const title = document.getElementById("title").innerText;
const purpose = document.getElementById("purpose").innerText;
const details = document.getElementById("details").innerText;
const issuesElement = document.getElementById('issues');
const issues = issuesElement ? issuesElement.textContent : 'Element with id "issues" not found';
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteIdeaModal = new bootstrap.Modal(document.getElementById("deleteIdeaModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteIdeaButtons = document.getElementsByClassName("btn-delete-idea");
const deleteConfirm = document.getElementById("deleteConfirm");
const closeButtons = document.getElementsByClassName("btn-close");

// Edit Idea

let currentIdeaId = null; // Store the current idea ID


function populateModal(title, purpose, details, issues) {
  document.getElementById('id_title').value = title;
  document.getElementById('id_purpose').value = purpose;
  document.getElementById('id_details').value = details;
  document.getElementById('id_issues').value = issues;
}

for (let button of editIdeaButtons) {
  button.addEventListener("click", (e) => {
    editModal.show();
    const title = document.getElementById("title").innerText;
    const purpose = document.getElementById("purpose").innerText;
    const details = document.getElementById("details").innerText;
    const issuesElement = document.getElementById('issues');
    const issues = issuesElement ? issuesElement.textContent : 'Element with id "issues" not found';

    
    // // Get the idea details from the clicked button
    // let title = e.target.getAttribute("title");
    // let purpose = e.target.getAttribute("purpose");
    // let details = e.target.getAttribute("details");
    // let issues = e.target.getAttribute("issues");

    // Populate the modal with the idea details
    populateModal(title, purpose, details, issues);

    // Store the current idea ID for form submission
    currentIdeaId = e.target.getAttribute("idea_id");
  });
}

// Add event listener for form submission
document.getElementById('ideaForm').addEventListener('submit', function(e) {
  e.preventDefault(); // Prevent default form submission
  
  // Update the form action with the current idea ID
  this.setAttribute("action", `edit_idea/${currentIdeaId}`);
  
  // Submit the form to update the idea
  this.submit();
});

// function populateModal(title, purpose, details, issues) {
//   document.getElementById('id_title').value = title;
//   document.getElementById('id_purpose').value = purpose;
//   document.getElementById('id_details').value = details;
//   document.getElementById('id_issues').value = issues;
// }

// for (let button of editIdeaButtons) {
//   button.addEventListener("click", (e) => {
//     editModal.show();
//     populateModal(title, purpose, details, issues);
    
//     let ideaId = e.target.getAttribute("idea_id");
//     commentForm.setAttribute("action", `edit_comment/${commentId}`);
//   });
// }

  // for (let button of closeButtons) {
  //   button.addEventListener("click", (e) =>
  //   editModal(hide));
  // }                            // This button for closing the modal isn't working at the moment

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


// Delete comment

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