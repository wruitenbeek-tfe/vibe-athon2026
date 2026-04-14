const form = document.getElementById("match-form");
const statusNode = document.getElementById("status");
const summaryNode = document.getElementById("results-summary");
const matchesNode = document.getElementById("matches");
const chatThreadNode = document.getElementById("chat-thread");
const chatInputNode = document.getElementById("chat-summary");
const promptChipNodes = document.querySelectorAll("[data-chat-prompt]");

function setStatus(text) {
  statusNode.textContent = text;
}

function setBusy(busy) {
  const button = form.querySelector("button");
  if (button) {
    button.disabled = busy;
  }
}

function appendBubble(role, text) {
  const bubble = document.createElement("article");
  bubble.className =
    role === "user" ? "chat-bubble chat-bubble-user" : "chat-bubble chat-bubble-bot";

  const label = document.createElement("p");
  label.className = "chat-role";
  label.textContent = role === "user" ? "Candidate" : "Matcher bot";

  const body = document.createElement("p");
  body.textContent = text;

  bubble.append(label, body);
  chatThreadNode.appendChild(bubble);
  chatThreadNode.scrollTop = chatThreadNode.scrollHeight;
}

async function submitMessage(summary) {
  const response = await fetch("/api/match/chat-intake", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ summary, answers: [] }),
  });

  if (!response.ok) {
    throw new Error(`Request failed (${response.status})`);
  }

  return response.json();
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  setStatus("Submitting starter turn...");
  setBusy(true);

  try {
    const summary = chatInputNode.value.trim();
    if (!summary) {
      throw new Error("Type a message first.");
    }

    appendBubble("user", summary);
    const data = await submitMessage(summary);
    appendBubble("bot", data.reply);
    chatInputNode.value = "";

    summaryNode.textContent = `Captured profile preview: ${data.profile_preview}`;
    matchesNode.textContent = "Vacancy ranking is still for the team to build.";
    setStatus("Ready");
  } catch (error) {
    summaryNode.textContent = "No results.";
    matchesNode.textContent = "";
    setStatus(error instanceof Error ? error.message : "Request failed");
  } finally {
    setBusy(false);
  }
});

for (const chip of promptChipNodes) {
  chip.addEventListener("click", () => {
    chatInputNode.value = chip.dataset.chatPrompt || "";
    chatInputNode.focus();
  });
}
