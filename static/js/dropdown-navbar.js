document.addEventListener("DOMContentLoaded", function() {
    var triggerDropdown = document.getElementById("triggerDropdown");
    var listDropdown = document.getElementById("listDropdown");

    triggerDropdown.addEventListener("click", function(event) {
        event.stopPropagation();
        if (listDropdown.style.display === "none" || listDropdown.style.display === "") {
            listDropdown.style.display = "block";
            triggerDropdown.classList.add("ativo");
        } else {
            listDropdown.style.display = "none";
            triggerDropdown.classList.remove("ativo");
        }
    });

    document.addEventListener("click", function(event) {
        if (!listDropdown.contains(event.target) && event.target !== triggerDropdown) {
            listDropdown.style.display = "none";
            triggerDropdown.classList.remove("ativo");
        }
    });
});