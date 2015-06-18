//If image is hovered over
$("p img").hover(function(){
    
    //if image source has 2 in it
    if (this.src.indexOf("2") != -1) {
        
       //something2.jpg = something.jpg
        this.src = this.src.replace("2", "")    
    } 
    
    //if image source doesn't have 2 in it
    else {
        
        //something.jpg = something2.jpg
        this.src = this.src.slice(0,-4) + "2.jpg";
    }

});

// can also use this regex thing:
// var hasNumber = /\d/