$(document).ready(function(){
    $("p").css("color", "green");
    $(".lager-p").show(0);
    $(".ipa-p").hide(0);
    $(".sour-p").show(0);

    $(".lager").mouseover (function(){
        $(".lager-p").show(1000);
    })
    $(".lager").mouseleave (function(){
        $(".lager-p").hide(1000);

    $(".ipa").mouseover (function(){
        $(".ipa-p").show(1000);
    })
    $(".ipa").mouseleave (function(){
        $(".ipa-p").hide(1000);
    
    $(".sour").mouseover (function(){
        $(".sour-p").show(1000);
    })
    $(".sour").mouseleave (function(){
        $(".sour-p").hide(1000);
    })
    
    })
    })
    });
