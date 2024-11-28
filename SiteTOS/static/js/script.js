function toggleMenu(menuId) {
    const menu = document.getElementById(menuId);
    menu.classList.toggle('hidden');
}

document.getElementById('addNewsBtn').addEventListener('click', function() {
    toggleMenu('newsMenu');
});

document.getElementById('addContractBtn').addEventListener('click', function() {
    toggleMenu('contractMenu');
});


function showDetails(contestId) {
    // Получаем данные о конкурсе, например, через AJAX
    fetch(`/api/competitions/${contestId}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('contestTitle').innerText = data.title;
            document.getElementById('contestDescription').innerText = data.text;
            document.getElementById('contestDetails').classList.remove('hidden');
        })
        .catch(error => console.error('Ошибка:', error));
}

function closeDetails() {
    const contestDetails = document.getElementById('contestDetails');
    contestDetails.classList.add('hidden');
}