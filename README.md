# Cat_study_timer_python_tkinter

Run from terminal by executing command “python 3 main.py”


This is a study timer created with Python using the “tkinter” graphics module. The study timer enforces the principles of the “Pomodoro” study technique, 
which states that we work more efficiently when we break down large projects into smaller actionable tasks. Consequently, by working in 25-minute intervals
with a 5-minute rest in between intervals and a larger 20 mins rest after 4 work sessions, a person works more productively by avoiding distraction and 
working past the point of optimal production. 

Timer functionality breakdown:

The “Start” button starts the timer and the “Reset” button resets the timer.
The timer beings at 25 minutes in the “Work” state and counts down to zero, afterwards switching to the “Short Break” state. The “Short Break” state begins
at 5 minute and counts down to zero, switching back to and repeating the “Work” state. This cycle repeats 4 times, where after the timer counts down to 
zero, the timer switches to the 20 minute “Long Break” state. This indicates the completion of one entire timer cycle, where afterwards the timer simply repeats its functionality. After each 25 minute work and 5 minute break cycle, a checkmark icon indicates to the user which "Work" interval out of a possible 4 the timer is counting down from. Furthermore, there are 2 “Work” related, 4 “Short Break” related and 3 “Long Break” related cat images that are randomly selected to display during their respective state.


For more on the Pomodoro study technique: https://en.wikipedia.org/wiki/Pomodoro_Technique



<img width="1188" alt="image" src="https://user-images.githubusercontent.com/76194492/179327119-01f6fbde-8611-435a-a5fd-00255cb3ffd2.png">
Figure 1: Start Menu

<img width="1188" alt="image" src="https://user-images.githubusercontent.com/76194492/179327133-d99a9adb-8e96-4599-bcc0-021de3a921f3.png">
Figure 2: Work Timer State

<img width="1188" alt="image" src="https://user-images.githubusercontent.com/76194492/179327160-e318c31c-987b-40f1-a031-11e455463cf4.png">
Figure 3: Break State

