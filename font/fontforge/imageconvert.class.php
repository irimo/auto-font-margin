<?php
class ImageConvert {
  var $dir;
  var $bmpDir;
  var $bmpPath;
  var $processDir;
  function __construct($dir){ 
    $this->dir = $dir;
    $this->bmpDir = "./maked_fonts/bmps/";
    $this->processDir = "./maked_fonts/processimgs/";
  }
/* private */
  function setBMP($file){
    if(file_exists($file) && filesize($file)){
      exec("mkdir {$this->bmpDir}{$this->dir}");
      $this->bmpPath = "{$this->bmpDir}{$this->dir}/".basename($file);
      if(!file_exists($this->bmpPath) || filesize($this->bmpPath) === 0){
        $cmd = "cp {$file} {$this->bmpPath}";
        exec($cmd);
      }
      return true;
    } else {
      return false;
    }
  }
  

  public function makeSVG($code, $file){
    if($this->setBMP($file) === false) return false;
    exec("mkdir {$this->processDir}{$this->dir}");
    exec("mkdir  ./maked_fonts/fonts/{$this->dir}");  // fontmaker.pe で使う
    
    $cmd_pgm = "convert {$this->bmpPath} {$this->processDir}{$this->dir}/{$code}.pgm";
    $cmd_svg = "potrace -s -a 1 -k 0.9 {$this->processDir}{$this->dir}/{$code}.pgm -W10cm -H 10cm";
    exec($cmd_pgm);
    exec($cmd_svg);
    return true;
  }
}