// document.addEventListener("DOMContentLoaded", function(event) { 
//     // check if user has been here before
//     var visited = localStorage.getItem('visited');

//     if (!visited) {
//         // this code will only run if the user hasn't been here before
//         alert("Welcome to our website!");
//         // set the user to have now visited
//         localStorage.setItem('visited', true);
//     }
// });

document.addEventListener("DOMContentLoaded", function(event) { 
    // check if user has been here before
    var visited = localStorage.getItem('visited');

    if (!visited) {
        // this code will only run if the user hasn't been here before
        var welcomeModal = new bootstrap.Modal(document.getElementById('welcomeModal'), {});
        welcomeModal.show();
        // set the user to have now visited
        localStorage.setItem('visited', true);
    }
});