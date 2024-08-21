const words = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
    "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry",
    "strawberry", "tangerine", "ugli", "vanilla", "watermelon", "xigua", "yam", "zucchini",
    // ... more words to make up to 200
];

const shuffledWords = words.sort(() => 0.5 - Math.random()).slice(0, 200);

let currentWordIndex = 0;
let score = 0;
let fallingInterval;

const gameArea = document.getElementById('game-area');
const fallingWord = document.getElementById('falling-word');
const wordInput = document.getElementById('word-input');
const scoreDisplay = document.getElementById('score');
const startButton = document.getElementById('startButton');
const messageBox = document.getElementById('message-box');

function updateMessage(message) {
    messageBox.textContent = message;
}

function startGame() {
    startButton.disabled = true;
    wordInput.disabled = false;
    currentWordIndex = 0;
    score = 0;
    scoreDisplay.textContent = `Score: ${score}`;
    updateMessage('Game Started!');
    showNextWord();
    wordInput.focus();
    fallingInterval = setInterval(moveWordDown, 50);
}

function showNextWord() {
    fallingWord.textContent = shuffledWords[currentWordIndex];
    fallingWord.style.top = '0px';
    wordInput.value = '';
    updateMessage(`Next word: ${shuffledWords[currentWordIndex]}`);
}

function moveWordDown() {
    const top = parseInt(window.getComputedStyle(fallingWord).top);
    if (top < gameArea.clientHeight - 30) {
        fallingWord.style.top = `${top + 2}px`;
    } else {
        clearInterval(fallingInterval);
        fallingWord.textContent = 'Game Over!';
        wordInput.disabled = true;
        startButton.disabled = false;
        updateMessage('Game Over!');
    }
}

wordInput.addEventListener('input', () => {
    if (wordInput.value === shuffledWords[currentWordIndex]) {
        score++;
        currentWordIndex++;
        scoreDisplay.textContent = `Score: ${score}`;
        updateMessage(`Correct! Your score: ${score}`);
        if (currentWordIndex < shuffledWords.length) {
            showNextWord();
        } else {
            clearInterval(fallingInterval);
            fallingWord.textContent = 'Well done! You completed the game!';
            wordInput.disabled = true;
            startButton.disabled = false;
            updateMessage('Well done! You completed the game!');
        }
    }
});

startButton.addEventListener('click', startGame);
