document.getElementById('colorPicker').addEventListener('input', function () {
  const baseColor = this.value;
  const palette = document.getElementById('palette');
  palette.innerHTML = '';

  for (let i = 1; i <= 5; i++) {
    const shade = shadeColor(baseColor, i * -10);
    const tint = shadeColor(baseColor, i * 10);
    addColorBox(shade);
    addColorBox(tint);
  }
});

function addColorBox(color) {
  const box = document.createElement('div');
  box.className = 'color-box';
  box.style.backgroundColor = color;
  box.textContent = color;
  box.onclick = () => {
    navigator.clipboard.writeText(color);
    alert(`Copied: ${color}`);
  };
  document.getElementById('palette').appendChild(box);
}

function shadeColor(color, percent) {
  let R = parseInt(color.substring(1,3),16);
  let G = parseInt(color.substring(3,5),16);
  let B = parseInt(color.substring(5,7),16);

  R = parseInt(R * (100 + percent) / 100);
  G = parseInt(G * (100 + percent) / 100);
  B = parseInt(B * (100 + percent) / 100);

  R = (R<255)?R:255;
  G = (G<255)?G:255;
  B = (B<255)?B:255;

  const RR = (R.toString(16).padStart(2, '0'));
  const GG = (G.toString(16).padStart(2, '0'));
  const BB = (B.toString(16).padStart(2, '0'));

  return `#${RR}${GG}${BB}`;
}
