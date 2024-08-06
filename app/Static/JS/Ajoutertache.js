document.addEventListener('DOMContentLoaded', function() {
    // Tableau de catégories simulé (à remplacer par votre source de données réelle)
    const categories = [
        { id: '1', name: 'Catégorie 1' },
        { id: '2', name: 'Catégorie 2' },
        { id: '3', name: 'Catégorie 3' }
        // Ajoutez d'autres catégories si nécessaire
    ];

    // Sélection de l'élément <select> dans le formulaire
    const categorySelect = document.getElementById('category');

    // Ajout des options dynamiquement à partir du tableau categories
    categories.forEach(function(category) {
        const option = document.createElement('option');
        option.value = category.id;
        option.textContent = category.name;
        categorySelect.appendChild(option);
    });
});
