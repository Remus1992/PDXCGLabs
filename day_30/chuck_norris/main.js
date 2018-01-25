function grab_joke() {
    $.ajax({
        url: 'http:/m',
        type: 'GET',
        success: function (response) {
            $('#jokeId').text(response.value.id);
            $('#joke').text(response.value.joke);
        },
        error: function (e) {
            console.log(e);
        }

    });
}

$('#factMe').click(grab_joke);