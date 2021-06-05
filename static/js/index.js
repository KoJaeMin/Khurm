$(function(){
    $("#main_logo").on("click", function(){
        location.href="#";
    })
    for(var i=0;i<left_menu.Mname.length;i++){
        $("#menu").append(`<div class="button" onclick = "clickonmenu('${left_menu.Mname[i]}')"> ${left_menu.Mname[i]} </div>`);
    }
    $('#file_content').find('.main_contents').load('test');
    //$('#file_content').find('.main_contents').hide();
    //$('.abstract').find('.main_contents').not().hide();
    
})
function clickonmenu(item){
    $('.abstract > p').html(`${item}`);
    //$('.abstract > .main_contents')
    switch(item){
        case '사진 파일':
            $('#file_content').find('.main_contents').load('img_s3');
            break;
        case '즐겨찾기':
            $('#file_content').find('.main_contents').load('favorite_s3');
            break;
        case '공유된 파일':
            $('#file_content').find('.main_contents').load('shared_s3');
            break;
        default:
            $('#file_content').find('.main_contents').load('test');
            break;
    }
    //$('.main_contents').toggle();
    /*$.ajax({
        url:'/folder/', 
        success:function(data)
        { $('.main_contents').html(data) } 
    });
    */
}

var iptEls = document.querySelectorAll('input[id="folder_set"]');

var left_menu = {
    Mname:['홈','사진 파일','즐겨찾기','공유된 파일'],
    EMname:['home','imgfile','bookmark','shared'],
    //Mlink:['./file_home.html','./file_all.html','./file_bookmark.html','./file_shared.html','./file_delete.html'],//['/home','/file','/file/bookmark','/file/shared','/file/delete'],
};
