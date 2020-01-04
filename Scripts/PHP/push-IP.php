<?php
$IP_HOME = $_SERVER['REMOTE_ADDR'];
$myfile = fopen("/var/www/html/ip/ip.html", "w") or die("Unable to open file!");
fwrite($myfile, $IP_HOME);
fclose($myfile);
?>
