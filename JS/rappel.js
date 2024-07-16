document.addEventListener('DOMContentLoaded', function() {
    const taskForm = document.getElementById('taskForm');
    const taskList = document.getElementById('taskList');

    taskForm.addEventListener('submit', function(event) {
        event.preventDefault();
        
        // Récupération des valeurs du formulaire
        const category = document.getElementById('category').value;
        const task = document.getElementById('task').value;
        const startDate = document.getElementById('startDate').value;
        const endDate = document.getElementById('endDate').value;

        // Création d'un élément tâche
        const taskElement = document.createElement('div');
        taskElement.classList.add('task');
        taskElement.innerHTML = `
            <h3>${task}</h3>
            <p><strong>Catégorie:</strong> ${category}</p>
            <p><strong>Date de Début:</strong> ${startDate}</p>
            <p><strong>Date de Fin:</strong> ${endDate}</p>
        `;

        // Ajout de la nouvelle tâche à la liste
        taskList.appendChild(taskElement);

        // Réinitialisation du formulaire
        taskForm.reset();
    });
});
