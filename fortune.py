#!/usr/bin/env python3

import random


def main():
    print("\n🔮 Welcome to Aman Raj's Fortune Teller (21JE0087) 🔮")

    # Get user's mood
    mood = input(
        "How are you feeling today? (happy/sad/neutral/stressed): ").lower()

    # Fortune options for each mood
    happy_fortunes = [
        "Great things await you, Aman! Keep smiling.",
        "Your positivity will bring unexpected opportunities today!",
        "The happiness you feel today will multiply in the coming days."
    ]

    sad_fortunes = [
        "Don't worry, better days are coming. Tomorrow will be brighter!",
        "Every cloud has a silver lining. Your sadness is temporary.",
        "This too shall pass. Joy is waiting just around the corner."
    ]

    neutral_fortunes = [
        "Balance is key. Stay centered and opportunities will find you.",
        "Your steady approach will lead to consistent progress.",
        "Sometimes the middle path leads to the greatest discoveries."
    ]

    stressed_fortunes = [
        "Take a deep breath. Aman would remind you that this stress will fade.",
        "The pressure you feel today is building your strength for tomorrow.",
        "Step back, prioritize, and watch your stress melt away."
    ]

    # Generate fortune based on mood
    if mood == "happy":
        print(f"✨ Your fortune: {random.choice(happy_fortunes)} ✨")
    elif mood == "sad":
        print(f"✨ Your fortune: {random.choice(sad_fortunes)} ✨")
    elif mood == "neutral":
        print(f"✨ Your fortune: {random.choice(neutral_fortunes)} ✨")
    elif mood == "stressed":
        print(f"✨ Your fortune: {random.choice(stressed_fortunes)} ✨")
    else:
        print(
            "I'm not sure how to interpret that mood. Try happy, sad, neutral, or stressed.")


if __name__ == "__main__":
    main()
