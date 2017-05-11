$(document).ready(function(){

	$(".click_me_player").click(function(){
		$(".clicked_player").toggleClass("clicked_player");
		$ (this).toggleClass("clicked_player");

});
		$(".click_me_enemy").click(function(){
		$(".clicked_enemy").toggleClass("clicked_enemy");
		$ (this).toggleClass("clicked_enemy");
	});
		$("#fight").click(function(){
			$.ajax({
           type: "GET",
           url: "/attack/",
           data:{
               'partEnemy':$(".clicked_enemy").data('part'),
               'partPlayer':$(".clicked_player").data('part'),
           },
           cache:false,
           success:
           function(data){
           		console.log(data)
           		var obj = jQuery.parseJSON( data );
               $("#enemy").css("width",obj.healthEnemy+"%");
               $("#player").css("width",obj.healthPlayer+"%");

           }
      });
	});
})