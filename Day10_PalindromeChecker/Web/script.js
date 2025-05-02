function checkPalindrome() {
  const input = document.getElementById("inputText").value;
  const cleaned = input.toLowerCase().replace(/[^a-z0-9]/g, '');
  const reversed = cleaned.split('').reverse().join('');
  const result = document.getElementById("result");

  if (cleaned === "") {
    result.textContent = "Please enter valid text.";
    return;
  }

  result.textContent = cleaned === reversed
    ? "✅ It's a palindrome!"
    : "❌ Not a palindrome.";
}
