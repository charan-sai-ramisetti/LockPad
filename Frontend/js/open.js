async function openPad() {
  const key = document.getElementById("keyInput").value;

  if (!key) {
    alert("Key required");
    return;
  }

  const res = await fetch("https://lockpad.charansai.me/api/pad/open/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ key })
  });

  if (!res.ok) {
    alert("Invalid key or server error");
    return;
  }

  const data = await res.json();

  // Store temporarily
  sessionStorage.setItem("pad_id", data.id);
  sessionStorage.setItem("key", key);
  sessionStorage.setItem("content", data.content);

  // Go to editor
  window.location.href = "pad.html";
}
