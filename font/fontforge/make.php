<?php
require_once("./makefont.class.php");
$filename = "test";
$fontname_e = "test font";
$fontname_j = "FONT";
$authorname = "UNKNOWN";

$files = array();

// $n = hexdec("21");
// $n_max = hexdec("7e");
// for($i=$n; $i<=$n_max; $i++) {
//     $files["u00".dechex($n)] = "./maked_fonts/raw/A.jpg";
// }
$files["u0021"] = "./maked_fonts/raw/A.jpg";
/*
// A-Z u0041-u005a
$n = 41;
// これ for で回せないの...
$files["u00".dechex($n)] = "./maked_fonts/raw/A.jpg";
$files["u00".dechex(++$n)] = "./maked_fonts/raw/B.jpg";
$files["u00".dechex(++$n)] = "./maked_fonts/raw/C.jpg";
$files["u00".dechex(++$n)] = "./maked_fonts/raw/D.jpg";
$files["u00".dechex(++$n)] = "./maked_fonts/raw/E.jpg";
$files["u00".dechex(++$n)] = "./maked_fonts/raw/F.jpg";
$files["u00".dechex(++$n)] = "./maked_fonts/raw/G.jpg";
$files["u00".dechex(++$n)] = "./maked_fonts/raw/H.jpg";
$files["u00".dechex(++$n)] = "./maked_fonts/raw/I.jpg";
$files["u00".dechex(++$n)] = "./maked_fonts/raw/J.jpg";
$files["u00".dechex(++$n)] = "./maked_fonts/raw/K.jpg";
$files["u00".dechex(++$n)] = "./maked_fonts/raw/L.jpg";
$files["u00".dechex(++$n)] = "./maked_fonts/raw/M.jpg";
$files["u00".dechex(++$n)] = "./maked_fonts/raw/N.jpg";
$files["u00".dechex(++$n)] = "./maked_fonts/raw/O.jpg";
$files["u00".dechex(++$n)] = "./maked_fonts/raw/P.jpg";
$files["u00".dechex(++$n)] = "./maked_fonts/raw/Q.jpg";
$files["u00".dechex(++$n)] = "./maked_fonts/raw/R.jpg";
$files["u00".dechex(++$n)] = "./maked_fonts/raw/S.jpg";
$files["u00".dechex(++$n)] = "./maked_fonts/raw/T.jpg";
$files["u00".dechex(++$n)] = "./maked_fonts/raw/U.jpg";
$files["u00".dechex(++$n)] = "./maked_fonts/raw/V.jpg";
$files["u00".dechex(++$n)] = "./maked_fonts/raw/W.jpg";
$files["u00".dechex(++$n)] = "./maked_fonts/raw/X.jpg";
$files["u00".dechex(++$n)] = "./maked_fonts/raw/Y.jpg";
$files["u00".dechex(++$n)] = "./maked_fonts/raw/Z.jpg";

// a-z u0061-u007a
$n = 41;
for($n2=hexdec("61"); $n2<=hexdec("7a"); $n2++) {
    $files["u00".dechex($n2)] = $files["u00".dechex($n++)];
}
// 0-9 u0030-u0039
$n3 = 0;
for($n3_code=hexdec("30"); $n3_code<=hexdec("39"); $n3_code++) {
    $files["u00".dechex(30)] = "./maked_fonts/raw/".$n3++.".jpg";
}
// !
$files["u0021"] = "./maked_fonts/raw/exclamation.jpg";
// ?
$files["u003f"] = "./maked_fonts/raw/question.jpg";
// ,
$files["u002c"] = "./maked_fonts/raw/colon.jpg";
// .
$files["u002e"] = "./maked_fonts/raw/dot.jpg";
*/

$filepath = MakeFont::make($filename, $fontname_e, $fontname_j, $authorname, $files);
if(file_exists($filepath) === true){
    echo $filepath;
    echo "<br>フォントが作成されました。";
	// header('Content-Disposition: attachment; filename="'.$filename.'.ttf"');
	// header('Content-Type: application/octet-stream');
	// header('Content-Length: '.filesize($filepath));
	// readfile($filepath);
    // exec("cp {$filepath} ./maked_fonts/backup/");
    // exec("rm -rf {$filepath}");
} else {
	echo "フォントの作成に失敗しました。";
}