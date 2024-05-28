document.getElementById('deleteLink').addEventListener('click', function(event) {
    event.preventDefault();
    document.getElementById('confirmationModal').style.display = 'flex';
});

document.getElementById('confirmDelete').addEventListener('click', function() {
    window.location.href = document.getElementById('deleteLink').href;
});

document.getElementById('cancelDelete').addEventListener('click', function() {
    document.getElementById('confirmationModal').style.display = 'none';
});