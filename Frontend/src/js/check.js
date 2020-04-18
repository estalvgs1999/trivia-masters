/* -------------------------------------------
 * File: check.js
 * Develop by: @estalvgs1999
 * Description: controls events and connect w/
 * backend,related w/ question checking.
 *
 * version 0.1
 * Last edit : 17/4/2020 [21:30]
 *
 * A project by av_software 
 * ------------------------------------------ */

/**
 * 
 */
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