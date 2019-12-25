var NoResume=true;
$('.Button-stop').on('click', function () {
    console.log("here");
    $('.progress-bar').css('background-color', 'red').attr('aria-valuenow', 20);
    
    $('.Button-pause').attr("disabled", true);

});
$('.Button-pause').on('click', function () {
     $('.Button-pause').css('display','none');
     $('.Button-resume').css('display','inline');
     $('.progress-bar').css('background-color', '#ffcc00');
});
$('.Button-resume').on('click', function () {
    $('.Button-resume').css('display','none');
    $('.Button-pause').css('display','inline');
    $('.progress-bar').css('background-color', 'blue');
});
