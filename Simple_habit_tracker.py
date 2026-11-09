habits = {}
while True:
    habit = input("Enter a habit to mark complete (or 'done' to finish): ").strip()
    if habit.lower() == "done":
        break
    if habit :
        habits[habit] = habits.get(habit,0) + 1
        print(f"Recorded '(habit)'.Count this session: {habits[habit]}")

print("\nSession summary")
for habit, count in habits.items():
    print(f"- {habit}: {count} completion(s)")


