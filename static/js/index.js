$(function(){
    $("#main_logo").on("click", function(){
        location.href="#";
    })
    for(var i=0;i<left_menu.Mname.length;i++){
        $("#menu").append(`<div class="button" onclick = "clickonmenu('${left_menu.Mname[i]}')"> ${left_menu.Mname[i]} </div>`);
    }
    $('body').on('click',(e)=>{
        var $tgPoint = $(e.target);
        var $popCallBtn = $tgPoint.hasClass('sub_button')
        var $popArea = $tgPoint.hasClass('folder_set')
        if ( !$popCallBtn && !$popArea ) {
            $('ul.submenu > li').css('display','none');
        }
    })
    $('.folder_set').on('click',()=>{
        $(this).next('#folder').click();
    })

    
    
})
function clickonmenu(item){
    $('.abstract > p').html(`${item}`);
    $.ajax({
        url:'/folder/', 
        success:function(data)
        { $('.main_contents').html(data) } 
    });
}

var iptEls = document.querySelectorAll('input[id="folder_set"]');

var left_menu = {
    Mname:['홈','사진 파일','즐겨찾기','공유된 파일','삭제된 파일'],
    EMname:['home','imgfile','bookmark','shared','delete'],
    //Mlink:['./file_home.html','./file_all.html','./file_bookmark.html','./file_shared.html','./file_delete.html'],//['/home','/file','/file/bookmark','/file/shared','/file/delete'],
};
