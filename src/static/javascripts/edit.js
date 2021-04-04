function handler (i) {
    let popup = document.getElementById("popup");
    popup.style.display = "block";

    document.getElementById("name").setAttribute("value", i.getAttribute('name'));
    document.getElementById("type").setAttribute("value", i.getAttribute('type'));
    document.getElementById("old-grade").setAttribute("value", i.getAttribute('grade'));
}