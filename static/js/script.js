const editButtons = document.getElementsByClassName("btn-edit");
const editModal = new bootstrap.Modal(document.getElementById("editModal"));

const title = document.getElementById("title").innerText;
const purpose = document.getElementById("purpose").innerText;
const details = document.getElementById("details").innerText;
const issues = document.getElementById("issues").innerText;


function populateModal(title, purpose, details, issues) {
    console.log("populateModal working")
    document.getElementById('id_title').value = title;
    document.getElementById('id_purpose').value = purpose;
    document.getElementById('id_details').value = details;
    document.getElementById('id_issues').value = issues;
  }

for (let button of editButtons) {
  button.addEventListener("click", (e) =>
    editModal.show(),
    populateModal(title, purpose, details, issues)
)}
  