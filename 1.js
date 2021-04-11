document.getElementById("container").onscroll = function() {
  //console.log(document.getElementById("container").offsetHeight);
  const height = document.getElementById("container").offsetHeight;
  const scroll = document.getElementById("container").scrollTop
  const opacity = 1 - ((height-scroll)/height);
 console.log(opacity); document.getElementById("overlay").style.opacity = opacity;
}