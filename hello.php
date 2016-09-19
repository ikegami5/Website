<?php

$br = "<br>";

//変数
$message = "Hello from PHP!";
echo $message.$br;

//演算
$int1 = 1;
$int2 = 2;
$int3 = 3;
echo ($int1 + $int2).$br;

//型を表示
var_dump($message);
echo $br;

//定数
define("MY_FINAL_VALUE", "14");
echo MY_FINAL_VALUE.$br;

//特殊定数(行数)
var_dump(__LINE__);
echo $br;

//文字列
$str = "PHP";
$hello = "hello $str";
$wrong = 'hello $str';
echo $hello.$br;
echo $wrong.$br;

//if
$score = 85;
if ($score > 80) {
	echo "great!";
} elseif ($score > 60) {
	echo "good!";
} else {
	echo "soso";
}
echo $br;

//真偽値
if (!(0 or false or null or "" or "0")) {
	echo "false";
}
echo $br;
if (1 and true and "hello") {
	echo "true";
}
echo $br;

//三項演算子
$seven = 7;
$five = 5;
$max = ($seven > $five) ? $seven : $five;
//it means ...
if ($seven > $five) {
	$max = $seven;
} else {
	$max = $five;
}
echo $max.$br;

//switch
$signal = "red";
switch ($signal) {
	case "red":
		echo "stop$br";
		break;
	default:
		echo "wrong$br";
		break;
}

//while
$index = 0;
while ($index < 10) {
	echo "$index ";
	$index++;
}
echo $br;
do {
	$index--;
	echo "$index ";
} while ($index > 0);
echo $br;

//for,break,continue
for ($index = 0; $index < 10; $index++) { 
	echo "$index ";
}
echo $br;
for ($index = 0; $index < 10; $index++) { 
	if ($index === 5) {
		break;
	}
	echo "$index ";
}
echo $br;
for ($index = 0; $index < 10; $index++) {
	if ($index === 5) {
		continue;
	} 
	echo "$index ";
}
echo $br;

//配列
$sales = array(
	"two hundred" => 200,
	"eight hundred" => 800,
	"six hundred" => 600,
);
echo $sales["eight hundred"].$br;
$colors = array("red", "blue", "pink");
echo $colors[1].$br;

//foreach
foreach ($sales as $key => $value) {
	echo "($key) $value ";
}
echo $br;
foreach ($colors as $value) {
	echo "$value ";
}
echo $br;

//colon using for, while, if, foreach: confortable for writing in html
for ($index = 0; $index < 10; $index++):
	echo "$index ";
endfor;

//function
function sayHi($name = "nanashi") {
	echo "hi! $name$br";
}
sayHi("Tom");
sayHi("Bob");
sayHi();
function add($num1, $num2) {
	return $num1 + $num2;
}
$num = add(4, 7);
echo $num.$br;




?>
<!DOCTYPE html>
<html lang="ja">
<head>
	<title>PHP練習</title>
	<meta charset="utf-8">
</head>
<body>
	<p>htmlに<?php echo "php" ?>を埋め込む</p>
</body>
</html>