
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

function csrfSafeMethod(method) {
// these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$(document).ready(function() {
    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
});

function isEmail(email) {
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
}

function inputPhoneNumber(obj) {
    var number = obj.value.replace(/[^0-9]/g, "");
    var phone = "";

    if(number.length < 4) {
        return number;
    } else if(number.length < 7) {
        phone += number.substr(0, 3);
        phone += "-";
        phone += number.substr(3);
    } else if(number.length < 11) {
        phone += number.substr(0, 3);
        phone += "-";
        phone += number.substr(3, 3);
        phone += "-";
        phone += number.substr(6);
    } else {
        phone += number.substr(0, 3);
        phone += "-";
        phone += number.substr(3, 4);
        phone += "-";
        phone += number.substr(7);
    }
    obj.value = phone;
}

//modify script

var modifyButton = $("#modify");
modifyButton.on("click",function(e) {
    var form = $('#mod')[0];
    var d = new FormData(form);
    var header=sessionStorage["token"];
    $.ajax({
        type:'POST',
        enctype:'multipart/form-data',
        url:'/user/update/',
        data:d,
        processData:false,
        contentType:false,
        cache:false,
        timeout:600000,
        beforeSend: function (xhr) {
            xhr.setRequestHeader("Authorization","JWT " + header);
        },
        success:function(data) {
            alert("수정완료");
            console.log(data);
            top.location.href = '/user/home';
        },
        error: function(e) {
            console.log(e);
            alert("error");
        }
    });
});


//withdraw script

var withdrawButton = $("#withdrawal");

withdrawButton.on("click",function(e) {
    $.ajax({
        type:'POST',
        enctype:'multipart/form-data',
        url:'/delete',
        processData:false,
        contentType:false,
        cache:false,
        timeout:600000,
        success:function(data) {
            alert("삭제 완료");
            console.log(data);
            top.location.href = '/main';
        },
        error: function(e) {
            console.log(e);
            alert("error");
        }
    });
});