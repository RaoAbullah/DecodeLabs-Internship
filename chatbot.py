# ============================================================
#  DecodeLabs Internship - Artificial Intelligence
#  Project 1: Rule-Based AI Chatbot
#  Batch: 2026
# ============================================================

# --- KNOWLEDGE BASE (Dictionary - O(1) lookup) ---
responses = {
    "hello": "Hi there! Welcome to DecodeLabs AI Assistant. How can I help you?",
    "hi": "Hey! Great to see you. What can I do for you today?",
    "hey": "Hello! I'm your DecodeLabs AI chatbot. Ask me anything!",
    "how are you": "I'm running perfectly on logic and rules! How about you?",
    "what is ai": "AI stands for Artificial Intelligence. It's the simulation of human intelligence by machines!",
    "what is machine learning": "Machine Learning is a subset of AI where machines learn patterns from data without being explicitly programmed.",
    "what is deep learning": "Deep Learning uses neural networks with many layers to learn complex patterns from large amounts of data.",
    "what is python": "Python is a high-level, easy-to-read programming language widely used in AI, data science, and web development.",
    "who made you": "I was built by a DecodeLabs intern using Python and rule-based logic. Project 1 complete!",
    "what can you do": "I can answer questions about AI, ML, Python, and general topics. Try asking me something!",
    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs! 😄",
    "what is decodelabs": "DecodeLabs is a tech training organization helping students bridge the gap between learning code and building real projects.",
    "help": "You can ask me about: AI, Machine Learning, Deep Learning, Python, or just say hello!",
    "thanks": "You're welcome! Happy to help anytime.",
    "thank you": "My pleasure! Is there anything else you'd like to know?",
    "bye": "Goodbye! Keep coding and building amazing things. 🚀",
    "good morning": "Good morning! Ready to learn something about AI today?",
    "good night": "Good night! Rest well and come back ready to code!",
    "what is nlp": "NLP stands for Natural Language Processing — it's how computers understand and generate human language.",
    "what is a chatbot": "A chatbot is a program designed to simulate conversation with human users. You're talking to one right now!",
}

# --- PHASE 1: INPUT & SANITIZATION ---
def sanitize_input(raw_input):
    """Converts input to lowercase and strips whitespace."""
    return raw_input.lower().strip()

# --- PHASE 2: INTENT MATCHING & RESPONSE GENERATION ---
def get_response(clean_input):
    """Looks up the response from the knowledge base with a fallback."""
    return responses.get(clean_input, "I don't understand that yet. Try asking about AI, ML, Python, or say 'help'.")

# --- PHASE 3: THE HEARTBEAT - INFINITE LOOP ---
def run_chatbot():
    print("=" * 55)
    print("   DecodeLabs AI Chatbot - Project 1")
    print("   Rule-Based Intelligence Engine")
    print("=" * 55)
    print("   Type 'bye' or 'exit' to end the conversation.\n")

    while True:
        # Step 1: Get raw input
        raw_input = input("You: ")

        # Step 2: Sanitize input
        clean_input = sanitize_input(raw_input)

        # Step 3: Exit strategy - Kill command
        if clean_input in ["exit", "quit", "bye"]:
            print("Bot: Goodbye! Keep coding and building amazing things. 🚀")
            break

        # Step 4: Generate and display response
        reply = get_response(clean_input)
        print(f"Bot: {reply}\n")

# --- ENTRY POINT ---
if __name__ == "__main__":
    run_chatbot()
