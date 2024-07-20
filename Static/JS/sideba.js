document.addEventListener("DOMContentLoaded", function() {
    const menuToggle = document.querySelector(".icons img[src='../Images/menu1.png']");
    const sidebar = document.querySelector(".sidebar");
    const body = document.querySelector("body");

    // Initialiser la barre latérale comme fermée au chargement de la page
    sidebar.classList.add("close");
    body.classList.add("sidebar-closed");

    menuToggle.addEventListener("click", function() {
        sidebar.classList.toggle("close");
        body.classList.toggle("sidebar-closed");
    });

    // Ajouter également la fonctionnalité de bascule pour le mode sombre / clair
    const modeSwitch = document.querySelector(".toggle-switch");

    modeSwitch.addEventListener("click", function() {
        body.classList.toggle("mode");

        if (body.classList.contains("mode")) {
            document.querySelector(".mode-text").textContent = "Mode Clair";
        } else {
            document.querySelector(".mode-text").textContent = "Mode Sombre";
        }
    });
});
