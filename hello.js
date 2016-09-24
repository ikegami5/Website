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









