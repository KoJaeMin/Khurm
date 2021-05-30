$(function(){
    $("#main_logo").on("click", function(){
        location.href="http://naver.com";
    })
    for(var i=0;i<left_menu.Mname.length;i++){
        $("#menu").append(`<div class="button"><a href="${left_menu.Mlink[i]}"> ${left_menu.Mname[i]} </a></div>`);
    }
    
})

/*var iptEls = document.querySelectorAll('input');
[].forEach.call(inps, function(iptEl) {
    iptEl.onchange = function(e) {
        console.log(this.files);
    };
});
*/
var left_menu = {
    Mname:['홈','모든 파일','최근 항목','별표항목','공유됨','파일 요청','삭제된 파일'],
    Mlink:['','','','','','',''],
};
