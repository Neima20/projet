<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Connexion - TO-DO-LIST</title>
    <link rel="stylesheet" href="../CSS/Connexion.css">
</head>

<body>
    <div class="title">
        <h1>TO-DO-LIST</h1>
    </div>
    <div class="container">
        <div class="image-section">
            <img src="../Images/9.webp" alt="Image de gestion de tâche">
        </div>
        <div class="form-section">
            <?php
            $serveur = "localhost";
            $user = "root";
            $mtp = "";
            $dbs = "gestiondetache";

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

            <form method="POST">
                <h2>Connexion</h2>
                <label for="email">Email :</label>
                <input type="email" id="email" name="email" required>
                <label for="password">Mot de passe :</label>
                <input type="password" id="password" name="password" required>
                <button type="submit">Connexion</button>
                <a href="Inscription.html">S'inscrire</a>
            </form>
        </div>
    </div>
</body>

</html>