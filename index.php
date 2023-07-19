<?php

?>
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Import</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
</head>
<body>
<div class="container">

    <div class="px-4 py-5 my-5">
        <h1 class="display-5 fw-bold text-body-emphasis  text-center">Загрзучик товаров</h1>
        <div class="col-lg-6 mx-auto">
            <p class="lead mb-4">

            </p>

            <ol>
                <li>Прайс необходимо загрузить в форму</li>
                <li>Нажать кнопку обновить загрузочный файл (Результат выдас актуальное кол-во товаров)</li>
                <li>Далее переходим в админку, и запускаем загрузку товаров новых товаров<br>
                <img src="doc1.png" style="width: 100%">
                </li>
                <li>Дождаться рузультата и кнопкой ниже создать товарные предложения</li>
                <li>Скрипт может выдавать ошибку но в фоне дойдет, проверить можно кнопкой</li>
            </ol>

            <h2 class="mt-5">Форма загрузки прайса</h2>
            <form action="/import/create-offers.php" enctype="multipart/form-data" method="post" class="mb-5">
                <div class="mb-4">
                    <input type="file" name="price" >
                </div>
                <button type="submit"  class="btn btn-primary btn-lg px-4 gap-3">Обновить загрузочный файл</button>

            </form>

            <div class="d-grid gap-2 d-sm-flex justify-content-sm-center">
                <a href="/admin/index.php?route=mp/offer/import&user_token=2jce8eJk1nNzbJefVbXw4cDlyP3F9Whx&force=1" type="button" class="btn btn-success btn-lg px-4">Обновить товарные предложения</a>
                <a href="/admin/index.php?route=mp/offer/import&user_token=2jce8eJk1nNzbJefVbXw4cDlyP3F9Whx" type="button" class="btn btn-success btn-lg px-4">Проверить</a>
            </div>
        </div>
    </div>

</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>
</body>
</html>