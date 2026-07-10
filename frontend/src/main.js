async function loadStatus() {
  try {
    const res = await fetch('/api/status');
    const data = await res.json();
    const el = document.getElementById('status');
    el.innerText = JSON.stringify(data, null, 2);
  } catch (e) {
    document.getElementById('status').innerText = 'Error fetching status';
  }
}

loadStatus();
