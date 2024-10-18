from pyo import *


# Initialize the pyo server
s = Server().boot()

# Create two simple sounds (you can replace these with your own samples or synthesizers)
sound1 = Sine(freq=440, mul=0.3)  # A4 note
sound2 = Sine(freq=293.66, mul=0.7)  # D4 note

# Create a metro object to control the tempo (120 BPM)
# This is a trigger source. It releases a trigger at the rate of the specified beat
metro = Metro(time=0.5).play()

# Create a counter to keep track of the current beat
# Counter is a class in pyo that outputs a sequence of numbers in a loop.
beat = Counter(metro, min=0, max=8)  

# Create lists to store the patterns for each sound (1 for play, 0 for silence)
pattern1 = [1, 0, 1, 0, 1, 0, 1, 0]
pattern2 = [1, 0, 0, 0, 0, 0, 0, 0]


# Create triggering functions for each sound
def trigger_func1():
    if pattern1[int(beat.get())] == 1:  # Convert to int
        sound1.out()
    else:
        sound1.stop()
    print(beat.get())


def trigger_func2():
    if pattern2[int(beat.get())] == 1:  # Convert to int
        sound2.out()
    else:
        sound2.stop()


# Trigger the sounds based on their patterns
# TrigFunc listens for the trigger (metro) and runs the function (trigger_func1) when triggered
trig1 = TrigFunc(metro, trigger_func1)
trig2 = TrigFunc(metro, trigger_func2)

s.gui(locals())
