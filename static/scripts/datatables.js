$(document).ready(function() {
    var table = $(".datatable").DataTable({
        dom: 'lrtip',
        info: false,
        ordering: true,
        pagingType: "full_numbers",
        lengthMenu: [15],
        lengthChange: false,
        scrollCollapse: true,
        language: {
            emptyTable: "В таблице отсутствуют данные",
            searchPlaceholder: "Поиск...",
            processing: "Загрузка...",
            zeroRecords: "Ничего не найдено",
            paginate: {
                first: "<i class='fas fa-angle-double-left'></i>",
                last: "<i class='fas fa-angle-double-right'></i>",
                next: "<i class='fas fa-angle-right'></i>",
                previous: "<i class='fas fa-angle-left'></i>"
            }
        }
    });

    // Поиск
    $('.search input').on('input', function() {
        var value = this.value;
        if (value === "") {
            table.search(value).draw(); 
        }
    });

    $('#search-button').on('click', function() {
        var value = $('#search-input').val();
        table.search(value).draw();
    });
});
