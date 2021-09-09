// $("#file-upload").css("opacity", "0");

$("#file-browser").click((e) => {
  e.preventDefault();
  $("#file-upload").trigger("click");
});