const form = document.getElementById("chat-form");
const messageInput = document.getElementById("message");
const messages = document.getElementById("messages");
const statusText = document.getElementById("status");

function appendMessage(role, text) {
  const article = document.createElement("article");
  article.className = `message ${role}`;

  const paragraph = document.createElement("p");
  paragraph.textContent = text;

  article.appendChild(paragraph);
  messages.appendChild(article);
  messages.scrollTop = messages.scrollHeight;
}

async function sendMessage(message) {
  const response = await fetch("/api/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message }),
  });

  if (!response.ok) {
    throw new Error(`Chat request failed with status ${response.status}`);
  }

  return response.json();
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const message = messageInput.value.trim();
  if (!message) {
    return;
  }

  appendMessage("user", message);
  messageInput.value = "";
  messageInput.focus();
  statusText.textContent = "Thinking...";
  form.querySelector("button").disabled = true;

  try {
    const data = await sendMessage(message);
    appendMessage("bot", data.reply);
    statusText.textContent = "Ready";
  } catch (error) {
    appendMessage("bot", "The request failed. Check the API and try again.");
    statusText.textContent = error instanceof Error ? error.message : "Request failed";
  } finally {
    form.querySelector("button").disabled = false;
  }
});
