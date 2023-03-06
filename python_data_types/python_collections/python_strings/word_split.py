import string

text = "Already it was deep summer on roadhouse roofs and in front of wayside garages, where new red gas-pumps sat out in pools of light, and when I reached my estate at West Egg I ran the car under its shed and sat for a while on an abandoned grass roller in the yard. The wind had blown off, leaving a loud bright night with wings beating in the trees and a persistent organ sound as the full bellows of the earth blew the frogs full of life. The silhouette of a moving cat wavered across the moonlight and turning my head to watch it I saw that I was not alone--fifty feet away a figure had emerged from the shadow of my neighbor's mansion and was standing with his hands in his pockets regarding the silver pepper of the stars. Something in his leisurely movements and the secure position of his feet upon the yard suggested that it was Mr. Gatsby himself, come out to determine what share was his of our local heavens."


text = "An then the pig wnt to town.An then the pig wnt to town.An then the pig wnt to town.An then the pig wnt to town.An then the pig wnt to town.An then the pig wnt to town.An then the pig wnt to town.An then the pig wnt to town.An then the pig wnt to town.An then the pig wnt to town.An then the pig wnt to town.An then the pig wnt to town.An then the pig wnt to town."

def from_post(test:str):
    key = "the"

    list = [word.strip(string.punctuation) for word in test.split()]

    print_list = []
    for i in range(0, len(list)):
        if list[i] == key:
            temp = list [i + 1]
            if temp not in print_list:
                print_list.append(temp)
    print(print_list)


words = [word.strip(string.punctuation) for word in text.split()]
first_key = words.index('the')
print_list = set(words[first_key:])
print(print_list)

from_post(text)