function DeleteModal() {
    $(".delete-js").click(function () {
      var url = $(this).data("url");
      const modalId = "delete-form";
      var modal = document.getElementById(modalId);
      if (modal == null) {
        modal = document.createElement("section");
        modal.id = modalId;
        modal.className = "modal";
        document.body.appendChild(modal);
      }
  
      fetch(url).then((response) =>
        response.text().then((data) => {
          $(modal).html(data);
          $(modal).fadeIn();
          ModalsWindows();
          
          const forms = document.querySelectorAll("form");
          forms.forEach((form) => {
            form.addEventListener("submit", function (e) {
              e.preventDefault();
              const formData = new FormData(this);
              var url = this.action;
  
              const fetchResp = fetch(url, {
                method: "POST",
                body: formData,
              }).then((response) => {
                if (response.redirected) {
                  window.location.href = response.url;
                } else {
                  response.text().then((data) => {
                    $(modal).html(data);
                    ModalsWindows();
                  });
                }
              });
            });
          });
        })
      );
    });
}
DeleteModal();