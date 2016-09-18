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
		echo "stop".$br;
		break;
	default:
		echo "wrong".$br;
		break;
}



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