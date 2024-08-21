import random

def create_ladder(participants):
    ladder = []
    for i in range(len(participants) - 1):
        row = [0] * len(participants)
        positions = random.sample(range(len(participants) - 1), k=random.randint(0, len(participants) - 1))
        for pos in positions:
            row[pos] = 1
        ladder.append(row)
    return ladder

def print_ladder(ladder, participants):
    for i in range(len(participants)):
        print(f" {participants[i]} ", end="")
    print()
    for row in ladder:
        for i in range(len(row)):
            if row[i] == 1:
                print("|---", end="")
            else:
                print("|   ", end="")
        print("|")

def play_ladder(ladder, participants):
    result = participants[:]
    for row in ladder:
        for i in range(len(row)):
            if row[i] == 1:
                result[i], result[i + 1] = result[i + 1], result[i]
    return result

participants = ["A", "B", "C", "D"]
ladder = create_ladder(participants)
print("Generated Ladder:")
print_ladder(ladder, participants)
result = play_ladder(ladder, participants)
print("\nFinal Result:")
for i in range(len(participants)):
    print(f"{participants[i]} -> {result[i]}")
