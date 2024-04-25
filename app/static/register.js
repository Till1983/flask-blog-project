// This code was created entirely by ChatGPT.

document.addEventListener('DOMContentLoaded', function() {
    // Add event listener to register form submit event
    document.getElementById('registerForm').addEventListener('submit', function(event) {
        // Display loading spinner
        document.getElementById('loadingSpinner').style.display = 'block';
        // Disable register button to prevent multiple submissions
        document.getElementById('registerBtn').disabled = true;
    });
});