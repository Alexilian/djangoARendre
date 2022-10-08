$(".containerNM").on('click', function(){
    $(this).toggleClass('clicked');
    setTimeout(function (){
        window.location.href = "/userTasks/list/";
    }, 500);
});