// Données de test pour les tâches (à remplacer avec vos données réelles)
let tasks = [
    { id: 1, title: "Faire les courses", description: "Acheter des légumes et du lait." },
    { id: 2, title: "Répondre aux e-mails", description: "Répondre aux e-mails reçus aujourd'hui." },
    { id: 3, title: "Préparer la présentation", description: "Finaliser la présentation pour la réunion." }
];

// Sélecteurs
const taskListContainer = document.getElementById('task-list');
const addTaskForm = document.getElementById('add-task-form');
const taskDetailsModal = document.getElementById('task-details-modal');
const modalTaskTitle = document.getElementById('modal-task-title');
const modalTaskDescription = document.getElementById('modal-task-description');
const editTaskButton = document.getElementById('edit-task-btn');
const deleteTaskButton = document.getElementById('delete-task-btn');
const closeModalButton = document.getElementsByClassName('close')[0];

// Afficher la liste des tâches au chargement de la page
document.addEventListener('DOMContentLoaded', function() {
    displayTasks();
});

// Fonction pour afficher les tâches
function displayTasks() {
    taskListContainer.innerHTML = '';
    tasks.forEach(task => {
        const taskElement = document.createElement('div');
        taskElement.classList.add('task');
        taskElement.innerHTML = `
            <h3>${task.title}</h3>
            <p>${task.description}</p>
            <div class="task-actions">
                <button class="edit-task-btn" data-task-id="${task.id}">Modifier</button>
                <button class="delete-task-btn" data-task-id="${task.id}">Supprimer</button>
            </div>
        `;
        taskListContainer.appendChild(taskElement);
    });

    // Attacher des événements aux boutons d'action des tâches
    attachTaskButtonsEventListeners();
}

// Fonction pour attacher des événements aux boutons d'action des tâches
function attachTaskButtonsEventListeners() {
    const editTaskButtons = document.querySelectorAll('.edit-task-btn');
    const deleteTaskButtons = document.querySelectorAll('.delete-task-btn');

    editTask
