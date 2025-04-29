const exchangeRates = {
    USD: { INR: 83.2, EUR: 0.93, USD: 1 },
    INR: { USD: 0.012, EUR: 0.011, INR: 1 },
    EUR: { USD: 1.08, INR: 89.7, EUR: 1 }
};

function convert() {
    const amount = parseFloat(document.getElementById("amount").value);
    const from = document.getElementById("from").value;
    const to = document.getElementById("to").value;
    const resultEl = document.getElementById("result");

    if (isNaN(amount)) {
        resultEl.innerText = "Enter a valid amount.";
        return;
    }

    const rate = exchangeRates[from][to];
    const converted = amount * rate;
    resultEl.innerText = `${amount} ${from} = ${converted.toFixed(2)} ${to}`;
}
