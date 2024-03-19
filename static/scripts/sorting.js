$(document).ready(function() {
    const port = "sort"; // Класс для отображения стрелок
    const ArrowUp = '<i class="fas fa-caret-up"></i>';
    const ArrowDown = '<i class="fas fa-caret-down"></i>';

    const $sorting = $(".sorting");

    if ($sorting.length > 0) {
        const lastColumnIndex = $sorting.last().index();

        $sorting.each(function(index, element) {
            const $this = $(this);
            const columnIndex = $this.index();

            if (columnIndex !== lastColumnIndex) {
                $this.append(`<span class="${port}">${ArrowUp}${ArrowDown}</span>`); // Добавляем стрелки для сортировки
            }
        });
    }
});
