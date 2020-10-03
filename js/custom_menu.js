

$(document).ready(function () {
								 
	 

	
	/* Theme menu
  	 ------------------------------------------------------------------------*/
	if ($.fn.RMenu) { 
		$('ul#menu').RMenu({
								sub_menu_width	 	: parseInt($('#menu ul').css('width')),
								menu_height 		: 30, // Menu height px
								fade_effect 		: 'true'
								});
	
		 
	}
	
	
/* End custom scripts */
}) 

