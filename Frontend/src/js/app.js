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

var category = "Preguntas";
var q_level = "facil";
var a_points = 0;
var b_points = 0;

window.onload = async() => {

    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };

    const response = await fetch("http://127.0.0.1:8080/api/v1.0/points", requestOptions);
    const result = await response.json();

    document.getElementById("p1").innerHTML = result["a_points"];
    document.getElementById("p2").innerHTML = result["b_points"];
}


const select_category = async() => {

    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };

    const response = await fetch("http://127.0.0.1:8080/api/v1.0/category", requestOptions);
    const result = await response.json();

    set_category(result);
}


function set_category(result) {

    console.log(result);

    category = result["category"];

    console.log(`cat: ${category}`);
    document.getElementById("category").setAttribute('value', result["category"]);
}

function select_question(level) {
    localStorage.setItem("category", category);
    localStorage.setItem("level", level);
}