async function send() {
    let input = document.getElementById("msg");
    let msg = input.value;

    let chat = document.getElementById("chat");

    chat.innerHTML += `<div class="msg-user">${msg}</div>`;

    let res = await fetch("/ask", {
        method:"POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({message: msg})
    });

    let data = await res.json();

    chat.innerHTML += `<div class="msg-bot">${data.response}</div>`;

    input.value = "";
    chat.scrollTop = chat.scrollHeight;
}

// existing functions
async function sentiment() {
    let text = document.getElementById("sentText").value;

    let res = await fetch("/sentiment", {
        method:"POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({text})
    });

    let data = await res.json();
    document.getElementById("sentOut").innerText = data.result;
}

async function summarize() {
    let text = document.getElementById("sumText").value;

    let res = await fetch("/summarize", {
        method:"POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({text})
    });

    let data = await res.json();
    document.getElementById("sumOut").innerText = data.summary;
}