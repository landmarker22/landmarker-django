var isRun = false;
$(function(){
    $(".detail1").click(function(){
        var g_no = $(this).attr('data-id');
        console.log(g_no + isRun);
        if(isRun == true) {
            return;
        }
        isRun = true;
        $.ajax({
            async : false,
            url: 'gdetail.do',
            data:{'g_no': g_no},
            success: function(result){
                isRun = false;
                $('#con').html(result);
            }
        });
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

$(function(){
    $(".detail2").click(function(){
        var g_no = $(this).attr('data-id');
        console.log(g_no);
        console.log('ㅠㅠ');
        $.ajax({
            url: 'gdetail.do',
            type: 'post',
            data: {'g_no': g_no},
//            beforeSend: function () {
//                $("#m").modal("show");
//            },
            success: function (data) {
                alert(data);
            }
        });
        $('#m').modal();
        $('#m').modal({remote : 'common/gdetail.html'});

    })

    $(".detail3").click(function(){
        var data = $(this).data('id');
        console.log(data);
        $("#contents.body-contents").val(data);
        $("#text-contents.body-contents").html(data);
    });
})

