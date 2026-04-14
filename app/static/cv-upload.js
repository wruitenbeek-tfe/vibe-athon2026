const form = document.getElementById("match-form");
const statusNode = document.getElementById("status");
const summaryNode = document.getElementById("results-summary");
const matchesNode = document.getElementById("matches");
const fileInput = document.getElementById("cv-file");
const notesInput = document.getElementById("cv-notes");

function setStatus(text) {
  statusNode.textContent = text;
}

function setBusy(busy) {
  const button = form.querySelector("button");
  if (button) {
    button.disabled = busy;
  }
}

function showResponse(reply, preview) {
  summaryNode.textContent = reply;
  matchesNode.textContent = `Captured profile preview: ${preview}`;
}

async function readFileAsText(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => resolve(String(reader.result || ""));
    reader.onerror = () => reject(new Error("Could not read file."));
    reader.readAsText(file);
  });
}

async function submitCV(payload) {
  const response = await fetch("/api/match/cv-upload", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    throw new Error(`Request failed (${response.status})`);
  }

  return response.json();
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  setStatus("Submitting starter intake...");
  setBusy(true);

  try {
    const file = fileInput.files?.[0];
    if (!file) {
      throw new Error("Select a CV file.");
    }

    const content = (await readFileAsText(file)).trim();
    if (!content) {
      throw new Error("The selected file is empty.");
    }

    const data = await submitCV({
      filename: file.name,
      content,
      notes: notesInput.value,
    });

    showResponse(data.reply, data.profile_preview);
    setStatus("Ready");
  } catch (error) {
    summaryNode.textContent = "No results.";
    matchesNode.textContent = "";
    setStatus(error instanceof Error ? error.message : "Request failed");
  } finally {
    setBusy(false);
  }
});
