# chat_ai_advanced_learning_v5_internet.py
import re
import random
import math
from datetime import datetime

# Predefined responses for randomization
greetings = [
    "Hello there! How can I assist you today?",
    "Hi! What can I do for you?",
    "Hey! How can I help?",
    "Greetings! How may I assist you?"
    ""
]

farewells = [
    "Goodbye! It was nice talking to you.",
    "Bye! Have a great day!",
    "See you! Take care!",
    "Farewell! Stay safe!"
]

thank_you_responses = [
    "You're welcome! Happy to help.",
    "No problem!",
    "Anytime!",
    "Glad to be of assistance!"
]

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "How do you organize a space party? You planet.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't programmers like nature? Too many bugs."
]

colors = [
    "I love the color blue. It's calming and reminds me of the vast sky and deep ocean.",
    "Green is refreshing, like nature and new beginnings.",
    "Red is vibrant and full of energy, just like a beating heart.",
    "Yellow is bright and cheerful, like the sunshine."
]

movies = [
    "I don't watch movies, but I've heard 'The Matrix' is quite popular among humans.",
    "Many people seem to love 'Inception' for its mind-bending plot.",
    "I've read about 'The Godfather' being a classic in cinema.",
    "It seems 'Star Wars' has a huge following across the world."
]

# Simple in-memory knowledge base
knowledge_base = {}
user_explanations = {}  # Temporarily store user explanations

def fetch_weather():
    # Dummy function for weather data (In real scenario, use an API like OpenWeatherMap)
    return "I'm not sure about the weather, but it's always sunny in the world of code!"

def evaluate_expression(expression):
    try:
        # Replace common math symbols with Python syntax
        expression = expression.replace('^', '**')
        expression = expression.replace('√', 'math.sqrt')
        expression = re.sub(r'sqrt\((.*?)\)', r'math.sqrt(\1)', expression)

        # Trigonometric functions
        expression = re.sub(r'sin\((.*?)\)', r'math.sin(math.radians(\1))', expression)
        expression = re.sub(r'cos\((.*?)\)', r'math.cos(math.radians(\1))', expression)
        expression = re.sub(r'tan\((.*?)\)', r'math.tan(math.radians(\1))', expression)

        # Evaluate the expression
        result = eval(expression, {"math": math, "__builtins__": {}})
        return f"The result is {result}."
    except Exception as e:
        return f"I couldn't understand the expression. Error: {e}"

def perform_web_search(query):
    # Placeholder for a web search function
    # In a real application, you would use an API like Google Search API or Bing Search API
    print(f"AI: Searching the web for '{query}'...")  # Simulate web search
    return f"Here is some information I found about {query}: [insert search result here]"

def learn_from_user(user_input):
    keyword, explanation = user_explanations.get(user_input, (None, None))
    if keyword and explanation:
        knowledge_base[keyword] = explanation
        del user_explanations[user_input]
        return f"Got it! I'll remember that '{keyword}' means '{explanation}'."
    return None

def ask_for_explanation(keyword):
    print(f"AI: I don't know much about '{keyword}'. May you please explain?")
    user_explanations['explanation'] = (keyword, None)

def basic_ai():
    print("Hello! I'm an advanced AI with learning capabilities. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == 'exit':
            print("AI: Goodbye! Have a great day!")
            break
            get_response = "nil"
        if 'explanation' in user_explanations:
            keyword, _ = user_explanations['explanation']
            user_explanations['explanation'] = (keyword, user_input)
            response = learn_from_user('explanation')
            if response:
                print(f"AI: {response}")
            continue

        learned_response = get_response(user_input)
        if learned_response:
            print(f"AI: {learned_response}")
            continue

        if 'hello' in user_input or 'hi' in user_input:
            response = random.choice(greetings)
            print(f"AI: {response}")

        elif 'how are you' in user_input:
            print("AI: I'm just a bunch of code, but I'm here to help you!")

        elif 'what is your name' in user_input:
            print("AI: I'm your simple AI friend. You can call me AI.")

        elif 'thank you' in user_input or 'thanks' in user_input:
            response = random.choice(thank_you_responses)
            print(f"AI: {response}")

        elif 'weather' in user_input:
            weather_info = fetch_weather()
            print(f"AI: {weather_info}")

        elif 'calculate' in user_input or 'what is' in user_input:
            match = re.search(r'calculate (.+)|what is (.+)', user_input)
            if match:
                expression = match.group(1) if match.group(1) else match.group(2)
                print(f"AI: {evaluate_expression(expression)}")
            else:
                print("AI: Please provide a mathematical expression after 'calculate' or 'what is'.")

        elif 'bye' in user_input or 'goodbye' in user_input:
            response = random.choice(farewells)
            print(f"AI: {response}")
            break

        elif 'favorite color' in user_input:
            response = random.choice(colors)
            print(f"AI: {response}")

        elif 'tell me a joke' in user_input:
            response = random.choice(jokes)
            print(f"AI: {response}")

        elif 'your favorite movie' in user_input or 'favorite movie' in user_input:
            response = random.choice(movies)
            print(f"AI: {response}")

        elif 'time' in user_input:
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"AI: The current time is {current_time}.")

        elif 'day' in user_input:
            current_day = datetime.now().strftime("%A")
            print(f"AI: Today is {current_day}.")

        elif 'your creator' in user_input:
            print("AI: I was created by a human with a passion for coding and artificial intelligence.")

        elif 'tell me about' in user_input:
            topic = user_input.replace('tell me about', '').strip()
            if topic in knowledge_base:
                print(f"AI: {knowledge_base[topic]}")
            else:
                ask_for_explanation(topic)

        elif 'tell me' in user_input:
            topic = user_input.replace('tell me', '').strip()
            if topic in knowledge_base:
                print(f"AI: {knowledge_base[topic]}")
            else:
                ask_for_explanation(topic)

        else:
            # If the topic is unknown, perform a web search and ask for explanation
            ask_for_explanation(user_input)
            print(perform_web_search(user_input))

if __name__ == "__main__":
    basic_ai()





samplevar = "True"












if samplevar == "True":
    sound = AudioSegment.from_mp3('myfile.mp3')
    play(sound)
