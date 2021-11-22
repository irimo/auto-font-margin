<?php

$size = 50;
$angle = 0;
// $font_filename = "";
$str = "A";

// GD の環境変数を設定
putenv('GDFONTPATH=' . realpath('./dist/ttfs'));

// 使用されるフォント名 ( .ttf 拡張子の欠落に注意)
$font = 'VL-Gothic-Regular';

$points = imagettfbbox(
  $size, // float $size,
  $angle, // float $angle,
  $font, // string $font_filename,
  $str // string $string,
    // array $options = []
);
var_dump($points);
$out_filename = "./works/test.png";
// imagegd($image, $out_filename);