


/// Ajax onload wait

$(document).ajaxStart(function() {

	$('#spinner').html('<div class="sk-three-bounce "><div class="sk-child sk-bounce1"></div><div class="sk-child sk-bounce2"></div><div class="sk-child sk-bounce3"></div></div>');
   // $('#main').html("");
  	//  $('#result1').html("<center><i class=\"fa fa-spinner fa-3x fa-spin\"></i><br><br>Transcribing your video, please wait, this could take a few minutes...</center>");
});

$(document).ajaxStop(function() {
     $('#spinner').html('');
    // $('#convertButton').prop('disabled', false);

});


 var map = L.map('map').setView([-41.2858, 174.78682], 14);
        mapLink = 
            '<a href="http://openstreetmap.org">OpenStreetMap</a>';
        L.tileLayer(
            'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; ' + mapLink + ' Contributors',
            maxZoom: 18,
            }).addTo(map);

        
        function recenter(){

        var	x= -42.2858
        var	y = 175.78682

        map.panTo(new L.LatLng(40.737, -73.923));

        }



$('#location-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    


    get_location();
});




function get_location(){

    console.log("get_location post is working!"); // sanity check
    console.log($('#location').val());


   
    $.ajax({
        url : "/get_location_images", // the endpoint
        type : "GET", // http method
        data : { 
                location : $('#location').val(),
               //page : $('#page').val(),
                }, // data sent with the post request
        dataType: 'json',
        // handle a successful response
        success : function(json) {

        	recenter();
        	var p;
        	// p = parseInt($('#page').val());
        	p=1;
        	// p=p+1;

        	$( "#page" ).text( p );
             
            console.log(json); // log the returned json to the console
            //console.log(JSON.stringify(json));
            console.log("success"); // another sanity check
            console.log(json.length);
            console.log(p);
            var output =""


           
            for (i = 0; i < json.length; i++) {
					    //text += cars[i] + "<br>";
					   console.log(json[i]);
					    
					    output+='<div onclick="mark_fav(this.id)"" id="img'+i+'" class="image"><img src="'+
					    	json[i]+'"alt="">	</div>'

					}

			$('#images').html(output);
			$('.image_slider').show();
            // $('#result').html(JSON.stringify(json));
             //var base_url = window.location.origin;
    //           $('#result').html("<video width='320' height='240' controls>"+
				//   "<source src=' {{ STATIC_URL }}' ' type='video/mp4'>"+
				// "</video>");
                
    			
               
                    // alert(JSON.stringify(json["is_valid"]));
                    // $('#result2').html(json['is_valid']);
                    // $('#result3').html(JSON.stringify(json));
                   // console.log(JSON.stringify(json["is_valid"]));
                

                

        },

     
        error : function(xhr,errmsg,err) {

        	alert("No results");

            // $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
            //     " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
             console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }


    });


};


function click_next(){

	console.log("it works");
}

function mark_fav(id){

	console.log("it works - mark_fav");
	console.log(id);
	console.log($('#'+id+'>img').attr('src'));

	swal({
  title: "Add to Favorite?",
  text: "Click to OK to add to favorites",
  type: "info",
  showCancelButton: true,
  closeOnConfirm: false,
  showLoaderOnConfirm: true,
},
function(){
  
  // ajax post goes here 
  post_fav($('#'+id+'>img').attr('src'));
  setTimeout(function(){
    swal("Image has been added to favorites");
  }, 2000);
});

}

function post_fav(img){

	console.log('post_fav function accessed')

	$.ajax({
        url : "/add_to_fav", // the endpoint
        type : "POST", // http method
        data : { 
                
                	image : img,
               	
                }, // data sent with the post request
        dataType: 'json',
        // handle a successful response
        done : function(data) {

        	console.log('image has been added to favorites');

        },
        // error : function(xhr,errmsg,err) {

        //      console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        //      console.log('post_fav error');
        // }
    });
}




function get_next_10(){

    console.log("get_next 10 post is working!"); // sanity check
    console.log($('#location').val());
    console.log($('#page').val());


   
    $.ajax({
        url : "/get_next10", // the endpoint
        type : "GET", // http method
        data : { 
                location : $('#location').val(),
               	page : $('#page').val(),
                }, // data sent with the post request
        dataType: 'json',
        // handle a successful response
        success : function(json) {

        	
        	var p;
        	p = parseInt($('#page').val());
        	
        	p=p+1;

        	$( "#page" ).val( p );
             
            console.log(json); // log the returned json to the console
            //console.log(JSON.stringify(json));
            console.log("success"); // another sanity check
            console.log(json.length);
           	
            var output =""


           
             for (i = 0; i < json.length; i++) {
					    //text += cars[i] + "<br>";
					   console.log(json[i]);
					    
					    output+='<div onclick="mark_fav(this.id)"" id="img'+i+'" class="image"><img src="'+
					    	json[i]+'"alt="">	</div>'

					}

			$('#images').html(output);
            // $('#result').html(JSON.stringify(json));
             //var base_url = window.location.origin;
    //           $('#result').html("<video width='320' height='240' controls>"+
				//   "<source src=' {{ STATIC_URL }}' ' type='video/mp4'>"+
				// "</video>");
                
    			
               
                    // alert(JSON.stringify(json["is_valid"]));
                    // $('#result2').html(json['is_valid']);
                    // $('#result3').html(JSON.stringify(json));
                   // console.log(JSON.stringify(json["is_valid"]));
                

                

        },

     
        error : function(xhr,errmsg,err) {

        	alert("No results");

            // $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
            //     " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
             console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }


    });


};



function get_fav(){
	
	$('.image_slider').hide();

	console.log('get')

	$.ajax({
			  url: "/get_fav",
			  type:"GET",
			  dataType: 'json',

			  success: function (result) {
        	console.log(result);
        	var output =""



        	for (i = 0; i < result.length; i++) {
					    //text += cars[i] + "<br>";
					   console.log(result[i]);
					    
					    output+='<img  class="list_img" src="'+
					    	result[i]+'"alt="">'

					}

        	//<img class="list_img" src="https://farm1.staticflickr.com/633/22831431993_b5aa7c8ca8_t.jpg" alt="">
        	
        	console.log(output);
        	$('#list_imgs').html('');
        	$('#list_imgs').html(output);

    },
    error: function (xhr, ajaxOptions, thrownError) {
        console.log(xhr.statusText);
        console.log(xhr.responseText);
        console.log(xhr.status);
        console.log(thrownError);
    }
});
			// }).done(function(data) {

			// 	console.log(data);

			//   $( this ).addClass( "done" );
			// }).error(function(xhr,errmsg,err){

			// 	console.log("Get fave error");
			// 	console.log(xhr.status);
			// 	console.log(xhr.responseText);
			// 	console.log(errmsg);
				
			// });


}

function show_slider(){

	$('.image_slider').show();
}


function get_locations(){

	$('.image_slider').hide();
}