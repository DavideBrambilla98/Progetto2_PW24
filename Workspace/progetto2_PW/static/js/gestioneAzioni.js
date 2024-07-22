// Script per mantenere evidenziata la NAV in funzione della pagina attiva -------------------------------------------------

// Estrai il nome della pagina dal URL (aggiunto +1 altrimenti restituirebbe anche / dell'URL)
var pagina = window.location.pathname;

// Ottieni il pulsante tramite il suo ID
var pulsanteHome = document.getElementById("homeNav");
var pulsantePersona = document.getElementById("persNav");
var pulsanteOspedale = document.getElementById("ospNav");
var pulsanteVirus = document.getElementById("patoNav");

// Cambia il colore del pulsante in base alla pagina
switch (true) {
    case pagina.includes("ricovero"):
        pulsanteHome.style.color = "#0047AB";
        pulsantePersona.style.color = "#a3a2a2";
        pulsanteOspedale.style.color = "#a3a2a2";
        pulsanteVirus.style.color = "#a3a2a2";
        break;
    case pagina.includes("persona"):
        pulsanteHome.style.color = "#a3a2a2";
        pulsantePersona.style.color = "#0047AB";
        pulsanteOspedale.style.color = "#a3a2a2";
        pulsanteVirus.style.color = "#a3a2a2";
        break;
    case pagina.includes("ospedale"):
        pulsanteHome.style.color = "#a3a2a2";
        pulsantePersona.style.color = "#a3a2a2";
        pulsanteOspedale.style.color = "#0047AB";
        pulsanteVirus.style.color = "#a3a2a2";
        break;
    case pagina.includes("patologia"):
        pulsanteHome.style.color = "#a3a2a2";
        pulsantePersona.style.color = "#a3a2a2";
        pulsanteOspedale.style.color = "#a3a2a2";
        pulsanteVirus.style.color = "#0047AB";
        break;
    default:
        pulsanteHome.style.color = "#0047AB";
        pulsantePersona.style.color = "#a3a2a2";
        pulsanteOspedale.style.color = "#a3a2a2";
        pulsanteVirus.style.color = "#a3a2a2";
}
