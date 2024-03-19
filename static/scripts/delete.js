function DeleteModal() {
    $(document).on("click", ".delete-js", function () {
        var url = $(this).data("url");
        const modalId = "delete-form";
        var modal = document.getElementById(modalId);
        if (!modal) {
            modal = document.createElement("section");
            modal.id = modalId;
            modal.className = "modal";
            document.body.appendChild(modal);
        }

        fetch(url)
            .then(response => response.text())
            .then(data => {
                $(modal).html(data).fadeIn();
                ModalsWindows();
                $(modal).find("form").on("submit", function (e) {
                    e.preventDefault();
                    const formData = new FormData(this);
                    var url = this.action;

                    fetch(url, {
                        method: "POST",
                        body: formData
                    })
                    .then(response => {
                        if (response.redirected) {
                            window.location.href = response.url;
                        } else {
                            response.text().then(data => {
                                $(modal).html(data);
                                ModalsWindows();
                            });
                        }
                    });
                });
            });
    });
}

DeleteModal();
