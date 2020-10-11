<!DOCTYPE html>
<html>
<head>
 <title>Searcher</title>
 <style>
h1 {text-align: center; padding-bottom: 25px;}
</style>
 <link rel="stylesheet" type="text/css" href="../Assets/style.css">
</head>
<body>
 <main>
  <header>
    <nav>
      <a href="../index.html">
       <img class="logo" src="../Assets/pine-apple.png" height="125" width="125"/>
      </a>
      <div class="links">
       <a href="#">About</a>
       <a href="#">Demo</a>
       <button class="button_med" href="#">Login</button>
      </div>
    </nav>
  </header>
</main>

<h1>Search A Mac Address Here</h1>


<form method="post">
<input type="text" name="search" value="" />
<input type="submit" name="submit" value="Search" />
</form>

<table>
<tr>
<th>Mac Address</th>
<th>Signal Strength</th>
<th>Type</th>
<th>Last Seen</th>
</tr>

<?php
 if (isset($_POST['submit'])) {
 $search_string = $_POST['search'];
}
$db = new SQLite3('main');
 $result = $db->query("SELECT * FROM databasetableTwo WHERE Devmac LIKE '$search_string' OR Strongest_signal LIKE '$search_string' OR Type LIKE '$search_string' OR Last_time LIKE '$search_string'");
 while ($row = $result->fetchArray()){
        echo "<tr><td>";
	echo $row['devmac'];
	echo "</td><td>";
	echo $row['strongest_signal'];
	echo "</td><td>";
	echo $row['type'];
	echo "</td><td>";
	echo date('Y-m-d H:i:s',$row['last_time']);
	echo "</td></tr>";
        }
echo "</table>"
?>


</body>
</html>
