import time

def countdown_timer(seconds):
    while seconds:
        print(f"Time left: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

def countdown_timer_program():
    seconds = int(input("Enter the countdown time in seconds: "))
    countdown_timer(seconds)

countdown_timer_program()
