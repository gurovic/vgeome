from geometry import *
from random import randint 

ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ABC_2 = ['α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ']

def enter():
    print("How many points?")
    number = int(input())
    information = data(number)
    print("Your points:", end=' ')
    print(" ".join(information))
    information_2 = reader(information)
    printer()

def data(number):
    points = []
    for i in range(number):
        points.append(str(ABC[i]) + ' ' + str(randint()) + ' ' + str(randint()))
    return points    

def reader():
    '''
    segments
    mid
    triangle
    triangle information
    cercle
    beem
    '''
def printer():
    pass
