import json
import os

memory_file = "memory.json"

# load memory
if os.path.exists(memory_file):
    with open(memory_file, "r") as f:
        memory = json.load(f)
else:
    memory = {}

print("Saad Smart Bot 🤖 (type 'bye' to exit)")

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("Bot: Allah Hafiz 👋")
        break

    # special reply
    if "kis ne banaya" in user:
        print("Bot: Mujhe Muhammad Saad Iqbal ne banaya ❤️")
        continue

    # memory check
    if user in memory:
        print("Bot:", memory[user])
    else:
        print("Bot: Mujhe nahi pata 😅 tum sikhao")
        answer = input("Teach me: ")

        memory[user] = answer

        with open(memory_file, "w") as f:
            json.dump(memory, f)

        print("Bot: Seekh liya 👍")
