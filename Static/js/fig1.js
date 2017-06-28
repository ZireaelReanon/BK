$(document).ready(function(){

    $(".click_me_player").click(function(){
        $(".clicked_player").toggleClass("clicked_player");
        $(this).toggleClass("clicked_player");
    });
    $(".click_me_enemy").click(function(){
        $(".clicked_enemy").toggleClass("clicked_enemy");
        $(this).toggleClass("clicked_enemy");
    });



    $("#fight").click(function(){
        $("#player_name").data("id");
        $("#emeny_name").data("id");
        $.ajax({
            type: "GET",
            url: "/attack/",
            data:{
                'partEnemy':$(".clicked_enemy").data('part'),
                'partPlayer':$(".clicked_player").data('part'),
                // Допонительные параметры для поиска персонажей в базе данных
                'enemyId':$(".player_name").data('id'),
                'playerId':$(".enemy_name").data('id'),
                'roomId':$("#room").data("id")


            },
            cache:false,
            success:
            function(data){
                console.log(data)

                var obj = jQuery.parseJSON( data );

                if ( obj.result )
                        {
                            console.log(obj.result)
                            alert(obj.result)
                            $(location).attr('href', '/result')


                         }
                        else {
                            console.log("fight time");
                        };


                $("#enemy").css("width",obj.healthEnemy+"%");
                $("#player").css("width",obj.healthPlayer+"%");
                $('#player_health').html(obj.healthPlayer)
                $('#enemy_health').html(obj.healthEnemy)


            }
       });
    })
})