// compose and diaplay the copyright string in the foot
function display_copyright() {
  copyright=new Date();
  update=copyright.getFullYear();
  document.write("<div class=\"copyright\">&copy; " + update + " Copyright <b>openil.org</b>. All Rights Reserved.</div>");
}
