const windowSize = () => {
    const tab = document.getElementById("tab");
    if (window.innerWidth < 1050)
    {
        tab.classList.remove("tab-wrapper")
    }
    else
    {
        tab.classList.add("tab-wrapper")
    }
}
windowSize();

window.addEventListener("resize", function() {
    const tab = document.getElementById("tab");
    if (window.innerWidth < 1050)
    {
        tab.classList.remove("tab-wrapper")
    }
    else
    {
        tab.classList.add("tab-wrapper")
    }
})