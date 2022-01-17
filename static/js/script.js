$(document).ready(function(){
    $(".lager-p").hide(0);
    $(".ipa-p").hide(0);
    $(".sour-p").hide(0);
    $(".wheat-p").hide(0);
    $(".stout-p").hide(0);

  $(".lager").click(function(){
      $(".lager-p").slideToggle("slow");
  });

  $(".ipa").click(function(){
    $(".ipa-p").slideToggle("slow");
  });

  $(".sour").click(function(){
    $(".sour-p").slideToggle("slow");
  });

  $(".wheat").click(function(){
    $(".wheat-p").slideToggle("slow");
  });

  $(".stout").click(function(){
    $(".stout-p").slideToggle("slow");
  });

});
