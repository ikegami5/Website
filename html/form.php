<?php

$username = "";
if ($_SERVER["REQUEST_METHOD"] === "POST") {
	$username = $_POST["username"];
	$error = false;
	if (strlen($username) > 8) {
		$error = true;
	}
}

?>
<!DOCTYPE html>
<html lang="ja">
<head>
	<meta charset="utf-8" />
	<title>PHP練習2</title>
	<link rel="stylesheet" type="text/css" href="/style.css" />
</head>
<body>
	<h1>Form Test</h1>
	<p>9文字以上入れるとメッセージが出るよ(*´ω｀*)</p>
	<form action="#" method="POST">
		<input type="text" name="username" placeholder="user name" value="<?php echo htmlspecialchars($username, ENT_QUOTES, "utf-8"); ?>" />
		<input type="submit" value="Check!" />
	</form>
	<p><?php if ($error) { echo "<div class=\"error\">too long</div><br />"; } ?></p>
	<h2>Link</h2>
	<a href="/index.html">TOP</a>
</body>
</html>
