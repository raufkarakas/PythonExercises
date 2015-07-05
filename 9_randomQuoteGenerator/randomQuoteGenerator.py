__author__ = 'rkarakas'

import random

def randomQuoteGenerator():
    sentences = """A telephone, or phone, is a telecommunications device that permits two or more users to conduct a
    conversation when they are too far apart to be heard directly. A telephone converts sound, typically and most
    efficiently the human voice, into electronic signals suitable for transmission via cables or other transmission
    media over long distances, and replays such signals simultaneously in audible form to its user. In 1876, Alexander
    Graham Bell was the first to be granted a United States patent for a device that produced clearly intelligible
    replication of the human voice. This instrument was further developed by many others. The telephone was the first
    device in history that enabled people to talk directly with each other across large distances. Telephones rapidly
    became indispensable to businesses, government, and households, and are today some of the most widely used small
    appliances. The essential elements of a telephone are a microphone (transmitter) to speak into and an earphone
    (receiver) which reproduces the voice in a distant location. In addition, most telephones contain a ringer which
    produces a sound to announce an incoming telephone call, and a dial used to enter a telephone number when initiating
    a call to another telephone. Until approximately the 1970s most telephones used a rotary dial, which was superseded
    by the modern DTMF push-button dial, first introduced to the public by AT&T in 1963. The receiver and transmitter
    are usually built into a handset which is held up to the ear and mouth during conversation. The dial may be located
    either on the handset, or on a base unit to which the handset is connected. The transmitter converts the sound
    waves to electrical signals which are sent through the telephone network to the receiving phone. The receiving
    telephone converts the signals into audible sound in the receiver, or sometimes a loudspeaker. Telephones permit
    duplex communication, meaning they allow the people on both ends to talk simultaneously.""".split(".")

    sentenceNumber = int(input("How many sentences you want? -> "))

    finalQuote = []
    for i in range(sentenceNumber):
        finalQuote.append(random.choice(sentences))
    print("Your random quote: %s." %(format(".".join(finalQuote))))

randomQuoteGenerator()