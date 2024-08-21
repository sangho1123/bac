function createLadder(participants) {
    let ladder = [];
    for (let i = 0; i < participants.length ; i++) {
        let row = Array(participants.length).fill(0);
        
        // 가로줄을 넣을 두 위치를 무작위로 선택
        let randomIndices = [];
        while (randomIndices.length < 2) {
            let randomIndex = Math.floor(Math.random() * (participants.length ));
            // 중복되지 않는 위치에만 가로줄을 추가
            if (!randomIndices.includes(randomIndex)) {
                randomIndices.push(randomIndex);
            }
        }

        // 선택된 위치에 가로줄 추가
        randomIndices.forEach(index => {
            row[index] = 1;
        });

        ladder.push(row);
    }
    return ladder;
}

function displayLadder(ladder) {
    const ladderDiv = document.getElementById("ladder");
    ladderDiv.innerHTML = ''; // Clear previous ladder
    ladder.forEach(row => {
        const rowDiv = document.createElement("div");
        rowDiv.className = "row";
        row.forEach((cell, index) => {
            const cellDiv = document.createElement("div");
            cellDiv.className = "cell";
            if (cell === 1) {
                // 왼쪽 셀과 연결된 가로줄을 추가
                const lineDiv = document.createElement("div");
                lineDiv.className = "line";
                cellDiv.appendChild(lineDiv);
            }
            rowDiv.appendChild(cellDiv);
        });
        ladderDiv.appendChild(rowDiv);
    });
}



function playGame() {
    const participants = ["A", "B", "C", "D"];
    const ladder = createLadder(participants);
    displayLadder(ladder);
    // Here you can add more logic to determine the results
}
