$(document).on("click", "#search-button", function() {
    let query = $('#search-input').val();  // Получаем значение поля поиска
    let web_url = '/search/?q=' + query;  // Формируем URL для поискового запроса

    // Выполняем AJAX-запрос
    $.ajax({
        url: web_url,
        method: 'GET',  // Используем метод GET
        success: function(data) {
            // При успешном выполнении запроса заменяем содержимое таблицы результатами поиска
            $('#tableCars tbody').html(data);
        },
        error: function(xhr, status, error) {
            // Обработка ошибок, если они возникнут
            console.error(xhr.responseText);
        }
    });
});
