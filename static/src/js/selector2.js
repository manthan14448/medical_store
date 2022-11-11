function findPos(obj) {
  var curleft = (curtop = 0);
  if (obj.offsetParent) {
    curleft = obj.offsetLeft;
    curtop = obj.offsetTop;
    while ((obj = obj.offsetParent)) {
      curleft += obj.offsetLeft;
      curtop += obj.offsetTop;
    }
  }
  return [curleft, curtop];
}
var scLastOver = null;
function highlight(id) {
  if (scLastOver != null && scLastOver != id) dehighlight(scLastOver);
  var tr = document.getElementById("BodyPartTable").rows[id];
  var div1 = tr.cells[0].childNodes[0];
  var div2 = tr.cells[0].childNodes[1];
  div1.style.display = "none";
  div2.style.display = "block";
  var bodyPart = document.getElementById("BodyPart" + id);
  if (bodyPart != null) {
    bodyPart.style.display = "block";
    var posTr = findPos(tr);
    var posBodyPart = findPos(bodyPart);
    var trHeight = 0;
    if (id > 0) {
      trHeight =
        posTr[1] -
        findPos(document.getElementById("BodyPartTable").rows[id - 1])[1];
    } else {
      trHeight =
        findPos(document.getElementById("BodyPartTable").rows[1])[1] - posTr[1];
    }
    var x1 = posBodyPart[0] + bodyPart.childNodes[0].width / 2;
    var y1 = posBodyPart[1] + bodyPart.childNodes[0].height / 2;
    var x2 = posTr[0] - 2;
    var y2 = posTr[1] + trHeight / 2;

    var pt = false;
    var div = document.getElementById("ScLineDiv");
    if (div == null) {
      pt = true;
    }

    if (pt) {
      if (id == 0) {
        y1 -= 152;
        x1 += 2;
      } else if (id == 1) {
        y1 -= 141;
      } else if (id == 2) {
        y1 -= 92;
      }
    } else {
      var wRel = bodyPart.childNodes[0].width;
      var hRel = bodyPart.childNodes[0].height;
      if (id == 0) {
        y1 -= (144 * hRel) / 317;
      } else if (id == 1) {
        y1 -= (140 * hRel) / 317;
      } else if (id == 2) {
        y1 -= (127 * hRel) / 317;
      } else if (id == 3) {
        y1 -= (88 * hRel) / 317;
      } else if (id == 4) {
        y1 -= (70 * hRel) / 317;
        x1 += (35 * wRel) / 126;
      } else if (id == 5) {
        y1 -= (35 * hRel) / 317;
      } else if (id == 6) {
        y1 += (58 * hRel) / 317;
        x1 += (15 * wRel) / 126;
      } else if (id == 7) {
        y1 -= (25 * hRel) / 317;
        x1 += (35 * wRel) / 126;
      }
    }
    drawLine(x1, y1, x2, y2);
  }
  scLastOver = id;
}
function dehighlight(id) {
  var tr = document.getElementById("BodyPartTable").rows[id];
  var div1 = tr.cells[0].childNodes[0];
  var div2 = tr.cells[0].childNodes[1];
  div2.style.display = "none";
  div1.style.display = "block";
  var bodyPart = document.getElementById("BodyPart" + id);
  if (bodyPart != null) {
    bodyPart.style.display = "none";
    var scLineDiv = document.getElementById("ScLineDiv");
    if (scLineDiv == null) {
      scLineDiv = document.getElementById("ScLineDivPt");
    }
    scLineDiv.style.display = "none";
  }
  if (id == scLastOver) scLastOver = null;
}
function drawLine(x1, y1, x2, y2) {
  var top = true;
  if (x1 > x2) {
    var a = x1;
    x1 = x2;
    x2 = a;
  }
  if (y1 > y2) {
    var a = y1;
    y1 = y2;
    y2 = a;
    top = false;
  }
  var pt = false;
  var div = document.getElementById("ScLineDiv");
  if (div == null) {
    div = document.getElementById("ScLineDivPt");
    pt = true;
  }
  var pos = findPos(div.parentNode);
  div.style.left = "" + x1 - pos[0] + "px";
  div.style.top = "" + y1 - pos[1] + "px";
  var table = div.childNodes[0];
  table.setAttribute("width", x2 - x1 + 1);
  table.setAttribute("height", y2 - y1 + 1);
  var td1 = table.rows[0].cells[0];
  var td2 = table.rows[0].cells[1];
  if (pt) {
    if (top) {
      td1.style.borderTop = "0px";
      td1.style.borderBottom = "0px";
      td1.style.borderLeft = "0px";
      td1.childNodes[0].style.display = "block";
      td2.style.borderTop = "0px";
      td2.style.borderBottom = "0px";
      td2.style.borderLeft = "0px";
    } //child
    else {
      td1.style.borderTop = "0px";
      td1.style.borderBottom = "0px";
      td1.style.borderLeft = "0px";
      td1.childNodes[0].style.display = "none";
      td2.style.borderTop = "0px";
      td2.style.borderBottom = "0px";
      td2.style.borderLeft = "0px";
    }
  } else {
    if (top) {
      td1.style.borderTop = "0px";
      td1.style.borderBottom = "0px";
      td2.style.borderBottom = "0px";
      td2.style.borderTop = "0px";
    } else {
      td1.style.borderBottom = "0px";
      td1.style.borderTop = "0px";
      td2.style.borderTop = "0px";
      td2.style.borderBottom = "0px";
    }
  }
  div.style.display = "block";
}
