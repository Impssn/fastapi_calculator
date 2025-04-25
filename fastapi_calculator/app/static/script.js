// async function calculate() {
//     const num1 = document.getElementById("num1").value;
//     const num2 = document.getElementById("num2").value;
//     const op = document.getElementById("op").value;

//     const res = await fetch(`/calculate?num1=${num1}&num2=${num2}&op=${op}`);
//     const data = await res.json();

//     document.getElementById("result").innerText = `Result: ${data.result}`;
// }


function appendToDisplay(value) {
    document.getElementById('display').value += value;
}

function clearDisplay() {
    document.getElementById('display').value = '';
}

function calculateResult() {
    try {
        const result = eval(document.getElementById('display').value);
        document.getElementById('display').value = result;
    } catch (error) {
        alert('Invalid expression');
    }
}
