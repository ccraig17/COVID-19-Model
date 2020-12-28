#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 18:06:40 2020

@author: ccraig
"""

# Cool Vibrant Circle using the Turtle Module

import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("white")

a = 0
b = 0

t.speed(0)
t.penup()
t.goto(0,200)
t.pendown()

while True:  
    t.forward(a)
    t.right(b)
    a+=3
    b+=1
    if b ==210:
        break
    t.hideturtle()
turtle.done()