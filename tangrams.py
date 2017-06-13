# Tangrams.py
# 04/24/17

# This is a tangrams generator.

from cs1graphics import *
import random


# define your functions (eyesPicture and eyes) here

#the helper function eyes will create one face with arguments
#arguments: width(w), height(h), face color(faceColor), rotation angle (angle), and x,y coordinates (x,y)

colors = "aliceblue, antiquewhite, antiquewhite1, antiquewhite2, antiquewhite3,"
colors += "antiquewhite4, aquamarine, aquamarine1, aquamarine2, aquamarine3, aquamarine4,"
colors += "azure, azure1, azure2, azure3, azure4, beige, bisque, bisque1, bisque2, bisque3,"
colors += "bisque4, blanchedalmond, blue, blue1, blue2, blue3, blue4, blueviolet,"
colors +="brown, brown1, brown2, brown3, brown4, burlywood, burlywood1, burlywood2,"
colors +="burlywood3, burlywood4, cadetblue, cadetblue1, cadetblue2, cadetblue3,"
colors +="cadetblue4, chartreuse, chartreuse1, chartreuse2, chartreuse3, chartreuse4,"
colors +="chocolate, chocolate1, chocolate2, chocolate3, chocolate4, coral, coral1,"
colors +="coral2, coral3, coral4, cornflowerblue, cornsilk, cornsilk1, cornsilk2,"
colors +="cornsilk3, cornsilk4, cyan, cyan1, cyan2, cyan3, cyan4, darkblue, darkcyan,"
colors +="darkgoldenrod, darkgoldenrod1, darkgoldenrod2, darkgoldenrod3, darkgoldenrod4,"
colors +="darkgray, darkgreen, darkgrey, darkkhaki, darkmagenta, darkolivegreen,"
colors +="darkolivegreen1, darkolivegreen2, darkolivegreen3, darkolivegreen4, darkorange,"
colors +="darkorange1, darkorange2, darkorange3, darkorange4, darkorchid, darkorchid1,"
colors +="darkorchid2, darkorchid3, darkorchid4, darkred, darksalmon, darkseagreen,"
colors +="darkseagreen1, darkseagreen2, darkseagreen3, darkseagreen4, darkslateblue,"
colors +="darkslategray, darkslategray1, darkslategray2, darkslategray3, darkslategray4,"
colors +="darkslategrey, darkturquoise, darkviolet, deeppink, deeppink1, deeppink2,"
colors +="deeppink3, deeppink4, deepskyblue, deepskyblue1, deepskyblue2, deepskyblue3,"
colors +="deepskyblue4, dimgray, dimgrey, dodgerblue, dodgerblue1, dodgerblue2,"
colors +="dodgerblue3, dodgerblue4, firebrick, firebrick1, firebrick2, firebrick3,"
colors +="firebrick4, floralwhite, forestgreen, gainsboro, ghostwhite, gold, gold1, gold2,"
colors +="gold3, gold4, goldenrod, goldenrod1, goldenrod2, goldenrod3, goldenrod4, gray,"
colors +="honeydew, honeydew1, honeydew2, honeydew3, honeydew4, hotpink, hotpink1,"
colors +="hotpink2, hotpink3, hotpink4, indianred, indianred1, indianred2, indianred3,"
colors +="indianred4, ivory, ivory1, ivory2, ivory3, ivory4, khaki, khaki1, khaki2,"
colors +="khaki3, khaki4, lavender, lavenderblush, lavenderblush1, lavenderblush2,"
colors +="lavenderblush3, lavenderblush4, lawngreen, lemonchiffon, lemonchiffon1,"
colors +="lemonchiffon2, lemonchiffon3, lemonchiffon4, lightblue, lightblue1, lightblue2,"
colors +="lightblue3, lightblue4, lightcoral, lightcyan, lightcyan1, lightcyan2,"
colors +="lightcyan3, lightcyan4, lightgoldenrod, lightgoldenrod1, lightgoldenrod2,"
colors +="lightgoldenrod3, lightgoldenrod4, lightgoldenrodyellow, lightgray, lightgreen,"
colors +="lightgrey, lightpink, lightpink1, lightpink2, lightpink3, lightpink4,"
colors +="lightsalmon, lightsalmon1, lightsalmon2, lightsalmon3, lightsalmon4,"
colors +="lightseagreen, lightskyblue, lightskyblue1, lightskyblue2, lightskyblue3,"
colors +="lightskyblue4, lightslateblue, lightslategray, lightslategrey, lightsteelblue,"
colors +="lightsteelblue1, lightsteelblue2, lightsteelblue3, lightsteelblue4, lightyellow,"
colors +="lightyellow1, lightyellow2, lightyellow3, lightyellow4, limegreen, linen,"
colors +="magenta, magenta1, magenta2, magenta3, magenta4, maroon, maroon1, maroon2,"
colors +="maroon3, maroon4, mediumaquamarine, mediumblue, mediumorchid, mediumorchid1,"
colors +="mediumorchid2, mediumorchid3, mediumorchid4, mediumpurple, mediumpurple1,"
colors +="mediumpurple2, mediumpurple3, mediumpurple4, mediumseagreen, mediumslateblue,"
colors +="mediumspringgreen, mediumturquoise, mediumvioletred, midnightblue, mintcream,"
colors +="mistyrose, mistyrose1, mistyrose2, mistyrose3, mistyrose4, moccasin,"
colors +="navajowhite, navajowhite1, navajowhite2, navajowhite3, navajowhite4, navy,"
colors +="navyblue, oldlace, olivedrab, olivedrab1, olivedrab2, olivedrab3, olivedrab4,"
colors +="orange, orange1, orange2, orange3, orange4, orangered, orangered1, orangered2,"
colors +="orangered3, orangered4, orchid, orchid1, orchid2, orchid3, orchid4,"
colors +="palegoldenrod, palegreen, palegreen1, palegreen2, palegreen3, palegreen4,"
colors +="paleturquoise, paleturquoise1, paleturquoise2, paleturquoise3, paleturquoise4,"
colors +="palevioletred, palevioletred1, palevioletred2, palevioletred3, palevioletred4,"
colors +="papayawhip, peachpuff, peachpuff1, peachpuff2, peachpuff3, peachpuff4, peru,"
colors +="pink, pink1, pink2, pink3, pink4, plum, plum1, plum2, plum3, plum4, powderblue,"
colors +="purple, purple1, purple2, purple3, purple4, red, red1, red2, red3, red4,"
colors +="rosybrown, rosybrown1, rosybrown2, rosybrown3, rosybrown4, royalblue,"
colors +="royalblue1, royalblue2, royalblue3, royalblue4, saddlebrown, salmon, salmon1,"
colors +="salmon2, salmon3, salmon4, sandybrown, seagreen, seagreen1, seagreen2,"
colors +="seagreen3, seagreen4, seashell, seashell1, seashell2, seashell3, seashell4,"
colors +="sienna, sienna1, sienna2, sienna3, sienna4, skyblue, skyblue1, skyblue2,"
colors +="skyblue3, skyblue4, slateblue, slateblue1, slateblue2, slateblue3, slateblue4,"
colors +="slategray, slategray1, slategray2, slategray3, slategray4, slategrey, snow,"
colors +="snow1, snow2, snow3, snow4, springgreen, springgreen1, springgreen2,"
colors +="springgreen3, springgreen4, steelblue, steelblue1, steelblue2, steelblue3,"
colors +="steelblue4, tan, tan1, tan2, tan3, tan4, thistle, thistle1, thistle2, thistle3,"
colors +="thistle4, tomato, tomato1, tomato2, tomato3, tomato4, turquoise, turquoise1,"
colors +="turquoise2, turquoise3, turquoise4, violet, violetred, violetred1, violetred2,"
colors +="violetred3, violetred4, wheat, wheat1, wheat2, wheat3, wheat4, white,"
colors +="whitesmoke, yellow, yellow1, yellow2, yellow3, yellow4, yellowgreen"

colorsList = colors.split(',')

def randomColor():
    randNum = random.randint(0,len(colorsList) - 1)
    return colorsList[randNum].strip()

def triangle(w, h, pieceColor, angle, x, y): 
    
    #making a tangram board layer
    triangleBoard=Layer()
    
    # triangle piece
    triangle = Polygon(Point(0,0), Point(w,0), Point(0,h))
    triangle.setFillColor(pieceColor)
    triangle.setBorderWidth(4)
    triangleBoard.add(triangle)
    
    #rotation
    triangleBoard.rotate(angle)
    
    #transformation
    triangleBoard.moveTo(x,y)
    
    return triangleBoard
    
def square(w, h, pieceColor, angle, x, y):
    
    #making a tangram board layer
    squareBoard = Layer()
    
    #square piece
    #square = Square(w, Point(x,y))
    square = Square(w)
    square.setFillColor(pieceColor)
    square.setBorderWidth(4)
    squareBoard.add(square)
    
    #rotation
    squareBoard.rotate(angle)
    
    #transformation
    squareBoard.moveTo(x,y)
    
    return squareBoard
    
def trapezoid(w, h, pieceColor, angle, x, y):
    
    #making a tangram board layer
    trapezoidBoard = Layer()
    
    #trapezoidal piece
    trapezoid = Polygon(Point(0,0), Point(w,0), Point(w + h, -h), Point (h, -h))
    trapezoid.setFillColor(pieceColor)
    trapezoid.setBorderWidth(4)
    trapezoidBoard.add(trapezoid)
    
    #rotation
    trapezoidBoard.rotate(angle)
    
    #transformation
    trapezoidBoard.moveTo(x,y)
    
    return trapezoidBoard
    
def tangramGenerator(): 

    ## Create a Canvas where board pieces will be displayed
    canvas = Canvas(660, 660, 'white', 'Tangram Board')
    
    ## Now add all tangram pieces to the canvas.
    canvas.add(triangle(330,330,randomColor(), 0, 0, 0))
    canvas.add(triangle(233.34,233.34,randomColor(), 135, 165, 495))
    canvas.add(triangle(466.7,466.7,randomColor(), 45, 330, 330))
    canvas.add(triangle(466.7,466.7,randomColor(), 315, 330, 330))
    canvas.add(triangle(233.35,233.35,randomColor(), 225, 330, 330))
    canvas.add(square(233.35,233.35, randomColor(), 45, 165,330))
    canvas.add(trapezoid(330,165,randomColor(),0,165,165))
    
    canvas.saveToFile('TangramsTest.ps')
    
if __name__ == "__main__":    
    tangramGenerator()
    
    

#def tangramGenerator():     
#    ## Create a Canvas where board pieces will be displayed
#    canvas = Canvas(1320, 1320, 'white', 'Tangram Board')
#    
#    ## Now add all tangram pieces to the canvas.
#    canvas.add(triangle(660,660,'aliceblue', 0, 0, 0))
#    canvas.add(triangle(466.7,466.7,'aliceblue', 135, 330, 990))
#    canvas.add(triangle(933.4,933.4,'aliceblue', 45, 660, 660))
#    canvas.add(triangle(933.4,933.4,'aliceblue', 315, 660, 660))
#    canvas.add(triangle(466.7,466.7,'aliceblue', 225, 660, 660))
#    canvas.add(square(466.7, 466.7, 'aliceblue', 45, 330, 660))
#    canvas.add(trapezoid(660,330,'aliceblue',0,330,330))
#    
#tangramGenerator()

#def tangramGenerator(): 
#    ## Create a Canvas where board pieces will be displayed
#    canvas = Canvas(880, 880, 'white', 'Tangram Board')
#    
#    ## Now add all tangram pieces to the canvas.
#    canvas.add(triangle(440,440,'aliceblue', 0, 0, 0))
#    canvas.add(triangle(311.13,311.13,'aliceblue', 135, 220, 660))
#    canvas.add(triangle(622.27,622.27,'aliceblue', 45, 440, 440))
#    canvas.add(triangle(622.27,622.27,'aliceblue', 315, 440, 440))
#    canvas.add(triangle(311.13,311.13,'aliceblue', 225, 440, 440))
#    canvas.add(square(311.13, 311.13, 'aliceblue', 45, 220, 440))
#    canvas.add(trapezoid(440,220,'aliceblue',0,220,220))
#    
#tangramGenerator()



