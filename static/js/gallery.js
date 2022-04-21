$(function(){
    $(".detail").click(function(){
//        $("#detailModal").modal();
        $("#detailModal").css('display', 'flex');
        $("#detailModal").css('top', window.pageYOffset + 'px');
        document.body.style.overflowY = "hidden";
    })
})

$(function(){
    $('#close_modal').click(function(){
        $("#detailModal").css('display', 'none');
        document.body.style.overflowY = "visible";
    })
})
