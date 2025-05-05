const sentences = [
  "The quick brown fox jumps over the lazy dog.",
  "Typing is a useful skill for everyone.",
  "JavaScript powers interactive websites.",
  "Practice makes perfect in programming."
];

let sentence = sentences[Math.floor(Math.random() * sentences.length)];
document.getElementById("sentence").textContent = sentence;

let startTime = new Date().getTime();

function calculateSpeed() {
  const input = document.getElementById("inputArea").value.trim();
  let endTime = new Date().getTime();
  let timeTaken = (endTime - startTime) / 1000;

  let wordCount = input.split(" ").length;
  let wpm = Math.round(wordCount / (timeTaken / 60));

  let inputWords = input.split(" ");
  let originalWords = sentence.split(" ");
  let correctWords = inputWords.filter((word, index) => word === originalWords[index]).length;
  let accuracy = Math.round((correctWords / originalWords.length) * 100);

  document.getElementById("result").innerText = `WPM: ${wpm}, Accuracy: ${accuracy}%, Time: ${Math.round(timeTaken)} sec`;
}
