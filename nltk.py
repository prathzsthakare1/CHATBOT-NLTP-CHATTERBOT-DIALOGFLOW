import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name ?",
        ["I am a bot created by Prathmesh Thakare. you can call me prathzsthakare!",]
    ],
    [
        r"which courses can i apply for ?",
        ["This are the courses in our college:"
         "CSE-DS,AI-DS,IT,Computer,Civil",]
],
    [
        r"Is there any contact available?",
        ["This are contacts you can refer:9665515996 and 8806688663",]
    ],
    [
        r"What is the address of college?",
        ["It is near Vasai Road Station.",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","How can I help you?:)",]
    ],
[
        r"Is it a private college or government college?",
        ["It is a Government College.",]
    ],
    [
        r"What is the name of college?",
        ["Vidyavardhini College of Engineering.",]
    ],
    [
        r"How many seats are available for Computer Branch?",
        ["There are 120 seats available for Computer Branch same for IT and Civil,CSE and AI 60.",]
    ],
    [
        r"What are more facilities available inside college?",
        ['There is playground,gymkhana,multiple laboratories with computers available,Seminar halls and much more things.',]
    ],
    [
        r"What functions are organized in college?",
        ['Functions organized are Zeal,Hackathon,sport competitions,Indoor games and much more.']
    ],
]
def chat():
    print("Hi! I am a chatbot created by Prathmesh Thakare for your service")
    chat = Chat(pairs, reflections)
    chat.converse()
#initiate the conversation
if _name_ == "_main_":
    chat()
