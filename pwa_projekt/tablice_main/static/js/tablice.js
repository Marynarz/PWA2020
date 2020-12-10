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
    $(".remove_obj").click(function(){
        var data = $(this).data('href');
        var csrftoken = getCookie('csrftoken');
        var form = $('form').serializeArray()
        $.ajax({
        url: data,
        method: "POST",
        headers: {'X-CSRFToken': csrftoken},
        data: {'operation': "remove" }
        }).always(function(){
        location.reload(true)
        })
    });
    $(".add-board").click(function(){
        var csrftoken = getCookie('csrftoken');
        var form = $('form#addB').serializeArray();
        $.ajax({
        url: '/operation',
        method: "POST",
        headers: {'X-CSRFToken': csrftoken, form},
        data: {'operation': "add", form}
        }).always(function(){
        location.reload(true)
        });
    });
    $(".add-tab").click(function(){
        $('.board-body').fadeToggle()
    });
    $(".add-tab-load").click(function(){
        var data = $('a#page_url').data('href');
        var csrftoken = getCookie('csrftoken');
        var form = $('form#addT').serializeArray();
        $.ajax({
        url: data,
        method: "POST",
        headers: {'X-CSRFToken': csrftoken, form},
        data: {'operation': "add", form}
        }).always(function(){
        location.reload(true)
        });
    });
    $( ".tab" ).sortable({
        axis: 'y',
        update: function (event, ui) {
            var url_pos = $('a#pos_url').data('href');
            var data = $(this).sortable('serialize');
            var csrftoken = getCookie('csrftoken');
            // POST to server using $.post or $.ajax
            $.ajax({
                type: 'POST',
                headers: {'X-CSRFToken': csrftoken},
                url: url_pos,
                data: data
            });
        }
        });
    $(".add-elem").click(function(){
        $('.elem-add-body').fadeToggle()
    });
    $(".add-elem-load").click(function(){
        var data = $('a#add_tab_url').data('href');
        var csrftoken = getCookie('csrftoken');
        var form = $('form#addE').serializeArray();
        $.ajax({
        url: data,
        method: "POST",
        headers: {'X-CSRFToken': csrftoken, form},
        data: {'operation': "add", form}
        }).always(function(){
        location.reload(true)
        });
    });
        $(".elem").click(function(){
        $('.elem-body').fadeToggle()
    });
    $( ".sortable" ).sortable({
        connectWith: '.sortable',
        update: function (event, ui) {
            var data = $(this).sortable('toArray');
            var parent_id = $(this).parent().attr('id');
            var csrftoken = getCookie('csrftoken');
            // POST to server using $.post or $.ajax
            $.ajax({
                type: 'POST',
                headers: {'X-CSRFToken': csrftoken},
                url: '/position/elem/',
                data: {data, 'parent': parent_id}
            });
        }
        });
});