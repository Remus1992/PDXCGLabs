// $(document).ready(function() {
//     $('#addToDo').click(function (e) {
//     e.preventDefault();
//     var in_val = $('addToDoText').val();
//     console.log(in_val)
//     $('#toDoList').hide('slow'); // OR you can use .toggle()
// })


// document.querySelector('#addToDo').addEventListener('click', function (e) {
//     e.preventDefault();
//     console.log('Clicked')
// });
//
//
// OR
//
//
// $('#addToDo').click(function (e) {
//     e.preventDefault();
//     console.log('Clicked!')
// });



// document.querySelector('#addToDo').addEventListener('click', function (e) {
//     e.preventDefault();
//     console.log('Clicked')
//     var in_value = document.getElementById('addToDoText').value;
//     console.log(in_value);
// });
//
// //OR
//
// $('#addToDo').click(function (e) {
//     e.preventDefault();
//     console.log('Clicked!')
//     var in_val = $('addToDoText').val();
//     console.log(in_val)
//     $('#toDoList').hide('slow'); // OR you can use .toggle()
// });

// $('.tackDone').click (function (e) {
// console.log('checkbox clicked')
// });

$('#addToDo').click(function (e) {
    var in_val = $('addToDoText').val();
    if (in_val.length > 0) {
        var new_task = "<tr><td>" + in_val + '</td><td>input type="checkbox" class="taskDone"' +
            '</td><td><a href="#">X</a></td></tr>';
        var table = $('toDoList');
        table.append(new_task);
        input.val('')
    }
});

$('toDoList')
    .on('change', '.taskDone', function (e) {
    if ($(this).prop('checked')) {
        $($(this).parent().prev()[0]).css('textDecoration', 'line-through')
    } else {
        $($(this).parent().prev()[0]).css('textDecoration', 'none')
    }
  })
  on('click', '.taskDone', function (e)) {
    e.preventDefault();
    $(this).parent().parent().remove()
  });





















