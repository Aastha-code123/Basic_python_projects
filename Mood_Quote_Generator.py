from tkinter import *
from tkinter import ttk
import random  # Needed for random choice

window = Tk()
window.title("Mood Quote Generator")
window.geometry("500x400")
window.resizable(0, 0)
window.configure(bg="white")

# Title Label
label = Label(
    window,
    text="Mood Quote Generator",
    bg="white",
    fg="#B40AE8",
    font=("Montserrat", 20, "bold")
)
label.pack(pady=10)

# Prompt Label
label1 = Label(
    window,
    text="How are you feeling today?",
    bg="white",
    fg="#0F0F0F",
    font=("Lora", 15, "bold")
)
label1.pack(pady=20)

# Combobox for moods
select_mood = StringVar()
mood = ttk.Combobox(
    window,
    textvariable=select_mood,
    values=["Happy", "Sad", "Excited", "Angry", "Calm" , "Romantic" , "Motivated" , "Stressed"],
    state="readonly",
    font=("La Luxes", 12)
)
mood.pack(pady=20)

# Quote Label
quote_label = Label(
    window, 
    text="",
    bg="white",
    fg="#6A0DAD",
    font=("Arial", 13, "italic"),
    wraplength=420,
    justify="center"
)
quote_label.pack(pady=20)

# Function to generate random quote
def generate_quote():
    mood_selected = select_mood.get()
    quotes = {
        "Happy": [
            "Smile more, worry less.",
            "Happiness looks good on you.",
            "Collect moments, not things."
        ],
        "Sad": [
            "It’s okay to feel sad sometimes.",
            "Every storm runs out of rain.",
            "Even gray skies have silver linings."
        ],
        "Excited": [
            "Adventure awaits, go find it.",
            "Feel the thrill, chase the moment.",
            "Energy flows where focus goes."
        ],
        "Angry": [
            "Take a deep breath, let it go.",
            "Peace over anger, always.",
            "Control your mind, not your temper."
        ],
        "Calm": [
            "Breathe in, breathe out, relax.",
            "Still waters run deep.",
            "Calm is the new power."
        ],
        "Romantic": [
            "Love quietly, love deeply.",
            "You + me = ❤️",
            "Small gestures, big love."
        ],
        "Motivated": [
            "Dream big, start small.",
            "One step at a time.",
            "Believe in your hustle."
        ],
        "Stressed": [
            "Pause, breathe, reset.",
            "Let go of what you can’t control.",
            "Stress less, live more."
        ]
    }

    # Pick a random quote from the list for the selected mood
    quote = random.choice(quotes.get(mood_selected, ["Please select a mood to get a quote."]))
    quote_label.config(text=quote)

# Button
button = Button(
    window,
    text="Generate Quote",
    bg="#96ECF4",
    fg="white",
    font=("Montserrat", 12, "bold"),
    command=generate_quote  # Attach function here
)
button.pack(pady=20)

window.mainloop()
