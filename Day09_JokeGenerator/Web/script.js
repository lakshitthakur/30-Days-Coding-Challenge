function getJoke() {
  fetch("https://official-joke-api.appspot.com/random_joke")
    .then(res => res.json())
    .then(data => {
      document.getElementById("setup").textContent = data.setup;
      document.getElementById("punchline").textContent = data.punchline;
    })
    .catch(() => {
      document.getElementById("setup").textContent = "Failed to load joke.";
      document.getElementById("punchline").textContent = "";
    });
}
