document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('newsSearch');
    const gridItems = document.querySelectorAll('.grid-item');

    searchInput.addEventListener('input', function() {
        const query = searchInput.value.toLowerCase();
        
        gridItems.forEach(item => {
            const title = item.querySelector('h2').textContent.toLowerCase();
            const description = item.querySelector('.info-text p').textContent.toLowerCase();

            if (title.includes(query) || description.includes(query)) {
                item.style.display = '';
            } else {
                item.style.display = 'none';
            }
        });
        
        // Если поле пустое, показываем все элементы
        if (query === '') {
            gridItems.forEach(item => {
                item.style.display = '';
            });
        }
    });
});