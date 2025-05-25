# timer checks my face every 5 secons to see if iam available or not
import time
from facedetector import face_detection

def pomodoro_face_tracker(check_interval = 5 ,max_missed = 5): #This will check the function again and again at 10 sectords interval 
    missed_checks = 0
    print("Starting Pomodoro Face Tracker. Press Ctrl+C to stop.")
    while True:
        detected = face_detection()
        if detected:
            print('Face Detected Sucessfully...')
            missed_checks = 0
        else:
            missed_checks += 1 #adds to the missed check
            print(f"No face detected! Missed count: {missed_checks}")
        if missed_checks >= max_missed:
            print("You've been away too long! Take a break or reset timer.")
            exit()
        time.sleep(check_interval) # checks at every 10 secs
if __name__ == "__main__":
    pomodoro_face_tracker()        