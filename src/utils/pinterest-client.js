const API_BASE =
  (typeof process !== "undefined" &&
    process.env.REACT_APP_API_BASE) ||
  "http://localhost:3000";

export async function fetchStatus() {
  try {
    const res = await fetch(${API_BASE}/api/pinterest/status);
    if (!res.ok) throw res;
    return res.json();
  } catch (e) {
    return { status: "unknown", queue: 0, last: "error" };
  }
}

export async function fetchLogs() {
  try {
    const res = await fetch(${API_BASE}/api/pinterest/logs);
    if (!res.ok) throw res;
    return res.text();
  } catch (e) {
    return "// logs unreachable";
  }
}

export async function trigger(action) {
  try {
    const res = await fetch(${API_BASE}/api/pinterest/, {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ action }),
    });
    return res.json();
  } catch (e) {
    return { ok: false };
  }
}

