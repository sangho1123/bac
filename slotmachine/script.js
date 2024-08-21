let balance = 1000;  // 초기 자금 설정
const betAmount = 10;  // 스핀 당 걸리는 금액
const winAmount = 1000;  // 당첨 시 지급 금액
let autoSpinInterval;
let isAutoSpinActive = false;

const symbols = ["🍒", "🍋", "🍊", "🍉", "⭐", "🔔"];
const reel1 = document.getElementById("reel1");
const reel2 = document.getElementById("reel2");
const reel3 = document.getElementById("reel3");
const result = document.getElementById("result");
const balanceDisplay = document.getElementById("balance");
const spinButton = document.getElementById("spinButton");
const autoSpinButton = document.getElementById("autoSpinButton"); 

// 랜덤한 10개의 심볼을 생성하는 함수
function generateRandomSymbols() {
    let randomSymbols = [];
    for (let i = 0; i < 10; i++) {
        randomSymbols.push(symbols[Math.floor(Math.random() * symbols.length)]);
    }
    return randomSymbols;
}

// 릴에 랜덤한 심볼을 설정하는 함수
function setReelSymbols(reel) {
    const randomSymbols = generateRandomSymbols();
    reel.innerHTML = randomSymbols.map(sym => `<div>${sym}</div>`).join('');
}

// 특정 릴을 멈추고 최종적으로 보이는 심볼을 추출하는 함수
function stopReelAndGetTopSymbol(reel) {
    reel.style.animation = "none";  // 애니메이션을 중지
    reel.style.transform = `translateY(0)`;  // 릴을 최상단으로 고정
    // 릴에서 첫 번째로 보이는 심볼을 반환
    return reel.children[0].textContent;
}

function updateBalance(amount) {
    balance += amount;
    balanceDisplay.textContent = `Balance: $${balance}`;
}

function showSuccessAnimation(message) {
    result.textContent = message;
    result.classList.add("success-animation");

    setTimeout(() => {
        result.classList.remove("success-animation");
    }, 3000);  
}

function spinSlotMachine() {

    if (balance < betAmount) {
        result.textContent = "Insufficient funds!";
        return;
    }

    updateBalance(-betAmount);

    result.textContent = "Spinning...";
    spinButton.disabled = true;


    setReelSymbols(reel1);
    setReelSymbols(reel2);
    setReelSymbols(reel3);

    reel1.style.animation = "spin 1s infinite";
    reel2.style.animation = "spin 1.5s infinite";
    reel3.style.animation = "spin 2s infinite";

    
    setTimeout(() => {
        const topSymbol1 = stopReelAndGetTopSymbol(reel1); 
        setTimeout(() => {
            const topSymbol2 = stopReelAndGetTopSymbol(reel2); 
            setTimeout(() => {
                const topSymbol3 = stopReelAndGetTopSymbol(reel3); 

                if (topSymbol1 === topSymbol2 && topSymbol1 === topSymbol3) {
                    updateBalance(winAmount);
                    result.textContent = `Congratulations! You won with ${topSymbol1}!`;
                } else {
                    result.textContent = "Try again!";
                }

                spinButton.disabled = false;
            }, 500); 
        }, 500); 
    }, 500);  
}

function startAutoSpin() {
    if (!isAutoSpinActive) {
        autoSpinInterval = setInterval(spinSlotMachine, 4000); // 4초 간격으로 스핀
        isAutoSpinActive = true;
        autoSpinButton.textContent = "Stop Auto Spin";  // 버튼 텍스트 변경
    }
}


function stopAutoSpin() {
    clearInterval(autoSpinInterval);
    isAutoSpinActive = false;
    autoSpinButton.textContent = "Auto Spin";  // 버튼 텍스트 복구
}

autoSpinButton.addEventListener("click", () => {
    if (isAutoSpinActive) {
        stopAutoSpin();
    } else {
        startAutoSpin();
    }
});

spinButton.addEventListener("click", spinSlotMachine);
