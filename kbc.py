def run_kbc():
    print("--- 🏆 KBC CLI GAME ---")
    
    # Each question lists the exact string answers and option numbers that are correct
    questions = [
        {
            "q": "What is the file extension for Python?", 
            "choices": ["1. .pt", "2. .py"], 
            "valid_answers": [".Py", "B", "2", "2.", "B. .Py"]
        },
        {
            "q": "Keyword to define a function?", 
            "choices": ["1. func", "2. def"], 
            "valid_answers": ["Def", "B", "2", "2.", "B. Def"]
        },
        {
            "q": "Data structure with key-value pairs?", 
            "choices": ["1. list", "2. dictionary"], 
            "valid_answers": ["Dictionary", "B", "2", "2.", "B. Dictionary"]
        }
    ]
    
    money_tiers = [1000, 5000, 10000]
    score = 0

    for i, q_data in enumerate(questions):
        try:
            print(f"\nQ{i+1}: {q_data['q']}")
            for choice in q_data["choices"]: 
                print(choice)
                
            ans = input("Your Answer: ").strip().title()

            # Checks if the user's input matches any item in our valid answers list
            if any(valid in ans or ans == valid for valid in q_data["valid_answers"]):
                score = money_tiers[i]
                print(f"🎉 Correct! You won ₹{score:,}")
            else:
                print(f"❌ Wrong! The correct answer was option 2.")
                break
        except Exception as e:
            print(f"System Error: {e}")
            break

    print(f"\n💰 Total Winnings: ₹{score:,}")

if __name__ == "__main__":
    run_kbc()
