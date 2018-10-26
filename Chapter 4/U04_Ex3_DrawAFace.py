# U04_Ex3_DrawAFace.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 23 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 3
#    Source: Python Programming
#   Chapter: 4
#
# Program Description
#
# This program draws a face
#
# Algorithm (pseudocode)
# set smilyface to turtle
# set the colors/details
# set the variables for directions
#
#
def draw_smileyface(canvas, center, middle, vradius, hradius,
                    facecolor='yellow', eyecolor ='blue',
                    outlinecolor='black', thickness=2):
    left = center - vradius
    right = center + vradius
    width = right - left
    top = middle - hradius
    bottom = middle + hradius
    height = bottom - top
    centerleft = (center + left) / 2
    centerright = (center + right) / 2
    middletop = (middle + top) / 2
    middlebottom = (middle + bottom) / 2
    eyeradius = ((width+height)/2) / 20
    eye1center = (center + centerleft) / 2
    eye2center = (center + centerright) / 2
    eyemiddle = middletop
    smileheight = height / 10
    smiletop = middle
    smileleft = centerleft
    smileright = centerright
    canvas.create_oval(left,top, right,bottom,
                       fill=facecolor, width=thickness)
    canvas.create_oval(eye1center-eyeradius,eyemiddle-eyeradius,
                       eye1center+eyeradius,eyemiddle+eyeradius,
                       fill=eyecolor, width=thickness/2)
    canvas.create_oval(eye2center-eyeradius,eyemiddle-eyeradius,
                       eye2center+eyeradius,eyemiddle+eyeradius,
                       fill=eyecolor, width=thickness/2)
    canvas.create_arc(smileleft,middle-smileheight,
                      smileright,middle+smileheight,
                      start=0, extent=-180, width=thickness*2, style=ARC)
