function calculateMod(attr) {
    const base = parseInt(document.getElementById(`attr_${attr}_base`).value) || 0;
    const race = parseInt(document.getElementById(`attr_${attr}_race`).value) || 0;
    const misc = parseInt(document.getElementById(`attr_${attr}_misc`).value) || 0;

    const total = base + race + misc;
    const mod = Math.floor((total - 10) / 2);

    document.getElementById(`result_${attr}`).innerText = mod.toString();
}