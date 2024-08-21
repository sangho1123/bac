const maxSelection = 6;
let selectedNumbers = [];

function generateLottoNumbers() {
    let numbers = [];
    while (numbers.length < 6) {
        let num = Math.floor(Math.random() * 45) + 1;
        if (!numbers.includes(num)) {
            numbers.push(num);
        }
    }
    numbers.sort((a, b) => a - b);
    return numbers;
}

function updateSelectedNumbers(num, button) {
    if (selectedNumbers.includes(num)) {
        selectedNumbers = selectedNumbers.filter(n => n !== num);
        button.classList.remove('selected');
    } else if (selectedNumbers.length < maxSelection) {
        selectedNumbers.push(num);
        button.classList.add('selected');
    }

    document.getElementById('checkButton').disabled = selectedNumbers.length !== maxSelection;
}

function createNumberGrid() {
    const numberGrid = document.getElementById('numberGrid');
    for (let i = 1; i <= 45; i++) {
        let button = document.createElement('button');
        button.innerText = i;
        button.onclick = () => updateSelectedNumbers(i, button);
        numberGrid.appendChild(button);
    }
}

function checkLotto() {
    let generatedNumbers = generateLottoNumbers();
    document.getElementById("generatedLottoNumbers").innerText = "생성된 로또 번호: " + generatedNumbers.join(", ");

    let matchedNumbers = selectedNumbers.filter(num => generatedNumbers.includes(num));
    if (matchedNumbers.length > 0) {
        document.getElementById("result").innerText = "당첨된 번호: " + matchedNumbers.join(", ") + " (" + matchedNumbers.length + "개 맞춤)";
    } else {
        document.getElementById("result").innerText = "아쉽지만, 당첨된 번호가 없습니다.";
    }
}

createNumberGrid();
