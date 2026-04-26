function send() {
            let msg = document.getElementById("msg").value.trim();
            if (!msg) return;

            let chatbox = document.getElementById("chatbox");
            
            // Remove welcome message if exists
            const welcomeMsg = chatbox.querySelector('.welcome-message');
            if (welcomeMsg) {
                welcomeMsg.remove();
            }

            // Add user message
            chatbox.innerHTML += `
                <div class="message user">
                    <div class="message-content">
                        ${escapeHtml(msg)}
                    </div>
                </div>
            `;

            // Show typing indicator
            const typingIndicator = document.createElement('div');
            typingIndicator.className = 'message bot';
            typingIndicator.innerHTML = `
                <div class="typing-indicator" style="display: flex;">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            `;
            chatbox.appendChild(typingIndicator);

            chatbox.scrollTop = chatbox.scrollHeight;
            document.getElementById("msg").value = "";

            fetch("/chat", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({message: msg})
            })
            .then(res => res.json())
            .then(data => {
                // Remove typing indicator
                typingIndicator.remove();

                // Add bot response
                chatbox.innerHTML += `
                    <div class="message bot">
                        <div class="message-content">
                            ${escapeHtml(data.reply)}
                        </div>
                    </div>
                `;
                
                chatbox.scrollTop = chatbox.scrollHeight;
            })
            .catch(error => {
                typingIndicator.remove();
                chatbox.innerHTML += `
                    <div class="message bot">
                        <div class="message-content">
                            Sorry, there was an error processing your request.
                        </div>
                    </div>
                `;
                chatbox.scrollTop = chatbox.scrollHeight;
            });
        }

        function escapeHtml(text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }