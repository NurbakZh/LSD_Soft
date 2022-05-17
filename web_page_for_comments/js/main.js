window.onclick = submit;
var lr = document.querySelector(".left_arrow");
lr.style.display = "none";

function submit() {
    var text = document.querySelector("textarea")
    var comment = text.value;
    if(comment.length>6) {
        var token = "5120254425:AAF0I3xKI3Y08vjIHSBjGxGk-ZnIjSYlPhU";
        var id = -722237381;
        var url = `https://api.telegram.org/bot${token}/sendMessage?chat_id=${id}&text=${comment}`

        let api = new XMLHttpRequest();
        api.open("GET",url,true)
        api.send()
    }
}

var s = 0
var photos = document.getElementsByClassName("Slider");

function move(n) {
    if((s+n) > -1 && (s+n) < photos.length) {
        show(s += n);
    }
}

function show(n) {
    var lr = document.querySelector(".left_arrow");
    var rr = document.querySelector(".right_arrow");
    console.log(n)
    if(n == 0) {
        lr.style.display = "none";
    } else if(n == 4) {
        rr.style.display = "none";
    } else {
        lr.style.display = "block";
        rr.style.display = "block";
    }
    for (var i = 0; i < photos.length; i++) {
        photos[i].style.display = "none";
    }
    photos[n].style.display = "block";
}