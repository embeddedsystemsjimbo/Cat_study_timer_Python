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
zero, the timer switches to the 20 minute “Long Break” state. This marks the complete one timer cycle, where afterwards the timer simply repeats its 
function. Furthermore, there are 2 “Work” related, 4 “Short Break” related and 3 “Long Break” related cat images that are randomly selected to display 
during their respective state.


For more on the Pomodoro study technique: https://en.wikipedia.org/wiki/Pomodoro_Technique






