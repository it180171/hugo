fetch('/movies')
    .then(response => response.json())
    .then(movies => {
        // Do something with the movie data
        console.log(movies);
    })
    .catch(error => {
        // Handle any errors that occur during the request
        console.error(error);
    });