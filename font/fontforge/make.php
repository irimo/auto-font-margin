<?php
require_once("./makefont.class.php");
$filename = "test";
$fontname_e = "test font";
$fontname_j = "FONT";
$authorname = "UNKNOWN";

$filepath = MakeFont::make($filename, $fontname_e, $fontname_j, $authorname);
if(file_exists($filepath) === true){
	header('Content-Disposition: attachment; filename="'.$filename.'.ttf"');
	header('Content-Type: application/octet-stream');
	header('Content-Length: '.filesize($filepath));
	readfile($filepath);
    exec("cp {$filepath} ./maked_fonts/backup/");
    exec("rm -rf {$filepath}");
} else {
	echo "フォントの作成に失敗しました。";
}