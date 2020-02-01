function auto_grow(element) {
    element.style.height = "59.7777px";
    element.style.height = (element.scrollHeight)+"px";
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function submitForm(){
    let question = document.getElementById("questionText").value
    let answer = document.getElementById("answerText").value
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "write", true);
    var csrftoken = getCookie('csrftoken');
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            window.location.replace("/");
        }
    };
    let data = JSON.stringify({"question": question, "answer": answer});
    xhr.send(data);
}