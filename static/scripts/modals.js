function ModalsWindows(){
    $(".modal-area,.modal-exit,.cancel-js").click(function(){
        $(this).closest("section").fadeOut();
        return false;
    });
}