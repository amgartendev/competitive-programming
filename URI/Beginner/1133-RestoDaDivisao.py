# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

x = int(input())
y = int(input())

if (x > y):
    aux = y
    y = x
    x = aux

for i in range(x+1, y):
    if (i % 5 == 2) or (i % 5 == 3):
        print(i)
