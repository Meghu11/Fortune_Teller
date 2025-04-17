import random

def main():
    name = "Megh Ingle"
    admission_number = "21JE0554"

    print(f"Welcome to the Fortune Teller!")
    print(f"Developed by {name} | Admission No: {admission_number}")
    print("-" * 50)

    mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

    fortunes = {
        "happy": [
            f"{name}, today is a great day to achieve something new!",
            "Keep smiling, good things are coming your way!",
            f"Your joy is contagious, {name}—spread it around!"
        ],
        "sad": [
            f"Tough times don't last {name}, but tough people do.",
            f"Hang in there {name}, something good is around the corner.",
            "It's okay to feel down. Take time to heal."
        ],
        "neutral": [
            f"Stay steady {name}, great things often follow calmness.",
            "Your calm mindset is your superpower today.",
            f"Keep going {name} — you’re doing better than you think!"
        ],
        "stressed": [
            f"Take a deep breath and focus on what you can control {name}.",
            "Don't forget to take a break—you deserve it!",
            f"Stress is temporary {name}. Your strength is permanent."
        ]
    }

    if mood in fortunes:
        print("\n🔮 Your Fortune:")
        print(random.choice(fortunes[mood]))
    else:
        print("Sorry, I don't have a fortune for that mood yet. Try again!")

if __name__ == "__main__":
    main()
