function toggleList(index) {
    const list = document.getElementById(`list-${index}`);
    const icon = document.getElementById(`icon-${index}`);
    
    // Проверяем, видим ли мы список
    if (list.classList.contains('open')) {
        list.classList.remove('open'); // Скрываем список
        icon.textContent = '+'; // Меняем значок на "+"
    } else {
        list.classList.add('open'); // Показываем список
        icon.textContent = '-'; // Меняем значок на "-"
        
        // Скрываем другие списки
        for (let i = 1; i <= 3; i++) {
            if (i !== index) {
                document.getElementById(`list-${i}`).classList.remove('open');
                document.getElementById(`icon-${i}`).textContent = '+'; // Меняем значок на "+"
            }
        }
    }
}

// Инициализация всех списков как скрытых
document.querySelectorAll('.tos-list').forEach(list => {
   list.classList.remove('open');
});