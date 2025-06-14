from supabase import create_client, Client


url = ""
key = ""
supabase: Client = create_client(url, key)

# Dummy test data
dummy_logs = [
    {
        "user_id": "user_1",
        "logs": [
            {
                "prompt": "What is molecular mass?",
                "response": "The molecular mass is the sum of atomic masses...",
                "time": 50,
                "is_followup": False,
                "question_type": "factual",
                "topic": "chemistry"
            },
            {
                "prompt": "Write a code to calculate atomic mass",
                "response": "Here's a Python function...",
                "time": 25,
                "is_followup": True,
                "question_type": "code",
                "topic": "chemistry"
            }
        ]
    },
    {
        "user_id": "user_2",
        "logs": [
            {
                "prompt": "What are the physical properties of metals?",
                "response": "Metals are good conductors...",
                "time": 56,
                "is_followup": False,
                "question_type": "factual",
                "topic": "physics"
            }
        ]
    },
    {
        "user_id": "user_3",
        "logs": [
            {
                "prompt": "Explain Maxwell's equations in depth",
                "response": "Maxwell's equations describe how electric and magnetic fields interact...",
                "time": 110,
                "is_followup": False,
                "question_type": "conceptual",
                "topic": "physics"
            },
            {
                "prompt": "Derive Gauss's law using divergence theorem",
                "response": "Here's the derivation...",
                "time": 90,
                "is_followup": True,
                "question_type": "derivation",
                "topic": "physics"
            }
        ]
    },
    {
        "user_id": "user_4",
        "logs": [
            {
                "prompt": "What's the formula for area of a circle?",
                "response": "Area = πr²",
                "time": 10,
                "is_followup": False,
                "question_type": "factual",
                "topic": "math"
            },
            {
                "prompt": "What is pi?",
                "response": "Pi is the ratio of a circle’s circumference to its diameter.",
                "time": 20,
                "is_followup": True,
                "question_type": "conceptual",
                "topic": "math"
            }
        ]
    },
    {
        "user_id": "user_5",
        "logs": [
            {
                "prompt": "How does backpropagation work in neural networks?",
                "response": "Backpropagation uses gradient descent to update weights...",
                "time": 120,
                "is_followup": False,
                "question_type": "conceptual",
                "topic": "machine learning"
            },
            {
                "prompt": "How can we address covariate shift in a real-time data stream without retraining the entire model?",
                "response": "We can address covariate shift in real-time streams by applying importance weighting or online domain adaptation techniques like adaptive batch normalization....",
                "time": 180,
                "is_followup": True,
                "question_type": "code",
                "topic": "machine learning"
            }
        ]
    }
]


# Insert data
try:
    print("Inserting dummy logs...")
    for i, log in enumerate(dummy_logs):
        result = supabase.table("chat_history").insert(log).execute()
        print(f"Inserted log {i+1}: {result.data}")

except Exception as e:
    print(f"Error inserting data: {e}")
