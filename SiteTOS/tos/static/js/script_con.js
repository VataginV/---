function sortContests() {
    const contestContainer = document.getElementById('contestContainer');
    const tiles = Array.from(contestContainer.getElementsByClassName('tile'));
    
    // Получаем выбранный порядок сортировки
    const sortOrder = document.getElementById('sort').value;

    // Сортируем массив контестов по заголовку
    tiles.sort((a, b) => {
        const titleA = a.getAttribute('data-title').toLowerCase();
        const titleB = b.getAttribute('data-title').toLowerCase();

        if (sortOrder === 'asc') {
            return titleA.localeCompare(titleB);
        } else {
            return titleB.localeCompare(titleA);
        }
    });

    // Очищаем контейнер и добавляем отсортированные элементы
    contestContainer.innerHTML = '';
    tiles.forEach(tile => contestContainer.appendChild(tile));
}

// Инициализация сортировки при загрузке страницы
document.addEventListener('DOMContentLoaded', () => {
    sortContests(); // Сортируем по умолчанию
});