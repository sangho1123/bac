import tkinter as tk
import random
import time

# 슬롯머신 심볼 리스트
symbols = ["🍒", "🍋", "🍊", "🍉", "⭐", "🔔"]

# GUI 설정
window = tk.Tk()
window.title("Slot Machine")
window.geometry("400x300")

# 슬롯 머신 릴 레이블
reel1 = tk.Label(window, text="🍒", font=("Helvetica", 48))
reel1.pack(side=tk.LEFT, expand=True)

reel2 = tk.Label(window, text="🍋", font=("Helvetica", 48))
reel2.pack(side=tk.LEFT, expand=True)

reel3 = tk.Label(window, text="🍊", font=("Helvetica", 48))
reel3.pack(side=tk.LEFT, expand=True)

# 결과 레이블
result_label = tk.Label(window, text="", font=("Helvetica", 24))
result_label.pack(pady=20)

# 슬롯 머신 회전 애니메이션 함수
def spin_animation(label, duration=2):
    end_time = time.time() + duration
    while time.time() < end_time:
        label.config(text=random.choice(symbols))
        window.update()
        time.sleep(0.1)  # 릴이 회전하는 속도 조절

# 슬롯 머신 스핀 함수
def spin_slot_machine():
    result_label.config(text="스핀 중...")
    window.update()
    
    # 릴 회전 애니메이션
    spin_animation(reel1, 2)
    spin_animation(reel2, 3)
    spin_animation(reel3, 4)
    
    # 최종 결과 확인
    if reel1.cget("text") == reel2.cget("text") == reel3.cget("text"):
        result_label.config(text="축하합니다! 승리했습니다!")
    else:
        result_label.config(text="다시 시도하세요.")

# 스핀 버튼
spin_button = tk.Button(window, text="Spin", font=("Helvetica", 24), command=spin_slot_machine)
spin_button.pack(pady=20)

# GUI 루프 시작
window.mainloop()
