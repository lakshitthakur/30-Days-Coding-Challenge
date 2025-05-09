document.getElementById('quizForm').addEventListener('submit', function(e) {
  e.preventDefault();

  const answers = ['q1', 'q2', 'q3', 'q4', 'q5'];
  const counts = {};

  answers.forEach(q => {
    const val = document.querySelector(`input[name=${q}]:checked`);
    if (val) {
      counts[val.value] = (counts[val.value] || 0) + 1;
    }
  });

  let result = Object.entries(counts).sort((a, b) => b[1] - a[1])[0];
  let resultText = '';

  switch(result?.[0]) {
    case 'thinker': resultText = "🧠 You are The Thinker! Logical, curious, and insightful."; break;
    case 'artist': resultText = "🎨 You are The Artist! Creative, expressive, and imaginative."; break;
    case 'adventurer': resultText = "🚀 You are The Adventurer! Bold, spontaneous, and daring."; break;
    case 'peacekeeper': resultText = "🧘 You are The Peacekeeper! Calm, thoughtful, and balanced."; break;
    default: resultText = "Please answer all questions!";
  }

  document.getElementById('result').textContent = resultText;
});
