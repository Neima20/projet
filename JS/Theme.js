document.addEventListener("DOMContentLoaded", function() {
    const themeButtons = document.querySelectorAll(".theme-button");
    
    themeButtons.forEach(button => {
        button.addEventListener("click", function() {
            const color = this.getAttribute("data-color");
            document.documentElement.style.setProperty("--primary-color", color);
            document.documentElement.style.setProperty("--button-hover-color", shadeColor(color, -10));
            localStorage.setItem('themeColor', color);
        });
    });

    const savedColor = localStorage.getItem('themeColor');
    if (savedColor) {
        document.documentElement.style.setProperty("--primary-color", savedColor);
        document.documentElement.style.setProperty("--button-hover-color", shadeColor(savedColor, -10));
    }
});

function shadeColor(color, percent) {
    let R = parseInt(color.substring(1, 3), 16);
    let G = parseInt(color.substring(3, 5), 16);
    let B = parseInt(color.substring(5, 7), 16);

    R = parseInt(R * (100 + percent) / 100);
    G = parseInt(G * (100 + percent) / 100);
    B = parseInt(B * (100 + percent) / 100);

    R = (R < 255) ? R : 255;
    G = (G < 255) ? G : 255;
    B = (B < 255) ? B : 255;

    const RR = ((R.toString(16).length === 1) ? "0" + R.toString(16) : R.toString(16));
    const GG = ((G.toString(16).length === 1) ? "0" + G.toString(16) : G.toString(16));
    const BB = ((B.toString(16).length === 1) ? "0" + B.toString(16) : B.toString(16));

    return "#" + RR + GG + BB;
}
