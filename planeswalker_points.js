function getMatches(verbose = false){
    var his_rows = document.getElementsByClassName("MatchHistoryRow");
    console.log("Number of rows:" + his_rows.length);

    if(true){
        var text;
        for(var i = 0; i < his_rows.length; i++){
            var opp = his_rows[i].getElementsByClassName("MatchOpponent")[0].innerText;
			if(opp == "" || opp == "Multiple Opponents"){
                if(!verbose) continue;
				str = his_rows[i].getElementsByClassName("MatchResult")[0].innerText + "\n";
            } else {
                str = his_rows[i].getElementsByClassName("MatchResult")[0].innerText + " " + opp;
            }

            text += str;
        }
        console.log(text);
    }
}