// Script per mantenere evidenziata la NAV in funzione della pagina attiva -------------------------------------------------

// Ottieni l'URL della pagina corrente
var url = window.location.href;

// Estrai il nome della pagina dal URL (aggiunto +1 altrimenti restituirebbe anche / dell'URL)
var pagina = url.substring(url.lastIndexOf('/') + 1);

// Ottieni il pulsante tramite il suo ID
var pulsanteHome = document.getElementById("homeNav");
var pulsantePersona = document.getElementById("persNav");
var pulsanteOspedale = document.getElementById("ospNav");
var pulsanteVirus = document.getElementById("patoNav");

// Cambia il colore del pulsante in base alla pagina
switch (true) {
    case pagina.includes("index.php"):
        pulsanteHome.style.color = "#0047AB";
        break;
    case pagina === (""):
        pulsanteHome.style.color = "#0047AB";
        break;
    case pagina.includes("cittadino.php"):
        pulsantePersona.style.color = "#0047AB";
        break;
    case pagina.includes("ospedale.php"):
        pulsanteOspedale.style.color = "#0047AB";
        break;
    case pagina.includes("patologia.php"):
        pulsanteVirus.style.color = "#0047AB";
        break;
    default:
        pulsanteHome.style.color = "#a3a2a2";
        pulsantePersona.style.color = "#a3a2a2";
        pulsanteOspedale.style.color = "#a3a2a2";
        pulsanteVirus.style.color = "#a3a2a2";
}

// per non far visualizzare la linea sotto al link delle pagine se si è già in quella pagina
document.addEventListener("DOMContentLoaded", function () {
    var links = document.querySelectorAll("nav ul li a");
    for (var i = 0; i < links.length; i++) {
        if (links[i].href == window.location.href) {
            links[i].classList.add("current-page");
        }
    }
});