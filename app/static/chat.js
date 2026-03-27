const form = document.getElementById("chat-form");
const messageInput = document.getElementById("message");
const messages = document.getElementById("messages");
const matchesContainer = document.getElementById("matches");
const resultsSummary = document.getElementById("results-summary");
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

function renderMatches(matches) {
  matchesContainer.replaceChildren();

  if (!matches.length) {
    resultsSummary.textContent = "No strong vacancy match yet.";
    return;
  }

  resultsSummary.textContent = `${matches.length} vacancy match(es) ranked by relevance.`;

  for (const match of matches) {
    const card = document.createElement("article");
    card.className = "match-card";

    const title = document.createElement("h4");
    title.textContent = match.vacancy.job_title;

    const description = document.createElement("p");
    description.textContent = match.vacancy.job_description;

    const meta = document.createElement("p");
    meta.className = "match-meta";
    meta.textContent =
      `${match.vacancy.location} • ${match.vacancy.employment_type} • ` +
      `${match.vacancy.experience_level} • ${match.vacancy.education_level}`;

    const reasons = document.createElement("p");
    reasons.className = "match-reasons";
    reasons.textContent = `Why it matched: ${match.reasons.join(", ")}`;

    const skills = document.createElement("div");
    skills.className = "match-badges";
    for (const skill of match.vacancy.required_skills) {
      const badge = document.createElement("span");
      badge.className = "badge";
      badge.textContent = skill;
      skills.appendChild(badge);
    }

    card.append(title, description, meta, reasons, skills);
    matchesContainer.appendChild(card);
  }
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
    renderMatches(data.matches);
    statusText.textContent = "Ready";
  } catch (error) {
    appendMessage("bot", "The request failed. Check the API and try again.");
    renderMatches([]);
    statusText.textContent = error instanceof Error ? error.message : "Request failed";
  } finally {
    form.querySelector("button").disabled = false;
  }
});
