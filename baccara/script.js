const cardImages = {
    "2C": "2C.png",
    "2D": "2D.png",
    "2H": "2H.png",
    "2S": "2S.png",
    "3C": "3C.png",
    "3D": "3D.png",
    "3H": "3H.png",
    "3S": "3S.png",
    "4C": "4C.png",
    "4D": "4D.png",
    "4H": "4H.png",
    "4S": "4S.png",
    "5C": "5C.png",
    "5D": "5D.png",
    "5H": "5H.png",
    "5S": "5S.png",
    "6C": "6C.png",
    "6D": "6D.png",
    "6H": "6H.png",
    "6S": "6S.png",
    "7C": "7C.png",
    "7D": "7D.png",
    "7H": "7H.png",
    "7S": "7S.png",
    "8C": "8C.png",
    "8D": "8D.png",
    "8H": "8H.png",
    "8S": "8S.png",
    "9C": "9C.png",
    "9D": "9D.png",
    "9H": "9H.png",
    "9S": "9S.png",
    "10C": "10C.png",
    "10D": "10D.png",
    "10H": "10H.png",
    "10S": "10S.png",
    "JC": "JC.png",
    "JD": "JD.png",
    "JH": "JH.png",
    "JS": "JS.png",
    "QC": "QC.png",
    "QD": "QD.png",
    "QH": "QH.png",
    "QS": "QS.png",
    "KC": "KC.png",
    "KD": "KD.png",
    "KH": "KH.png",
    "KS": "KS.png",
    "AC": "AC.png",
    "AD": "AD.png",
    "AH": "AH.png",
    "AS": "AS.png",
};

function getCardKey() {
    const suits = ["C", "D", "H", "S"];
    const values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"];
    const value = values[Math.floor(Math.random() * values.length)];
    const suit = suits[Math.floor(Math.random() * suits.length)];
    return value + suit;
}

function calculateScore(card1, card2) {
    const valueMap = {
        "A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 0, "J": 0, "Q": 0, "K": 0
    };
    const score = (valueMap[card1.slice(0, -1)] + valueMap[card2.slice(0, -1)]) % 10;
    return score;
}

function playGame() {
    const playerCard1 = getCardKey();
    const playerCard2 = getCardKey();
    const bankerCard1 = getCardKey();
    const bankerCard2 = getCardKey();

    const playerScore = calculateScore(playerCard1, playerCard2);
    const bankerScore = calculateScore(bankerCard1, bankerCard2);

    document.getElementById("playerCard1").src = "images/" + cardImages[playerCard1];
    document.getElementById("playerCard2").src = "images/" + cardImages[playerCard2];
    document.getElementById("bankerCard1").src = "images/" + cardImages[bankerCard1];
    document.getElementById("bankerCard2").src = "images/" + cardImages[bankerCard2];

    let result = `Player's Score: ${playerScore}\nBanker's Score: ${bankerScore}\n`;

    if (playerScore > bankerScore) {
        result += "Player wins!";
    } else if (bankerScore > playerScore) {
        result += "Banker wins!";
    } else {
        result += "It's a tie!";
    }

    document.getElementById("result").textContent = result;
}

document.getElementById("playButton").addEventListener("click", playGame);
