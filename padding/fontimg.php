<?php

$size = 50;
$angle = 0;
// $font_filename = "";
$str = "A";

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

// フォントファイルへのパス
// $font = './arial.ttf';

// まず最初のテキスト用のバウンディングボックスを作成します
// $bbox = imagettfbbox(10, 45, $font, 'Powered by PHP ' . phpversion());

$bbox = imagettfbbox(
  $size, // float $size,
  $angle, // float $angle,
  $font, // string $font_filename,
  $str // string $string,
    // array $options = []
);
// X 座標と Y 座標
$x = $bbox[0] + (imagesx($im) / 2) - ($bbox[4] / 2) - 25;
$y = $bbox[1] + (imagesy($im) / 2) - ($bbox[5] / 2) - 5;

// 書き込みます
imagettftext($im, $size, $angle, $x, $y, $black, $font, $str);

$out_filename = "./works/test.png";
imagepng($im, $out_filename);
imagedestroy($im);