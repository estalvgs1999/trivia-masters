/* -------------------------------------------
 * File: app.js
 * Develop by: @smidvarg
 * Description: controls events and connect w/
 * backend.
 *
 * version 0.1
 * Last edit : 6/4/2020 [20:30]
 *
 * A project by av_software 
 * ------------------------------------------ */



var categories = ["Preguntas", "¿Quién lo dijo?", "Completa la frase"];

var equipo1 = 0;
var equipo2 = 0;

var category = "Preguntas";
var q_level = "facil";


function select_category() {
    category = categories[Math.floor(Math.random() * categories.length)];
    console.log(category);
    document.getElementById("category").setAttribute('value', category);
}

function select_question(level) {
    localStorage.setItem("category", category);
    localStorage.setItem("level", level);
}