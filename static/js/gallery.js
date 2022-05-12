$.ajaxSetup({
        headers: { "X-CSRFToken": '{{csrf_token}}' }
    });
$(function(){
    $(document).on('click', '#gwrite-btn', function(){
        var u_no = $("#gwrite-btn").attr('data-id');
        console.log('u_no : ' + u_no);
        if(u_no == ''){
            alert('로그인이 필요합니다.');
        }else{
            $.ajax({
                url: 'gwrite.do',
                data:{'u_no': u_no},
                type:'post',
                success: function(result){
                    $('#con').html(result);
                    $(".nav-bar").css('display', 'none');
                    $("#detailModal").css('display', 'flex');
                    $("#detailModal").css('top', window.pageYOffset + 'px');
                    document.body.style.overflowY = "hidden";
                }
            });
        }

    })
    $(document).on('click', '.detail1', function(){
        var g_no = $(this).attr('data-id');
        console.log('g_no : ' + g_no);
        $.ajax({
            url: 'gdetail.do',
            data:{'g_no': g_no},
            success: function(result){
                $('#con').html(result);
                $(".nav-bar").css('display', 'none');
                $("#detailModal").css('display', 'flex');
                $("#detailModal").css('top', window.pageYOffset + 'px');
                document.body.style.overflowY = "hidden";
            }
        });
    })

    $(document).on('click', '#close_modal', function(){
        $("#detailModal").css('display', 'none');
        $(".nav-bar").css('display', 'block');
        document.body.style.overflowY = "visible";
        $(".close_modal").unbind("click");
    })

    $(document).on('click', '.like', function(){
        var g_no = $(this).attr('g_no');
        var u_no = $(this).attr('u_no');
        var onoff = $(this).attr('onoff');
        if(u_no == 0){
            alert("로그인이 필요합니다.");
        }else{
            console.log('g_no : ' + g_no + ', u_no : ' + u_no + ', onoff : ', onoff);
            $.ajax({
                url: 'gallike.do',
                data:{'g_no': g_no,
                      'u_no': u_no,
                      'onoff': onoff},
                success: function(result){

                }
            });
            if(onoff=='1'){
                $(this).attr('onoff', '0');
                $(this).attr('class', 'bi bi-heart fs-5 like');
                $(this).css('color', '#e06666');
            }else{
                $(this).attr('onoff', '1');
                $(this).attr('class', 'bi bi-heart-fill fs-5 like');
                $(this).css('color', '#e06666');
            }
        }
    })

    $(document).on('keypress', '#search-bar', function(e){
        if(e.keyCode == 13){
            $('#search-btn').click();
        }
    })

    $(document).on('click', '#search-btn', function(){
        var search = $('#search-bar').val();
        console.log(search);

        $.ajax({
            url: 'galsearch.do',
            data: {'search': search},
            success:function(result){
                if(result.length == 0){
                    alert('검색 결과가 없습니다.');
                }
                else{
                    $('#galbox').html(result);
                }
            }
        });
    })

    $(document).on('click', '.op', function(){
        var op = $(this).attr('op');
        console.log(op);

        $.ajax({
            url: 'galselect.do',
            data: {'op': op},
            type: 'GET',
            success:function(result){
                $('#galbox').html(result);
            }
        });
    })
})
