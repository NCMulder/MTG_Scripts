document.addEventListener("keydown", keyDownTextField, false);
gotoNext();

function keyDownTextField(e) {
var keyCode = e.keyCode;
  if(keyCode==13)
    gotoNext();
}

function gotoNext(){
    var newloc;
    var qstr = getParameterByName('showpick');
    if(qstr == 'false'){
        newloc = window.location.href.replace('showpick=false', 'showpick=true');
    } else {
        var pick = getParameterByName('pick');
        var pack = getParameterByName('pack');
        var player = getParameterByName('player');
        
        alert(pick);
        pick = (pick=='15')? '1' : pick++;
        alert(pick);
        
    }
    window.location.assign(newloc);
    return false;
}

function getParameterByName(name) {
    var url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

