<?php
$serveur = "localhost";
$utilisateur = "root";
$motDePasse = "";
$base = "GestiondeTache";
$connect=mysqli_connect($serveur, $utilisateur , $motDePasse,$base);
if (!$connect) {
    die("Échec de la connexion : " . mysqli_connect_error());
}
echo "Connexion réussie <br>";

$id=$_POST["id"];
$email=$_POST["email"];
$password=$_POST["password"];
$nom=$_POST["nom"];
$passwordC=$_POST["passwordC"];

$sql="insert into user values ('$id','$email','$password','$nom' , '$passwordC' )";
if (mysqli_query($connect, $sql)) {
    echo "Les données ont bien été enregistrées dans la
    base données.";
} else {
    echo "Erreur : " . $sql . "<br>" . mysqli_error($connect);
}
//Fermeture de la connexion 
mysqli_close($connect);
?>