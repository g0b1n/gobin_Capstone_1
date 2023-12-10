$(document).ready(function(){
    // Variable to hold the timeout ID
    let closeDropdownTimeout;

    // Handle dropdown open on mouseover
    $(document).on('mouseover', '.dropdown-toggle', function() {
        var $dropdown = $(this).closest('.dropdown');
        $dropdown.addClass('show');
        $dropdown.find('.dropdown-menu').addClass('show');

        // Clear any existing timeout to prevent closing
        clearTimeout(closeDropdownTimeout);
    });

    // Handle dropdown open on click
    $(document).on('click', '.dropdown-toggle', function() {
        let $dropdown = $(this).closest('.dropdown');
        $dropdown.toggleClass('show');
        $dropdown.find('.dropdown-menu').toggleClass('show');
    });

    // Handle closing the dropdown with a delay
    $('.dropdown').on('mouseout', function(event){
        let $dropdown = $(this);
        closeDropdownTimeout = setTimeout(function() {
            if (!$(event.relatedTarget).closest('.dropdown').length) {
                $dropdown.removeClass('show');
                $dropdown.find('.dropdown-menu').removeClass('show');
            }
        }, 300); // 500 milliseconds delay
    });

    // Cancel the timeout if the user re-enters the dropdown area
    $('.dropdown').on('mouseover', function() {
        clearTimeout(closeDropdownTimeout);
    });
});

// Toggle button from outline to solid when clicked to add to favriote
document.getElementById('toggleButton').addEventListener('click', function() {
    var button = this;
    if (button.classList.contains('btn-outline-success')) {
        button.classList.remove('btn-outline-success');
        button.classList.add('btn-success');
    } else {
        button.classList.remove('btn-success');
        button.classList.add('btn-outline-success');
    }
});


// Add movie to fav
// document.getElementById('toggleButton').addEventListener('click', function(){
//     fetch('/add_to_favorites/' + movieId, {method: 'POST'})
//     .then(response => response.json())
//     .then(data => {
//         if (data.success) {
//             // change the heart icon to filled
//             document.getElementById('toggleButton').addEventListener('click', function() {
//                 var button = this;
//                 if (button.classList.contains('btn-outline-success')) {
//                     button.classList.remove('btn-outline-success');
//                     button.classList.add('btn-success');
//                 } else {
//                     button.classList.remove('btn-success');
//                     button.classList.add('btn-outline-success');
//                 }
//             });
//         }
//     })
//     .catch(error => console.error('Error:', error))
// })


// Read more button
function toggleReadMore() {
    let bioElement = document.getElementById('person-bio');
    bioElement.classList.toggle('expanded');
}



function addToFavorites(movieId) {
    // Make an AJAX request to your Flask route to add the movie to favorites
    fetch(`/add_to_favorites/${movieId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            // Any additional data you want to send
        }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        // Optionally update the UI based on the response
        // For example, change the button color, update the icon, etc.
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}