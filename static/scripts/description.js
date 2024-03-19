$(document).on("click", ".description-js", function() {
    let url = $(this).data("url");
    const modalId = "description-form";
    let modal = $("#" + modalId);

    if (!modal.length) {
        modal = $("<section></section>", {
            id: modalId,
            class: "modal"
        }).appendTo("body");
    }

    fetch(url)
        .then(response => response.text())
        .then(data => {
            modal.html(data).fadeIn();
            ModalsWindows();

            modal.find("form").on("submit", function(e) {
                e.preventDefault();
                const formData = new FormData(this);
                let actionUrl = this.action;

                fetch(actionUrl, {
                    method: "POST",
                    body: formData
                }).then(response => {
                    if (response.redirected) {
                        window.location.href = response.url;
                    } else {
                        response.text().then(data => {
                            modal.html(data);
                            ModalsWindows();
                        });
                    }
                });
            });
        });

    return false;
});
