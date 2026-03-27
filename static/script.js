const messageInput = document.querySelector(".message-input");
const chatBody = document.querySelector(".chat-body");
const chatbotToggler = document.querySelector("#chatbot-toggler");
const chatForm = document.getElementById("chat-form");
const closeBtn = document.getElementById("close-chatbot");

const userData = {
    message: null
};

// =========================
// 🧱 CREATE MESSAGE ELEMENT
// =========================
const createMessageElement = (content, ...classes) => {
    const div = document.createElement("div");
    div.classList.add("message", ...classes);
    div.innerHTML = content;
    return div;
};

// =========================
// 🤖 FETCH BOT RESPONSE
// =========================
const generateBotResponse = async (incomingMessageDiv) => {
    const messageTextDiv = incomingMessageDiv.querySelector(".message-text");

    try {
        const response = await fetch("http://127.0.0.1:5000/check", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: userData.message })
        });

        if (!response.ok) throw new Error("Server error");

        const data = await response.json();
        console.log("Backend response:", data);

        // ✅ Conversational reply
        const reply = data.reply || "No response from server";

        messageTextDiv.innerText = reply;

    } catch (error) {
        console.error(error);
        messageTextDiv.innerText = "❌ Unable to connect to server.";
    }

    // remove thinking state
    incomingMessageDiv.classList.remove("thinking");

    // auto scroll
    chatBody.scrollTop = chatBody.scrollHeight;
};

// =========================
// 📤 HANDLE USER MESSAGE
// =========================
const handleOutgoingMessage = (e) => {
    e.preventDefault();

    userData.message = messageInput.value.trim();
    if (!userData.message) return;

    messageInput.value = "";

    // 🧑 Show user message
    const userMessageDiv = createMessageElement(
        `<div class="message-text">${userData.message}</div>`,
        "user-message"
    );

    chatBody.appendChild(userMessageDiv);
    chatBody.scrollTop = chatBody.scrollHeight;

    // 🤖 Show bot "typing"
    setTimeout(() => {
        const botMessageDiv = createMessageElement(
            `<div class="message-text">Typing...</div>`,
            "bot-message",
            "thinking"
        );

        chatBody.appendChild(botMessageDiv);
        chatBody.scrollTop = chatBody.scrollHeight;

        generateBotResponse(botMessageDiv);
    }, 500);
};

// =========================
// ⌨️ ENTER KEY HANDLING
// =========================
messageInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        handleOutgoingMessage(e);
    }
});

// =========================
// 📩 FORM SUBMIT
// =========================
chatForm.addEventListener("submit", handleOutgoingMessage);

// =========================
// 🔘 TOGGLE CHATBOT
// =========================
chatbotToggler.addEventListener("click", () => {
    document.body.classList.toggle("show-chatbot");
});

// =========================
// ❌ CLOSE CHATBOT
// =========================
closeBtn.addEventListener("click", () => {
    document.body.classList.remove("show-chatbot");
});