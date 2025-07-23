const buttonplay = document.getElementById('buttonplay')
const volumeControl = document.getElementById('volumeControl');
const volumeLabel = document.getElementById('volumeLabel');
const audio = document.getElementById("radioPlayer");
var first = true

audio.volume = 0.2

function play() {
    if (first) {
        audio.play()
        audio.muted = true
        first = false
    }
    if (audio.muted) {
        buttonplay.style.border = '10px solid rgb(20, 20, 20)'
        buttonplay.style.marginLeft = '0'
        audio.muted = false
    } else {
        buttonplay.style.border = '15px solid transparent'
        buttonplay.style.borderLeft = '20px solid rgb(20, 20, 20)'
        buttonplay.style.marginLeft = '20px'
        audio.muted = true
    }
}

volumeControl.addEventListener('input', () => {
    audio.volume = volumeControl.value;
    if (audio.volume == 0) {
        document.getElementById('volumeImg').src = "../static/img/Mute.png"
    } else {
        document.getElementById('volumeImg').src = "../static/img/Volume.png"
    }
});

volumeLabel.addEventListener('click', () => {
    if (audio.volume == 0) {
        document.getElementById('volumeImg').src = "../static/img/Volume.png"
        audio.volume = volumeControl.value;
    } else {
        document.getElementById('volumeImg').src = "../static/img/Mute.png"
        audio.volume = 0;
    }
});

function MenuO(){
    document.getElementById("MenuOpen").style.display = "none"
    document.getElementById("menu").style.display = "flex"
};