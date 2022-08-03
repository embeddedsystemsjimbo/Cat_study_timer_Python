## Cat_study_timer_Python_Tkinter ##

***

To run the cat timer, execute "Python3 main.py" from terminal.

***

This is a study timer created with Python using the “tkinter” graphics module. The study timer enforces the principles of the “Pomodoro” study technique, 
which states that we work more efficiently when we break down large projects into smaller actionable tasks. Consequently, by working in 25-minute intervals
with a 5-minute rest in between intervals and a larger 20 mins rest after 4 work sessions, a person works more productively by avoiding distraction and 
working past the point of optimal production. 

For more on the Pomodoro study technique: https://en.wikipedia.org/wiki/Pomodoro_Technique

***

## Timer functionality breakdown: ##


The “Start” button starts the timer and the “Reset” button resets the timer. The timer beings at 25 minutes in the “Work” state and counts down to zero, afterwards switching to the “Short Break” state. Between each state transistion there is an "cat meow" audio clip that is played to indicated that the counter has reached zero. The “Short Break” state begins at 5 minute and counts down to zero, switching back to and repeating the “Work” state. This cycle repeats 4 times, where after the timer counts down to zero, the timer switches to the 20 minute “Long Break” state. The completion of the "Long Break"  indicates the completion of one entire "Pomodoro Study Technique" cycle, where afterwards the timer simply repeats its functionality. After each 25 minute work and 5 minute break cycle, a checkmark icon indicates to the user which "Work" interval out of a possible 4 the timer is counting down from. Furthermore, there are 2 “Work” related, 4 “Short Break” related and 3 “Long Break” related cat images that are randomly selected to display during their respective state.

***

<img width="891" alt="image" src="https://user-images.githubusercontent.com/76194492/179369668-b80056e0-ba6d-40bd-b3f0-facb98ce3638.png">

Figure 1: Start Menu

***


<img width="891" alt="image" src="https://user-images.githubusercontent.com/76194492/179369674-a95b31b6-6c43-4f16-ac72-437d91119139.png">

Figure 2: Work Timer State

***


<img width="891" alt="image" src="https://user-images.githubusercontent.com/76194492/179369745-dce5f354-6b3d-4377-9001-eeee751e7526.png">

Figure 3: Break State

