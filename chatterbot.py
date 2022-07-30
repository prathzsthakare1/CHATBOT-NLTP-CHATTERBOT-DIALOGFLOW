from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from datetime import date,datetime

bot = ChatBot('Buddy',storage_adapter='chatterbot.storage.SQLStorageAdapter',database_uri='sqlite:///database.sqlite3')
trainer=ListTrainer(bot)
trainer.train([
'Hi',
'Hello',
'Who are You?',
'I am a bot created by Prathmesh Thakare to help you ',
'What is name of college?',
'Vidyavardhini College of Engineering',
'What is college email?',
'It is vcet.2039209@vcet.edu.in',
'What are contact available for reference?',
'Here is contact number you can refer:9665515996',
'What are courses available in VCET?',
'Courses available are:CSE-DS,AI-DS,Computers,IT,CIVIL',
'How many Seats available for all courses?',
'Comps,IT & Civil:120,AI & CSE:60',
'What More facilities are provided?',
'College has playground,gymkhana,Seminar Halls,Laboratories,Classrooms and much more',
'What functions are organized by college?',
'College organizes Zeal,Hackathon,Sport Events,Indoor Games and much more.',
'Thank You',
'Welcome.'
])

name=input("Enter Your Name:")
now=datetime.now()
today=now.strftime("%A")
time=now.strftime("%H:%M:%S")

print("Hi,I am Bot Created by Prathmesh Thakare")
print(f"Today is {today},current time is {time}")
print("Let Me Know how i can help you?")

while True:
    request=input(name+':')
    if request=='Bye' or request =='bye':
        print('Bot:Bye')
        break
    else:
        response=bot.get_response(request)
        print('Bot:',response)
