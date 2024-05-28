document.addEventListener("DOMContentLoaded", function() {
    var triggerOption = document.getElementById("triggerOption");
    var listOption = document.getElementById("listOption");

    triggerOption.addEventListener("click", function(event) {
        event.stopPropagation();
        if (listOption.style.display === "none" || listOption.style.display === "") {
            listOption.style.display = "block";
            triggerOption.classList.add("option-ativo");
        } else {
            listOption.style.display = "none";
            triggerOption.classList.remove("option-ativo");
        }
    });

    document.addEventListener("click", function(event) {
        if (!listOption.contains(event.target) && event.target !== triggerOption) {
            listOption.style.display = "none";
            triggerOption.classList.remove("option-ativo");
        }
    });
});