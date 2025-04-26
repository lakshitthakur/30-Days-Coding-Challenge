function calculate() {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    const operator = document.getElementById('operator').value;
    const resultDisplay = document.getElementById('result');
    let result;

    if (isNaN(num1) || isNaN(num2)) {
        resultDisplay.innerText = "Please enter valid numbers.";
        return;
    }

    switch (operator) {
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            if (num2 !== 0)
                result = num1 / num2;
            else {
                resultDisplay.innerText = "Error: Division by zero!";
                return;
            }
            break;
        default:
            resultDisplay.innerText = "Invalid operation!";
            return;
    }

    resultDisplay.innerText = `Result: ${result}`;
}
