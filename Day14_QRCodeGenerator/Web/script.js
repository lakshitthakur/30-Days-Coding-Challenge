function generateQR() {
  const input = document.getElementById("qrInput").value;
  const qr = new QRious({
    element: document.getElementById("qrCanvas"),
    value: input,
    size: 250
  });
}
