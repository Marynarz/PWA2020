$(function(){
    function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
    }

    $(".board").click(function(){
        $(this).children(".board-body").slideToggle();
    });
    $(".remove_obj").click(function(){
        var data = $(this).data('href');
        var csrftoken = getCookie('csrftoken');
        $.ajax({
        url: data,
        method: "POST",
        headers: {'X-CSRFToken': csrftoken},
        data: {'operation': "remove" }
        }).always(function(){
        location.reload(true)
        })
    });
});