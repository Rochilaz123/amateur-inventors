// Edit Idea


const editModal = new bootstrap.Modal(document.getElementById("editModal"));
const editIdeaButtons = document.getElementsByClassName("btn-edit-idea");
const title = document.getElementById("title").innerText;
const purpose = document.getElementById("purpose").innerText;
const details = document.getElementById("details").innerText;
const issues = document.getElementById("issues");


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
    populateModal(title, purpose, details, issues)
)}


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
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_comment/${commentId}`);
  });
}