<?php

//変数
$message = "Hello from PHP!";
echo $message;

//演算
$int1 = 1;
$int2 = 2;
$int3 = 3;
echo $int1 + $int2;

//べき乗
echo $int2 ** $int3;

//型を表示
var_dump($message);

//定数
define("MY_FINAL_VALUE", "14");
echo MY_FINAL_VALUE;

//特殊定数(行数)
var_dump(__LINE__);



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