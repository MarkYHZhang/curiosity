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

function sendPOST(path, dataDict, onResponseCallback){
    let xhr = new XMLHttpRequest();
    xhr.open("POST", path, true);
    let csrftoken = getCookie('csrftoken');
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            onResponseCallback()
        }
    };
    let data = JSON.stringify(dataDict);
    xhr.send(data);
}

function submitForm(pk=null){
    let question = document.getElementById("questionText").value;
    let answer = document.getElementById("answerText").value;
    let request = {
        "question": question,
        "answer": answer,
    };
    if (pk != null){
        request["pk"] = pk
    }
    let callbackFunction = function () {
        window.location.replace("/");
    };
    sendPOST("write", request, callbackFunction)

}

function deletePost(postPk){
    let request = {"operation":"delete", "pk": postPk};
    let callbackFunction = function () {
        window.location.replace("/manage");
    };
    sendPOST("manage", request, callbackFunction)
}

function editPost(postPk){
    let request = {"operation":"edit", "pk": postPk};
    let callbackFunction = function () {
        window.location.replace("/write?pk="+postPk);
    };
    sendPOST("manage", request, callbackFunction)
}