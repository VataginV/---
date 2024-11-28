function downloadDocument(fileUrl) {
    // Создаем ссылку на файл
    const link = document.createElement('a');
    link.href = fileUrl; // Используем URL файла
    link.download = ''; // Указываем пустое значение, чтобы браузер использовал имя файла из URL
    document.body.appendChild(link);
    link.click(); // Имитируем клик по ссылке
    document.body.removeChild(link); // Удаляем ссылку после скачивания
}
function filterTable() {
    const input = document.getElementById('searchInput');
    const filter = input.value.toLowerCase(); // Приводим к нижнему регистру
    const table = document.getElementById('documentBody');
    const rows = table.getElementsByTagName('tr');

    for (let i = 0; i < rows.length; i++) {
        const cells = rows[i].getElementsByTagName('td');
        let found = false;

        // Проверяем ячейку с названием файла (вторая ячейка)
        if (cells[1]) { // Ячейка с названием
            const fileName = cells[1].textContent || cells[1].innerText;
            if (fileName.toLowerCase().indexOf(filter) > -1) {
                found = true;
            }
        }

        // Проверяем ячейку с именем автора (третья ячейка)
        if (cells[2]) { // Ячейка с автором
            const authorName = cells[2].textContent || cells[2].innerText;
            if (authorName.toLowerCase().indexOf(filter) > -1) {
                found = true;
            }
        }

        // Показываем или скрываем строку в зависимости от результата поиска
        rows[i].style.display = found ? "" : "none";
    }
}

function sortTable() {
    const table = document.getElementById('documentBody');
    const rows = Array.from(table.getElementsByTagName('tr'));
    const sortValue = document.getElementById('sortSelect').value;

    // Убираем заголовок из массива строк
    rows.shift();

    if (sortValue === "az") {
        // Сортировка по названию (А-Я)
        rows.sort((a, b) => {
            const nameA = a.cells[1].textContent.toLowerCase();
            const nameB = b.cells[1].textContent.toLowerCase();
            return nameA.localeCompare(nameB);
        });
    } else if (sortValue === "za") {
        // Сортировка по названию (Я-А)
        rows.sort((a, b) => {
            const nameA = a.cells[1].textContent.toLowerCase();
            const nameB = b.cells[1].textContent.toLowerCase();
            return nameB.localeCompare(nameA);
        });
    } else if (sortValue === "newest") {
        // Сортировка по дате (Новинки)
        rows.sort((a, b) => {
            return b.getAttribute('data-date') - a.getAttribute('data-date');
        });
    } else if (sortValue === "oldest") {
        // Сортировка по дате (Старые)
        rows.sort((a, b) => {
            return a.getAttribute('data-date') - b.getAttribute('data-date');
        });
    }

    // Добавляем отсортированные строки обратно в таблицу
    rows.forEach(row => table.appendChild(row));
}