const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");

function addMessage(text, sender) {
    const message = document.createElement("div");
    message.classList.add("message", sender);
    message.innerText = text;
    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;

    addMessage(message, "user");
    userInput.value = "";

    // Typing indicator
    addMessage("Typing...", "bot");

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message })
    })
    .then(res => res.json())
    .then(data => {
        chatBox.removeChild(chatBox.lastChild);
        addMessage(data.reply, "bot");
    })
    .catch(() => {
        chatBox.removeChild(chatBox.lastChild);
        addMessage(" Error connecting to server", "bot");
    });
}

// Send on Enter key
userInput.addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});
