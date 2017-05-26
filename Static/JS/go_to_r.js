$(document).ready(function() {

	$(".go_to_room").click(function(event) {
		$.ajax({
			url: '/'+$(this).data('id')+'/game',
			type: 'GET',

		})
		
		
	});
	
});