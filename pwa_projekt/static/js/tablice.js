$(function(){
    var board_id;
    var tab_id;
    var rem_url;
    function remove_tab(board_id, tab_id){
        board_id = board_id;
        tab_id = tab_id;
        rem_url = "/operation/" + board_id + "/" + tab_id
    };
    $(".board").click(function(){
        $(this).children(".board-body").slideToggle();
    });
    $(".tab-remove").click(remove_tab(){
        $.post(rem_url, {operation: 'remove'})
    });
});