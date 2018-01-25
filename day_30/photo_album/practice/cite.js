var photos = document.getElementById('photo_album');

var liList = document.getElementById('photo_album').getElementsByTagName('li');
var largo = liList.length;
document.getElementById('num_photos').innerHTML = "The Number of Photos On This Page Is: " + largo

function newPhoto() {
    var new_photo = document.getElementById('myURL').value;
    var new_entry = document.createElement('li');
    var link = document.createElement('a');
    var image = document.createElement('img');

    link.href = new_photo;
    image.src = new_photo;
    link.appendChild(image);
    new_entry.appendChild(link);
    photos.appendChild(new_entry);
    largo ++ ;
    document.getElementById('num_photos').innerHTML = "The Number of Photos On This Page Is: " + largo;
}

var add_photo = document.getElementById('photo_submit');
add_photo.addEventListener('click', newPhoto);


// function check_function (){
//  console.log("Photo Added");
//
// }

