<?php

$size = 50;
$angle = 0;
// $font_filename = "";
$str = "q";

// GD の環境変数を設定
putenv('GDFONTPATH=' . realpath('./dist/ttfs'));

// 使用されるフォント名 ( .ttf 拡張子の欠落に注意)
$font = 'VL-Gothic-Regular';

// $points = imagettfbbox(
//   $size, // float $size,
//   $angle, // float $angle,
//   $font, // string $font_filename,
//   $str // string $string,
//     // array $options = []
// );
// var_dump($points);
// $out_filename = "./works/test.png";
// imagegd($image, $out_filename);

// 300x150 の画像を作成します
$im = imagecreatetruecolor(300, 150);
$black = imagecolorallocate($im, 0, 0, 0);
$white = imagecolorallocate($im, 255, 255, 255);

// 背景を白に設定します
imagefilledrectangle($im, 0, 0, 299, 299, $white);

$bbox = imagettfbbox(
  $size, // float $size,
  $angle, // float $angle,
  $font, // string $font_filename,
  $str // string $string,
    // array $options = []
);
// 配列のキー	値の意味
// 0	左下角の X 座標
// 1	左下角の Y 座標
// 2	右下角の X 座標
// 3	右下角の Y 座標
// 4	右上角の X 座標
// 5	右上角の Y 座標
// 6	左上角の X 座標
// 7	左上角の Y 座標
var_dump($bbox);
// X 座標と Y 座標
// $x = $bbox[0] + (imagesx($im) / 2) - ($bbox[4] / 2);
$x = 0;
// $y = $bbox[1] + (imagesy($im) / 2) - ($bbox[5] / 2);
$h = abs($bbox[7] - $bbox[1]);
$y = $h;

// 書き込みます
// 最初の文字のベースポイント (ほぼ文字の左下角) 
imagettftext($im, $size, $angle, $x, $y, $black, $font, $str);
$rect = array("x" => $x, "y" => 0, "width" => abs($bbox[6] - $bbox[4]), "height" => $h);
var_dump($rect);
$im_crop = imagecrop($im, $rect);
$out_filename = "./works/test.png";
imagepng($im_crop, $out_filename);
imagedestroy($im);
imagedestroy($im_crop);
