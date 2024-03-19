console.log('Перед определением функции ModalsWindows');
function ModalsWindows() {
    $(document).on("click", ".modal-area, .modal-exit, .cancel-js", function() {
        $(this).closest("section").fadeOut();
        return false;
    });
}
