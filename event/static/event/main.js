const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});


$(document).ready(function() {
    var value1;
    var value2;
    var value2_text;
    var value1;
    $("#p1").change(function () {
     value1 = $(this).val();
     value1_text = $("#p1 option:selected").text();
     $('#pl1').val(value1);
     $("#pl1").text(value1_text)

    });

    $("#p2").change(function () {
    value2 = $(this).val();
    if(value1 == value2){
        alert('Player name are same please change name!')
        return false;
    }
    else{
        value2_text = $("#p2 option:selected").text();
        $('#pl2').val(value2);
        $("#pl2").text(value2_text)
    }
    });
   });