# Saulbot is supposed to be a fun helpful bot

import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Saulbot")

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "That is good to hear.",
    "Thank you.",
    "Your're welcome.",
]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)

response = chatbot.get_response("Good Morning!")
print(response)