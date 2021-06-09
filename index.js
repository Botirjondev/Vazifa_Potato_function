// potatoes("potato") ➞ 1

// potatoes("potatopotato") ➞ 2

// potatoes("potatoapple") ➞ 1

var str1 = 'potatopotatoinlinepotatoofkillhisworkpotato';

function potatoes(str) {
	var myTurn = str.match(/potato/g).length;
	return myTurn;
}


console.log(potatoes(str1));

// Bu code qo`shimcha

var str = "atirgulMohigulgulchexra ";

function rain(str) {
    var res = str.match(/gul/g);
    return res;
}


console.log(rain(str));
