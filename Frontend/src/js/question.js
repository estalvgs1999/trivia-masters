var question;
var answer;
var level;


window.onload = async() => {

    category = localStorage.getItem("category");
    level = localStorage.getItem("level");

    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({ "category": category, "level": level });

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    const response = await fetch("http://127.0.0.1:8080/api/v1.0/question", requestOptions);
    const json = await response.json();

    question = json["question"];

    document.getElementById("p1").innerHTML = json["a_points"];
    document.getElementById("p2").innerHTML = json["b_points"];

    set_options();
}

function set_options() {

    document.getElementById("question").innerHTML = question['enunciado'];
    document.getElementById("a").innerHTML = question['opciones']['a'];
    document.getElementById("b").innerHTML = question['opciones']['b'];
    document.getElementById("c").innerHTML = question['opciones']['c'];
    document.getElementById("d").innerHTML = question['opciones']['d'];
}

function set_answer(ans) {
    answer = ans;
    console.log(ans);
}

const validate_answer = async() => {

    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({ "answer": answer, "question": question });

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    const response = await fetch("http://127.0.0.1:8080/api/v1.0/answer", requestOptions);
    const json = await response.json();

    localStorage.setItem("level", level);

    if (json["state"]) {
        location.href = '../html/correct_index.html';
    } else {
        location.href = '../html/incorrect_index.html';
    }


}