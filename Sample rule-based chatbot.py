import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample responses
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey", "good morning", "good afternoon", "good evening")
GREETING_RESPONSES = ["Hi!", "Hey!", "Hello!", "Good to see you!", "How can I help you today?", "I am happy to chat with you!"]

# Basic personal responses
PERSONAL_QUESTIONS = {
    "what is your name": "I am a chatbot created to assist you!",
    "who are you": "I am an AI chatbot here to help you with your queries.",
    "what are your hobbies": "I enjoy learning new things and helping people like you!",
    "how are you": "I'm just a program, but I'm functioning as expected! How can I assist you?",
    "where are you from": "I exist in the digital realm, ready to assist you anywhere and anytime!"
}

# Function to tokenize and normalize text (no nltk)
def simple_tokenize(text):
    text = text.lower().translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    return text.split()  # Split into words (tokens)

# Lemmatization replacement (since lemmatizing requires deeper linguistic analysis, we'll use a simpler form normalization)
def LemNormalize(text):
    return simple_tokenize(text)

# Greeting function
def greeting(sentence):
    """Return a greeting response if the user's input is a greeting"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Check for personal questions
def personal_question(sentence):
    """Return a response to personal questions"""
    for question in PERSONAL_QUESTIONS:
        if question in sentence:
            return PERSONAL_QUESTIONS[question]
    return None

# Expanded conversation corpus
raw_corpus = """
Hello, I am your friendly chatbot. I can help with basic questions.
How can I assist you today?
Tell me more about your projects.
I can answer questions about various topics.
Feel free to ask me about anything!

The history of sports is vast, with the first Olympic Games held in 776 BC in ancient Greece.
Football, also known as soccer, is the world's most popular sport with over 4 billion fans.
Cricket is a major sport in countries like India, Pakistan, and Australia, with a rich history.
Basketball was invented in 1891 by Dr. James Naismith in the United States.
The Olympics are held every four years, showcasing various sports from around the world.

Bitcoin is the first decentralized cryptocurrency, created in 2009 by an unknown person using the name Satoshi Nakamoto.
Blockchain technology, which underpins cryptocurrencies like Bitcoin, ensures secure and transparent transactions.
Ethereum, another popular cryptocurrency, introduced smart contracts, enabling complex applications on the blockchain.
The rise of cryptocurrencies has led to the development of decentralized finance (DeFi) platforms.

Pakistan was established in 1947 after the partition of British India.
It has a rich cultural heritage and is home to the ancient Indus Valley Civilization.
The capital city of Pakistan is Islamabad, and its largest city is Karachi.
Pakistan is known for its diverse landscapes, from mountains to deserts.
K2, the second-highest peak in the world, is located in Pakistan.

The universe is vast and mysterious, with billions of galaxies, stars, and planets.
Artificial Intelligence is rapidly evolving and impacting industries from healthcare to finance.
Climate change is a pressing challenge affecting ecosystems and communities globally.
Astronomy is the study of celestial objects, space, and the universe as a whole.
The history of science spans thousands of years, with contributions from cultures around the world.
"""

# Split raw_corpus into a list of sentences
sentence_list = raw_corpus.split('\n')

# Response generation
def response(user_response):
    chatbot_response = ''
    sentence_list.append(user_response)

    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sentence_list)

    similarity_values = cosine_similarity(tfidf[-1], tfidf)
    idx = similarity_values.argsort()[0][-2]

    flat = similarity_values.flatten()
    flat.sort()
    req_tfidf = flat[-2]

    if req_tfidf == 0:
        chatbot_response = "I am sorry, I don't understand."
    else:
        chatbot_response = sentence_list[idx]

    sentence_list.remove(user_response)
    return chatbot_response

# Main chat loop
if __name__ == "__main__":
    flag = True
    print("Chatbot: Hello! I am a chatbot. Type 'bye' to exit.")

    while flag:
        user_response = input("You: ").lower()

        if user_response != 'bye':
            if user_response in ['thanks', 'thank you']:
                flag = False
                print("Chatbot: You're welcome!")
            else:
                if greeting(user_response) is not None:
                    print(f"Chatbot: {greeting(user_response)}")
                elif personal_question(user_response) is not None:
                    print(f"Chatbot: {personal_question(user_response)}")
                else:
                    print(f"Chatbot: {response(user_response)}")
        else:
            flag = False
            print("Chatbot: Goodbye! Take care!")
