
import json

# Define the path once using a raw string
path = r'C:\Dev\task\candidate_1.json'

try:
    # FIX: Use the 'path' variable instead of typing the raw path without quotes
    with open(path, 'r') as file:
        data = json.load(file)
        print("--- Success! AI Candidate Data Loaded ---\n")
        
        # Displaying the structured output
        for profile in data:
            info = profile["candidate_profile"]["personal_info"]
            skills = profile["candidate_profile"]["skills"].get("technical", [])
            recent_job = profile["candidate_profile"]["experience"][0]
            
            print(f"Name: {info['name']}")
            print(f"Role: {recent_job['designation']} at {recent_job['company']}")
            print(f"Skills: {', '.join(skills)}")
            print("-" * 30)

except FileNotFoundError:
    print(f"Error: Could not find file at {path}")
except json.JSONDecodeError:
    print("Error: JSON format is invalid. Check for missing commas or brackets.")
except KeyError as e:
    print(f"Error: Missing expected field in JSON: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")