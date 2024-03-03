const sort = "sort"; // Класс для отображения стрелок
const ArrowUp = '<i class="fas fa-caret-up"></i>'
const ArrowDown = '<i class="fas fa-caret-down"></i>'

$(document).ready( function () {
    if ($(".sorting").length > 0){
        let last = $(".sorting").last().index(); // Находим последний столбец в таблице datatable (кнопки)
        $(".sorting").each(function( index, element ){
            if( $(this).index() != last ){
                $(this).append("<span class='"+ sort + "'>"+ ArrowUp + ArrowDown + "</span>"); // Добавляем стрелки для сортировки
            }
        });
    }
 });