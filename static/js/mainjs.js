
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
//login script
function isEmail(email) {
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
}
var loginButton = $("#login");

loginButton.on("click",function(e) {
    var email = document.getElementById("loginemail");
    var password = document.getElementById("loginpassword");
    if(email.value=='' || password.value=='') {
        //alert("필수 항목을 입력해주세요");
        if(email.value=='') {
            email.focus();
        }
        else {
            password.focus();
        }
        return false;
    }
    if(isEmail(email.value)==false) {
        alert("E-mail형식으로 입력해주세요.");
        email.focus();
        return false;
    }
    var form = $('#login')[0];
    var d = new FormData(form);
    $.ajax({
        type:'POST',
        enctype:'multipart/form-data',
        url:'/user/login/',//rest-auth/login에서 바꿈
        data:d,
        processData:false,
        contentType:false,
        cache:false,
        timeout:600000,
        success:function(data) {
            alert("로그인 완료");
            console.log(data);
            sessionStorage.setItem("token",data['token']);
            top.location.href="/user/home/";
        },
        error: function(request,status,error) {
            alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);

        }
    });
});

//register script

var registerButton = $("#register");
registerButton.on("click",function(e) {
    var email = document.getElementById("regemail");
    var nickname = document.getElementById("regnickname");
    var password1 = document.getElementById("regpassword1");
    var password2 = document.getElementById("regpassword2");
    if(isEmail(email.value)==false) {
        alert("E-mail형식으로 입력해주세요.");
        email.focus();
        return false;
    }
    if(email.value == '' || nickname.value == '' || password1.value == '' || password2.value == '') {
        //alert("필수 항목을 입력해주세요.");
        if(email.value=='') {
            email.focus();
        }
        else if(nickname.value=='') {
            nickname.focus();
        }
        else if(password1.value=='') {
            password1.focus();
        }
        else {
            password2.focus();
        }
        return false;
    }
    if(password1.value != password2.value) {
        alert("패스워드가 다릅니다.");
        password2.focus();
        return false;
    }
    var form = $('#reg')[0];
    var d = new FormData(form);
    $.ajax({
        type:'POST',
        enctype:'multipart/form-data',
        url:'/user/signup/',
        data:d,
        processData:false,
        contentType:false,
        cache:false,
        timeout:600000,
        success:function(data) {
            alert("회원가입 완료");
            console.log(data);
            top.location.href = '/user/main';
        },
        error: function(request,status,error) {
            alert(request.responseText);

        }
    });
});