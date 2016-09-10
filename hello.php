<?php

//変数
$message = "Hello from PHP!<br>";
echo $message;

//演算
$int1 = 1;
$int2 = 2;
$int3 = 3;
echo ($int1 + $int2)."<br>";

//型を表示
var_dump($message);
echo "<br>";

//定数
define("MY_FINAL_VALUE", "14");
echo MY_FINAL_VALUE."<br>";

//特殊定数(行数)
var_dump(__LINE__);
echo "<br>";

//文字列
$str = "PHP";
$hello = "hello $str";
echo $hello."<br>";



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