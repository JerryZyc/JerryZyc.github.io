(function () {
  const API_BASE = "http://localhost:5000";

  function createWidget() {
    const container = document.createElement("div");
    container.id = "chat-widget-container";

    // bubble
    const bubble = document.createElement("div");
    bubble.id = "chat-bubble";
    bubble.title = "AI 助手";
    bubble.innerHTML =
      '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>';
    container.appendChild(bubble);

    // panel
    const panel = document.createElement("div");
    panel.id = "chat-panel";

    // header
    const header = document.createElement("div");
    header.id = "chat-header";
    header.innerHTML = '<span>AI 知识助手</span><button id="chat-close">&times;</button>';
    panel.appendChild(header);

    // messages
    const msgs = document.createElement("div");
    msgs.id = "chat-messages";
    const welcome = document.createElement("div");
    welcome.className = "chat-msg chat-msg-bot";
    welcome.textContent = "你好！我是你的个人知识助手，可以帮你查询和整理本站内容。有什么想了解的？";
    msgs.appendChild(welcome);
    panel.appendChild(msgs);

    // input area
    const inputArea = document.createElement("div");
    inputArea.id = "chat-input-area";
    inputArea.innerHTML =
      '<textarea id="chat-input" rows="1" placeholder="输入问题..."></textarea><button id="chat-send">发送</button>';
    panel.appendChild(inputArea);

    container.appendChild(panel);
    document.body.appendChild(container);

    return { container, bubble, panel, msgs };
  }

  const { container, bubble, panel, msgs } = createWidget();
  const closeBtn = document.getElementById("chat-close");
  const input = document.getElementById("chat-input");
  const sendBtn = document.getElementById("chat-send");
  const history = [];

  bubble.addEventListener("click", () => {
    container.classList.add("active");
    input.focus();
  });
  closeBtn.addEventListener("click", () => {
    container.classList.remove("active");
  });

  input.addEventListener("input", () => {
    input.style.height = "auto";
    input.style.height = Math.min(input.scrollHeight, 120) + "px";
  });
  input.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      send();
    }
  });
  sendBtn.addEventListener("click", send);

  async function send() {
    const text = input.value.trim();
    if (!text) return;

    input.value = "";
    input.style.height = "auto";
    addMsg(text, "user");
    history.push({ role: "user", content: text });

    const loadingId = addMsg("思考中...", "loading");
    sendBtn.disabled = true;

    try {
      const res = await fetch(`${API_BASE}/api/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text, history }),
      });
      if (!res.ok) {
        const errData = await res.json().catch(() => ({}));
        throw new Error(errData.detail || `HTTP ${res.status}`);
      }
      const data = await res.json();

      const loadingEl = document.getElementById(loadingId);
      if (loadingEl) loadingEl.remove();

      const reply = data.reply || "（无响应）";
      addMsg(reply, "bot", data.sources);
      history.push({ role: "assistant", content: reply });
    } catch (err) {
      const loadingEl = document.getElementById(loadingId);
      if (loadingEl) loadingEl.textContent = "请求失败: " + err.message;
    } finally {
      sendBtn.disabled = false;
      input.focus();
    }
  }

  function addMsg(text, role, sources) {
    const id = role === "loading" ? "msg-loading-" + Date.now() : null;
    const div = document.createElement("div");
    if (id) div.id = id;
    div.className = "chat-msg chat-msg-" + role;
    div.textContent = text;

    if (sources && sources.length > 0) {
      const srcDiv = document.createElement("div");
      srcDiv.className = "chat-msg-sources";
      srcDiv.textContent = "来源: ";
      const seen = new Set();
      sources.forEach((s) => {
        if (seen.has(s.path)) return;
        seen.add(s.path);
        const a = document.createElement("a");
        a.href = "/" + s.path.replace(/\\/g, "/").replace(/\.md$/i, "/");
        a.textContent = s.title;
        a.target = "_blank";
        srcDiv.appendChild(a);
      });
      div.appendChild(srcDiv);
    }

    msgs.appendChild(div);
    msgs.scrollTop = msgs.scrollHeight;
    return id;
  }
})();
