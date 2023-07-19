<?php

if(!count($_FILES)) {
    echo 'Файлы не найдены';
    die();
}
if(!isset($_FILES['price'])) {
    echo 'Файл не найдены';
    die();
}

$info = pathinfo($_FILES['price']['name']);
$ext = $info['extension']; // get the extension of the file

if($ext != 'xlsx'){
    echo 'Неверный формат';
    die();
}

if(file_exists(__DIR__.'/import_excel.xlsx')){
    unlink(__DIR__.'/import_excel.xlsx');
}
if(file_exists(dirname(__DIR__).'/admin/uploads/data.json')){
    unlink(dirname(__DIR__).'/admin/uploads/data.json');
}


if(file_exists(dirname(__DIR__).'/admin/uploads/1.xlsx')){
    unlink(dirname(__DIR__).'/admin/uploads/1.xlsx');
}


move_uploaded_file( $_FILES['price']['tmp_name'], __DIR__.'/import_excel.xlsx');

$command = 'python3 ' . __DIR__ . '/excelimport.py';

$command = escapeshellcmd($command);
$output = shell_exec($command);


$json = @json_decode($output, true);
if(is_array($json) && $json['success']) {
    echo '<h2>Доступно для загрузки '. $json['count'] .' </h2>' ;
    echo 'Перйти в постащики для обновления на сайте: <a href="https://profildoors-spb-mall.ru/admin/index.php?route=catalog/suppler">Перейти</a>';
    die();
}

echo json_encode(['success'=>0, 'msg'=>'Error system', 'response'=>$output, 'command'=>$command]);
