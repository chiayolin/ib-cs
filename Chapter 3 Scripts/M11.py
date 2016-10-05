# M11.py - Sage Program Modification
#
# Following is the output of an “all knowing” Sage program that replies with 
# random responses to ques- tions posed by the user. The responses generated 
# have no meaningful connection to the questions asked.
#
# In the 1960s, a program called Eliza was developed that was able to behave 
# as a psychotherapist. It did not really understand anything, it only looked
# for certain words to turn the patient’s comments or ques- tions back to the 
# patient. For example, if a patient said, “My mom drives me crazy,” it might 
# reply with “Tell me more about your mom.” Modify this program so that it 
# appears to have understanding by similar means of word recognition as used 
# in the Eliza program. Specically, incorporate a set of “trigger” words that, 
# if found, causes a specific response to be given. For example, if the word “I” 
# appears in the question (for example, “Will I ever be rich?” or “Am I always 
# going to be happy?”), the response may be “You are in charge of your own 
# destiny.” If the word “new” appears in the question (for example, “Will I find
# a new boyfriend soon?” or “Will I find a new life?,” the response may be 
# “Changes are up to you and the unpredictable events in life.”Be creative. In 
# order to determine if a given word (or phrase) appears in a given question, 
# make use of the in membership operator.
#
# date:    10/03/2016
# author:  n/a
# license: n/a

# Furtune Teller Program

from random import randint

trigger = { 
    "moodle" : "It's down again, isn't it?",
    "program" : "When in doubt, use brute force.",
    "lie" : "If you lie to the computer, it will get you",
    "dylan" : "The answer is blowin' in the wind.",
    "your" : "I don't like to talk about myself",
    "harambe" : "Harambe was just a gorilla.",
    "911" : "Guess who did 911? (https://goo.gl/HjJxS4)",
    "email" : "Tell me the best way to cover up emails.",
    "communist" : "Look out you Commies!" }

raw_str = input().replace("?", "").lower().split(" ")

# extract a token from the sentence 
token = list(filter(lambda token: token in trigger, raw_str))
if not token:
    response = "I don't know"
else:
    key = len(token) > 1 and token[randint(0, len(token) - 1)] or token[0]
    response = trigger[key]

print(response)
