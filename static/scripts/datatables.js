var tablelength = 15;
var pag = 'lrtip';
$(document).ready( function () {
    var tableid = $(".datatable").attr("id"); // Получаем таблицу
    var table = $("#" + tableid).DataTable({
        dom: 'lrtip',
        info: false,
        ordering: true,
        pagingType: "full_numbers",
        lengthMenu: [ tablelength,],
        lengthChange: false,
        scrollCollapse : true,
        language:{
            emptyTable: "В таблице отсутствуют данные",
            searchPlaceholder: "Поиск...",
            processing: "Загрузка...",
            zeroRecords: "Ничего не найдено",
            paginate: {
                "first":      "<i class='fas fa-angle-double-left'></i>",
                "last":       "<i class='fas fa-angle-double-right'></i>",
                "next":       "<i class='fas fa-angle-right'></i>",
                "previous":   "<i class='fas fa-angle-left'></i>"
            },
        },
    });
    // Поиск
    $('.search input').on('change paste keyup', function() {
        value = this.value;
        if (value == ""){
            table.search(value).draw(); 
        }
    });
    $('#search-button').on('click', function() {
        value = $('#search-input').val()
        table.search(value).draw();
    });
});