// JavaScript Document



// Can also be used with $(document).ready()
$(document).ready(function() {
  $('.flexslider').flexslider({
    animation: "fade"
  });
	
	$(".mobile-menu").click(function(){
		$(".mobile-nav").slideToggle(150);
	});
	
  	
});

