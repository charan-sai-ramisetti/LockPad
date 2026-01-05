const pad = document.getElementById("pad");
let isDirty = false;

pad.value = sessionStorage.getItem("content") || "";

pad.addEventListener("input", () => {
  isDirty = true;
});

async function savePad() {
  await fetch("https://lockpad.charansai.me/api/pad/open/", {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      key: sessionStorage.getItem("key"),
      content: pad.value
    })
  });

  isDirty = false;
}

async function saveAndExit() {
  await savePad();
  exit();
}

function closePad() {
  if (isDirty && !confirm("You have unsaved changes. Close anyway?")) {
    return;
  }
  exit();
}

function exit() {
  sessionStorage.clear();
  window.location.href = "index.html";
}

/* TAB CLOSE / REFRESH WARNING */
window.addEventListener("beforeunload", (e) => {
  if (isDirty) {
    e.preventDefault();
    e.returnValue = "";
  }
});
