<?php

//変数
$message = "Hello from PHP!\n";
echo $message;

//演算
$int1 = 1;
$int2 = 2;
$int3 = 3;
echo ($int1 + $int2)."\n";

//型を表示
var_dump($message);
echo "\n";

//定数
define("MY_FINAL_VALUE", "14");
echo MY_FINAL_VALUE."\n";

//特殊定数(行数)
var_dump(__LINE__);
echo "\n";ß


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