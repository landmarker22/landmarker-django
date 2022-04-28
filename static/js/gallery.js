$(function(){
    $(".detail1").click(function(){
        var g_no = $(this).attr('data-id');
        console.log(g_no);
        $.ajax({
            url: 'gdetail.do',
            data:{'g_no': g_no},
            success: function(result){
                $('#con').html(result);
            }
        });
        $("#navi").css('display', 'none');
        $("#detailModal").css('display', 'flex');
        $("#detailModal").css('top', window.pageYOffset + 'px');
        document.body.style.overflowY = "hidden";
    })

    $('#close_modal').click(function(){
        $("#detailModal").css('display', 'none');
        $("#navi").css('display', 'block');
        document.body.style.overflowY = "visible";
        $(".close_modal").unbind("click");
    })

    $("#plus").click(function(){

    })

})