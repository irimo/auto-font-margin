<?php
// makeFont.function.php
// 2013.03.29 syohan
// https://github.com/irimo/fonttt

require_once(DIRNAME(__FILE__)."/imageconvert.class.php");

class MakeFont{
  public static function make($filename, $fontname_e, $fontname_j, $authorname, $files){
    $tmp_dir = self::getTmpDir();
    $obj = new ImageConvert($tmp_dir);
    foreach($files as $key => $value){
      if(!isset($value))die("画像ファイルが読み込めません。");
      $obj->makeSVG($key, $value);
    }

    $cmd = "fontforge ./fontmaker.pe \"{$filename}\" \"{$fontname_e}\" \"{$fontname_j}\" \"{$authorname}\" \"{$tmp_dir}\"";
    exec($cmd);

    $filepath = "./maked_fonts/fonts/".$tmp_dir."/".$filename.".ttf";
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