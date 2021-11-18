<?php
// makeFont.function.php
// 2013.03.29 syohan
// https://github.com/irimo/fonttt

require_once(DIRNAME(__FILE__)."/imageconvert.class.php");

class MakeFont{
  public static function make($filename, $fontname_e, $fontname_j, $authorname){
    $tmp_dir = $this->getTmpDir();
    $obj = new ImageConvert($tmp_dir);
    if(!isset($_FILES))die("画像ファイルが読み込めません。");
    foreach($_FILES as $key => $value){
      $obj->makeSVG($key, $value);
    }

    $cmd = "fontforge ./fontmaker.pe \"{$filename}\" \"{$fontname_e}\" \"{$fontname_j}\" \"{$authorname}\" \"{$tmp_dir}\"";
    exec($cmd);

    $filepath = "/home/moemoe/maked_fonts/".$tmp_dir."-".$filename.".ttf";
    return $filepath;
  }
  function getTmpDir(){
    $ip = getenv('REMOTE_ADDR');
    $before_string = $ip.$filename.$fontname_e.$fontname_j.$authorname;
    $before_string .= date('ljS\ofFYhisA');
    $after_string = md5($before_string);
    return $after_string;
  }
}