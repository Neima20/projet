$(document).ready(function() {
    // Gestion de la soumission du formulaire
    $('#category-form').on('submit', function(event) {
        event.preventDefault(); // Empêche le formulaire de se soumettre normalement

        var categoryName = $('#category-name').val(); // Récupère le nom de la catégorie

        $.ajax({
            url: "{{ url_for('add_category') }}", // URL de la route Flask pour ajouter une catégorie
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ name: categoryName }), // Envoie le nom de la catégorie en JSON
            success: function(response) {
                // Redirige vers la page des catégories
                window.location.href = '{{ url_for("/categorie") }}';
            },
            error: function(xhr, status, error) {
                console.error('Erreur:', error);
            }
        });
    });

    // Gestion du bouton "Annuler"
    $('#cancel-button').on('click', function() {
        window.location.href = '{{ url_for("html/categorie.html") }}'; // Redirige vers la page des catégories
    });
});
