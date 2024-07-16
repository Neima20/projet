<?php
$serveur = "localhost";
$user = "root";
$mtp = "";
$dbs = "GestiondeTache";

$connect = mysqli_connect($serveur, $user, $mtp, $dbs);

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $email = $_POST["email"];
    $password = $_POST["password"];

    $result = mysqli_query($connect, "SELECT email, password  FROM user WHERE email ='$email' and password='$password'");

    if (mysqli_fetch_row($result) > 0) {
        header("location:../html/tableau.html");
        exit();
    } else {
        echo ("le email_patient ou le mot_de_passe_patient est incorrecte");
    }
}


?>