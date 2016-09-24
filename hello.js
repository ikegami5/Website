console.log("Hello from script!");

//変数
var hello = "Hello", x = 3;
console.log(hello);

var y = 10;
var z = y % x;
console.log("10 % 3 = ");
console.log(z);
z = y / x;
console.log("10 / 3 = ");
console.log(z);
x += 3;
console.log("3 + 3 = ");
console.log(x);
x--;
console.log("6 - 1 = ")
console.log(x);

//文字列
var s = "\"string\"\n";
var number = 1234;
console.log("文字列" + s + number);

// if
var score = 80;
if (score > 60) {
	console.log("OK!");
} else if (score > 40) {
	console.log("soso");
} else {
	console.log("NG");
}
if (score === 80) {
	console.log("score = " + score);
}
if (score > 70 && score < 90) {
	console.log("70 < score < 90");
}
if (!("" || 0 || NaN || null || undefined || false)) {
	console.log("false");
}
if ("abc" && 1 && true) {
	console.log("true");
}
var max = (x > y) ? x : y;
console.log("3 or 10, bigger is " + max);

// switch
var signal = "red";
switch (signal) {
	case "red":
		console.log("stop");
		break;
	case "green":
	case "blue":
		console.log("go");
		break;
	case "yellow":
		console.log("caution");
		break;
	default:
		console.log("wrong signal");
		break;
}

// while
var i = 0;
while (i < 10) {
	console.log(i);
	i++;
}
do {
	console.log(i);
	i--;
} while (i > 0);

// for
console.log("for");
for (var i = 0; i < 10; i++) {
	console.log(i);
}
console.log("break");
for (var i = 0; i < 10; i++) {
	if (i === 5) {
		break;
	}
	console.log(i);
}
console.log("continue");
for (var i = 0; i < 10; i++) {
	if (i === 5) {
		continue;
	}
	console.log(i);
}

// alert / confirm / prompt
alert("alert");

var bool = confirm("OK?");
if (bool) {
	console.log("OK");
} else {
	console.log("NG");
}

var name = prompt("insert name", "default name");
console.log(name);

// function
function message(name) {
	var msg = "Hello, " + name;
	return msg;
}
var greet = message("Tom");
console.log(greet);

var add = function(x, y) {
	return x + y;
};
console.log(add(3, 5));

(function() {
	var x = 10;
	var y = 20;
	console.log(x + y);
})();

// timer
var iInShow = 0;
/*
not recommended
*/
// function show() {
// 	iInShow++
// 	console.log(iInShow);
// }
// var interval = setInterval(function() {
// 	show();
// 	if (iInShow > 4) {
// 		clearInterval(interval);
// 	}
// }, 1000);
function show2() {
	iInShow++;
	console.log(iInShow);
	var timeout = setTimeout(function() {
		show2();
	}, 1000);
	if (iInShow > 4) {
		clearTimeout(timeout);
	}
}
show2();









