
// var map;
// // the initialize function creates the map
// function initialize(){
//     var center = new google.maps.LatLng(39.7392, -104.9903);
//     map = new google.maps.Map(document.getElementById('map'), {
//         center: center,
//         //the lower the number the further the map will be zoomed out
//         zoom: 13
//     });
// }
// // occurs when page loads
// google.maps.event.addDomListener(window, 'load', initialize);




// $(document).ready(function(){
//     $("#t-reg").click(function(){
//         $("#reg-form").slideToggle();
//     });
//     $("#t-log").click(function(){
//         $("#log-form").slideToggle();
//     });

//     $(".title").click(function(){
//         alert("WHOA NELLY!!");
//     });

// });


        /*
        var c = document.getElementById("card-container").childElementCount;
        console.log(c);
        function carousel(){
            var degrees = 360; //checked-success
            var arr = []; //checked-success
            var increment = 0; //checked-success
            var cardCount = document.getElementById("card-container").childElementCount;//will give number of cards
            var card = document.querySelectorAll("#card"); //checked-success(provides node list)
            console.log("CARD"+ card);
            console.log(cardCount);
            console.log("array before"+arr);

            arr.push(card);

            console.log("array after"+arr);
            
            console.log("DIVISION");
            degrees/=cardCount; //works = 72
            for(let i = 0; i < card.length; i++){
                var element = card[i];
                var child = element.parentNode.firstChild;
                var index = 0;
                increment += degrees;

                while(true){
                    if(child.nodeType === Node.ELEMENT_NODE){
                        console.log("element: "+ element + "| index: "+i);
                        console.log("style change: rotateY("+ increment + "deg)"); //increments properly
                        var transform = document.getElementById("card").style.transform = element + "rotateY("+ increment + "deg)";
                        transform;
                        index++;

                    }
                    if(child===element || !child.nextSibling){
                        break;
                    }
                    child = child.nextSibling;
                }

                element.dataset.number = index;
            }
            console.log(card);
        }
        carousel();

*/