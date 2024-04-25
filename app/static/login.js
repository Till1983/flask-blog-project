// This code was created entirely by ChatGPT.

document.addEventListener('DOMContentLoaded', function() {
    // Add event listener to login form submit event
    document.getElementById('loginForm').addEventListener('submit', function(event) {
        // Display loading spinner
        document.getElementById('loadingSpinner').style.display = 'block';
        // Disable login button to prevent multiple submissions
        document.getElementById('loginBtn').disabled = true;
    });
});
