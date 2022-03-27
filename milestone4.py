from graphics import *
import random

#
# CS 177 - milestone2.py
# Nikhil Pradeep 0029855549
#   Following the Coding Standards and Guidelines
#   This program will create a trivia quiz. First there will be a control window
#   asking the user to play or exit. If play, they will take a quiz with 5
#   questions. The # correct will be converted into chips which can be used to
#   drop a ball through pins, into various bins for points. The final score will
#   be displayed and then the window will close with a click and the control
#   will be displayed again. My custom version will include a hardmode version
#   which will deduct a point during the take quiz if a question is wrong.

#Create the basic game window with the black and yellow banner,
#and return both the graphics window and exit rectangle
def board():
    gamewin = GraphWin("{:^130}".format("Game Board"), 500, 700)
    gamewin.setBackground('light grey')
    banner = Image(Point(250,50),"Letsplay.gif")
    banner.draw(gamewin)
    white = Rectangle(Point(0,700),Point(500,600))
    white.setFill("white")
    white.draw(gamewin)
    line1 = Line(Point(0,100),Point(500,100))
    line1.setWidth(3)
    line2 = Line(Point(0,600),Point(500,600))
    line2.setWidth(3)
    line1.draw(gamewin)
    line2.draw(gamewin)
    chipz = Text(Point(50,650),'Chips: 0')
    chipz.draw(gamewin)
    scorez = Text(Point(445,650),'Score: 0')
    scorez.draw(gamewin)
    return gamewin, chipz, scorez

#create separate function to see if click is within rectangle
def isclicked(clickpt, rect):
    if not clickpt:
        return False
    mx,my = clickpt.getX(),clickpt.getY()
    x1,y1 = rect.getP1().getX(),rect.getP1().getY()
    x2,y2 = rect.getP2().getX(),rect.getP2().getY()
    return (x1 < mx < x2) and (y1 < my < y2)

#create gray bins
def bins(graphicwindow):
    for i in range(0,8):
        line1 = Line(Point(5+70*i,100),Point(5+70*i,139))
        line1.draw(graphicwindow)
    for i in range(0,8):
        line2 = Line(Point(5+70*i,560),Point(5+70*i,599))
        line2.draw(graphicwindow)
    num40 = Text(Point(40,575),"40")
    numo1 = Text(Point(110,575),"0")
    num60 = Text(Point(180,575),"60")
    num100 = Text(Point(250,575),"100")
    num20 = Text(Point(320,575),"20")
    numo2 = Text(Point(390,575),"0")
    num80 = Text(Point(460,575),"80")
    num40.draw(graphicwindow)
    numo1.draw(graphicwindow)
    num60.draw(graphicwindow)
    num100.draw(graphicwindow)
    num20.draw(graphicwindow)
    numo2.draw(graphicwindow)
    num80.draw(graphicwindow)

#draw all the pins
def pins(window):
    emptylist = []
#loop the circles and append list
    for i in range(0,5):
        for o in range (40,461,70):
            c = Circle(Point(o,180+(80*i)),5)
            c.setFill("black")
            c.draw(window)
            emptylist.append(c)
    for i in range(0,5):
        for o in range (75,426,70):
            c = Circle(Point(o,220+(80*i)),5)
            c.setFill("black")
            c.draw(window)
            emptylist.append(c)
    return emptylist

#create the graphics of the trivia board
def makeQuiz():
#make all the basic rectangles, colors, and text objects and draw them
    backg = GraphWin("Quiz Window", 400, 400)
    backg.setBackground("grey")
    triviat = Image(Point(200,40),'TriviaTime.gif')
    triviat.draw(backg)
    displayq = Text(Point(200,135),"")
    displayq.draw(backg)
    recta = Rectangle(Point(0,175),Point(400,220))
    rectb = Rectangle(Point(0,220),Point(400,265))
    rectc = Rectangle(Point(0,265),Point(400,310))
    rectd = Rectangle(Point(0,310),Point(400,355))
    recta.setFill("gold")
    rectb.setFill("gold")
    rectc.setFill("gold")
    rectd.setFill("gold")
    recta.draw(backg)
    rectb.draw(backg)
    rectc.draw(backg)
    rectd.draw(backg)
    choicea = Text(Point(200,197.5),"")
    choiceb = Text(Point(200,242.5),"")
    choicec = Text(Point(200,287.5),"")
    choiced = Text(Point(200,332.5),"")
    choicea.draw(backg)
    choiceb.draw(backg)
    choicec.draw(backg)
    choiced.draw(backg)
    blackrect = Rectangle(Point(0,360),Point(400,400))
    blackrect.setFill('black')
    blackrect.draw(backg)
    qnum = Text(Point(50,380),'Question #1')
    qnum.setTextColor('white')
    qnum.draw(backg)
    correct = Text(Point(350,380),'Correct: 0')
    correct.setTextColor('white')
    correct.draw(backg)
#return all the objects that the user will interact with
    return backg,displayq,recta,rectb,rectc,rectd,choicea,choiceb,choicec,choiced,qnum,correct

#function that accepts data file
def pickQs(filename):
#open the file then close
    openses = open(filename,'r', encoding="utf8")
#read into variable
    allqs = openses.read()
    openses.close()
#split the string based on rows, delete last line which is " "
    listqs = allqs.split('\n')
    del listqs[-1]
    listqs2 = []
#initialize empty list, and select five random question/answers string using the
#import random sample method
    listqs2 += random.sample(listqs,5)
    listqs3 = []
#loop through each question/answer string and split based on commas
    for each in listqs2:
        listqs3.append(each.split(','))
#create a new list of lists of question/answer combos
    newdic = {}
#initialize a dictionary and add the items of the list by index
    for each in listqs3:
        newdic[each[0]] = each[1],each[2],each[3],each[4],each[5]
    return newdic

#define the area of a rectangle
def isclicked(clickpt, rect):
    if not clickpt:
        return False
    mx,my = clickpt.getX(),clickpt.getY()
    x1,y1 = rect.getP1().getX(),rect.getP1().getY()
    x2,y2 = rect.getP2().getX(),rect.getP2().getY()
    return (x1 < mx < x2) and (y1 < my < y2)

def takeQuiz():
#call the previous functions and assign variables to objects/dictionary
    backg,displayq,recta,rectb,rectc,rectd,choicea,choiceb,choicec,choiced,qnum,correct = makeQuiz()
    newdic = pickQs('questions.txt')
#initialize/create all the graphics objects such as correct, incorrect, all done
    whiteback = Rectangle(Point(95,95),Point(305,205))
    whiteback.setFill('white')
    yay = Rectangle(Point(100,100),Point(300,200))
    yay.setFill('gold')
    boo = Rectangle(Point(100,100),Point(300,200))
    boo.setFill('red')
    hooray = Text(Point(200,135),"You are correct!")
    hooray.setSize(14)
    hooray.setStyle('bold')
    sorry = Text(Point(200,135),"Sorry, that is incorrect")
    sorry.setSize(13)
    sorry.setStyle('bold')
    continu = Text(Point(200,165),"Click to continue")
    continu.setStyle('italic')
#initialize the score and also question number
    score = 0
    qupd = int(qnum.getText()[-1])
#loop through key in dictionary
    for each in newdic:
#split key into list based on words
        banana = each.split(' ')
#initialize blank string and counter
        t = ""
        n = 0
#while the counter is less than the length of the list (until it reaches end)
        while n<len(banana):
#loop through each word in list
            for item in banana:
#concentate into the blank string and add a space after, update counter
                t += item + ' '
                n += 1
#when the counter is a factor of five, add backspace
                if n % 5 == 0:
                    t += '\n'
#in the for loop, continually update each question using the dictionary index
        displayq.setText(t)
        choicea.setText(newdic[each][0])
        choiceb.setText(newdic[each][1])
        choicec.setText(newdic[each][2])
        choiced.setText(newdic[each][3])
#update question number
        qnum.setText("Question #{}".format(qupd))
#initialize click, set x counter to 0
        click = backg.checkMouse()
        x = 0
#while the condition x has not been met
        while x!=1:
#continually update click
            click = backg.checkMouse()
#if the correct answer is A
            if newdic[each][4] == 'A':
#if the correct rectangle was clicked, draw all the 'correct' graphics
#and set x to 1 to exit the while loop, update the score
                if isclicked(click,recta):
                    whiteback.draw(backg)
                    yay.draw(backg)
                    hooray.draw(backg)
                    continu.draw(backg)
                    x = 1
                    score += 1
#otherwise display 'incorrect' graphics, set x to 1 to exit the while loop
                elif (isclicked(click,rectb)):
                    whiteback.draw(backg)
                    boo.draw(backg)
                    sorry.draw(backg)
                    continu.draw(backg)
                    x = 1
                elif (isclicked(click,rectc)):
                    whiteback.draw(backg)
                    boo.draw(backg)
                    sorry.draw(backg)
                    continu.draw(backg)
                    x = 1
                elif (isclicked(click,rectd)):
                    whiteback.draw(backg)
                    boo.draw(backg)
                    sorry.draw(backg)
                    continu.draw(backg)
                    x = 1
#repeat for all letters
            if newdic[each][4] == 'B':
                if isclicked(click,rectb):
                    whiteback.draw(backg)
                    yay.draw(backg)
                    hooray.draw(backg)
                    continu.draw(backg)
                    x = 1
                    score += 1
                elif (isclicked(click,recta)):
                    whiteback.draw(backg)
                    boo.draw(backg)
                    sorry.draw(backg)
                    continu.draw(backg)
                    x = 1
                elif (isclicked(click,rectc)):
                    whiteback.draw(backg)
                    boo.draw(backg)
                    sorry.draw(backg)
                    continu.draw(backg)
                    x = 1
                elif (isclicked(click,rectd)):
                    whiteback.draw(backg)
                    boo.draw(backg)
                    sorry.draw(backg)
                    continu.draw(backg)
                    x = 1
            if newdic[each][4] == 'C':
                if isclicked(click,rectc):
                    whiteback.draw(backg)
                    yay.draw(backg)
                    hooray.draw(backg)
                    continu.draw(backg)
                    x = 1
                    score += 1
                elif (isclicked(click,rectb)):
                    whiteback.draw(backg)
                    boo.draw(backg)
                    sorry.draw(backg)
                    continu.draw(backg)
                    x = 1
                elif (isclicked(click,recta)):
                    whiteback.draw(backg)
                    boo.draw(backg)
                    sorry.draw(backg)
                    continu.draw(backg)
                    x = 1
                elif (isclicked(click,rectd)):
                    whiteback.draw(backg)
                    boo.draw(backg)
                    sorry.draw(backg)
                    continu.draw(backg)
                    x = 1
            if newdic[each][4] == 'D':
                if isclicked(click,rectd):
                    whiteback.draw(backg)
                    yay.draw(backg)
                    hooray.draw(backg)
                    continu.draw(backg)
                    x = 1
                    score += 1
                elif (isclicked(click,rectb)):
                    whiteback.draw(backg)
                    boo.draw(backg)
                    sorry.draw(backg)
                    continu.draw(backg)
                    x = 1
                elif (isclicked(click,recta)):
                    whiteback.draw(backg)
                    boo.draw(backg)
                    sorry.draw(backg)
                    continu.draw(backg)
                    x = 1
                elif (isclicked(click,rectc)):
                    whiteback.draw(backg)
                    boo.draw(backg)
                    sorry.draw(backg)
                    continu.draw(backg)
                    x = 1
#update the correct: with the score 
        correct.setText("Correct: {}".format(score))
#again check mouse, while loop to detect a click in the popup box
        click = backg.checkMouse()
        while not(isclicked(click,yay) or isclicked(click,boo)):
            click = backg.checkMouse()
#undraw everything and move on to next question
        boo.undraw()
        yay.undraw()
        whiteback.undraw()
        hooray.undraw()
        sorry.undraw()
        continu.undraw()
        qupd +=1
#create/draw all the all done graphics
    whiteback.draw(backg)
    alldonee = Rectangle(Point(100,100),Point(300,200))
    alldonee.setFill('gold')
    alldonee.draw(backg)
    final = Text(Point(200,135),"Your final score is: {}".format(score))
    final.setSize(13)
    final.setStyle('bold')
    final.draw(backg)
    continu.draw(backg)
    qnum.setText('All done!')
#new click, while the box is not clicked keep checking, then close
    click2 = backg.checkMouse()
    while not isclicked(click2,alldonee):
        click2 = backg.checkMouse()
    backg.close()
#return score variable
    return score

#control function that opens up game control display 
def control():
#Create all the graphics objects (boxes, text, etc.)
    gamecon = GraphWin('Game Control',500,200)
    gamecon.setBackground('light grey')
    title1 = Image(Point(250,50),'TrinkoTitle.gif')
    title1.draw(gamecon)
    exi2 = Rectangle(Point(270,115),Point(380,145))
    exi2.setFill('red')
    exi2.draw(gamecon)
    play2 = Rectangle(Point(120,115),Point(230,145))
    play2.setFill('green')
    play2.draw(gamecon)
    exi2t = Text(Point(325,130),'EXIT')
    exi2t.setTextColor('white')
    exi2t.draw(gamecon)
    play2t = Text(Point(175,130),'PLAY')
    play2t.setTextColor('white')
    play2t.draw(gamecon)
#The hard mode box is for my custom feature
    hardbox = Rectangle(Point(190,160),Point(310,190))
    hardbox.draw(gamecon)
    hardbox.setFill('gold')
    hardtext = Text(Point(250,175),'Hard Mode')
    hardtext.draw(gamecon)
#return the exit box, play box, hard mode box, and graphic window
    return play2,exi2,gamecon,hardbox

#the bounce controls the reaction of the ball to the pin. Accepts ball pin and
#dx/dy direction
def bounce(ball,apin,dx,dy):
#Get the center of the ball and the pin
    center=ball.getCenter()
    center2 = apin.getCenter()
#Assign the x and y values of each center
    cx,cy = center.getX(),center.getY()
    c2x,c2y = center2.getX(),center2.getY()
#If the euclidean distance between the pin and ball center is less than radius
    if ((cx-c2x)**2+(cy-c2y)**2)**.5 <= (ball.getRadius()+apin.getRadius()):
#if the ball is on the left side of the pin, move it left by increment
        if cx < c2x:
            dx += -2.5
#if it's on the right side of the pin, move it right
        else:
            dx += 2.5
#move the y value up
        dy *= -.7
#set the pin to red
        apin.setFill('red')
#otherwise, when the condition is not met
    else:
#set the pin to black
        apin.setFill('black')
#if the ball is too close to the sides
    if cx < 1 or cx > 699:
#change the x direction to the opposite
        dx *= -1
#return dx,dy
    return dx,dy

#drop function to control the dropping. Accept the score, graph window, list of
#pins, and text box for the score and chips
def drop(integer,graphwin,pinz,chiptext,scoretext):
#set the count to hte score integer from takequiz
    count = integer
#initialize the new score to 0
    scorecount = 0
#define the areas/rectangles of each bin opening. within each bin(line), there is
#a 10 pixel spacing. example the first bin line is at x=5, the rectangle does not
#start until x=15. The second bin line at x = 75, the rect1 does not end until
#65. The next rectangle starts at 85. This makes sure the ball chip cannot
#be too close and overlap the borders of the starting bin
    rect1 = Rectangle(Point(15,100),Point(65,139))
    rect2 = Rectangle(Point(85,100),Point(135,139))
    rect3 = Rectangle(Point(155,100),Point(205,139))
    rect4 = Rectangle(Point(225,100),Point(275,139))
    rect5 = Rectangle(Point(295,100),Point(345,139))
    rect6 = Rectangle(Point(365,100),Point(415,139))
    rect7 = Rectangle(Point(435,100),Point(485,139))
#check for a click
    poo = graphwin.checkMouse()
#while the count (chip count, which is the integer/takequiz score) is greater
#than 0
    while count > 0:
#if any of the rectangle regions are clicked
        if (isclicked(poo,rect1) or isclicked(poo,rect2) or isclicked(poo,rect3) or isclicked(poo,rect4) or isclicked(poo,rect5) or isclicked(poo,rect6) or isclicked(poo,rect7)):
#create and draw ball chip with initial direction 1,1
            ball = Circle(poo,15)
            ball.setFill('pink')
            ball.draw(graphwin)
            dx,dy = 1,1
#while the y coordinate has not reached the bottom line
            while ball.getCenter().getY() < 580:
#check each pin in the list, make sure ball is not too close and call bounce
                for apin in pinz:
                    dx,dy = bounce(ball,apin,dx,dy)
#change dy and dx by this increment. The values in the assignment were too fast
#so changed them. 
                dy = dy + .5
                dx = dx*.9
#move the ball and update speed
                ball.move(dx,dy)
                update(50)
#update the count
            count = count - 1
#get the x coordinate of the ball once it falls
            xcoord = ball.getCenter().getX()
#depending on which bin it fell into, add the number to the score
            if int(xcoord) in range(6,74):
                scorecount += 40
            elif int(xcoord) in range(146,214):
                scorecount += 60
            elif int(xcoord) in range(216,284):
                scorecount += 100
            elif int(xcoord) in range(286,354):
                scorecount += 20
            elif int(xcoord) in range(426,496):
                scorecount += 80
#update the score and chip count with the new number
        scoretext.setText('Score: {}'.format(scorecount))
        chiptext.setText('Chips: {}'.format(count))
#reset mouse click
        poo = graphwin.checkMouse()
#create/draw all the all done graphics, which tell final score.
    pinkback = Rectangle(Point(95,195),Point(405,405))
    pinkback.setFill('pink')
    pinkback.draw(graphwin)
    congrats = Text(Point(250,260),"CONGRATS")
    congrats.setTextColor('red')
    congrats.setSize(17)
    congrats.setStyle('bold')
    congrats.draw(graphwin)
    finalscore = Text(Point(250,325),'Your total score: {}'.format(scorecount))
    finalscore.setTextColor('red')
    finalscore.setSize(15)
    finalscore.draw(graphwin)
#new click, while the box is not clicked keep checking, then close
    click2 = graphwin.checkMouse()
    while not isclicked(click2,pinkback):
        click2 = graphwin.checkMouse()
    graphwin.close()

#this is my custom function. It is a different version of take quiz.Similar to
#original except: when you get a question wrong, it takes away a point from
#correct. But the correct can never go below 0. So if you get one right, and
#then the next question wrong, you're score will be 0. Then if you get the next
#question wrong your score will still be 0
def takeQuizHard():
#call the previous functions and assign variables to objects/dictionary
    backg,displayq,recta,rectb,rectc,rectd,choicea,choiceb,choicec,choiced,qnum,correct = makeQuiz()
    newdic = pickQs('questions.txt')
#initialize/create all the graphics objects such as correct, incorrect, all done
    whiteback = Rectangle(Point(95,95),Point(305,205))
    whiteback.setFill('white')
    yay = Rectangle(Point(100,100),Point(300,200))
    yay.setFill('gold')
    boo = Rectangle(Point(100,100),Point(300,200))
    boo.setFill('red')
    hooray = Text(Point(200,135),"You are correct!")
    hooray.setSize(14)
    hooray.setStyle('bold')
    sorry = Text(Point(200,135),"Sorry, that is incorrect")
    sorry.setSize(13)
    sorry.setStyle('bold')
    continu = Text(Point(200,165),"Click to continue")
    continu.setStyle('italic')
#initialize the score and also question number
    score = 0
    qupd = int(qnum.getText()[-1])
#loop through key in dictionary
    for each in newdic:
#split key into list based on words
        banana = each.split(' ')
#initialize blank string and counter
        t = ""
        n = 0
#while the counter is less than the length of the list (until it reaches end)
        while n<len(banana):
#loop through each word in list
            for item in banana:
#concentate into the blank string and add a space after, update counter
                t += item + ' '
                n += 1
#when the counter is a factor of five, add backspace
                if n % 5 == 0:
                    t += '\n'
#in the for loop, continually update each question using the dictionary index
        displayq.setText(t)
        choicea.setText(newdic[each][0])
        choiceb.setText(newdic[each][1])
        choicec.setText(newdic[each][2])
        choiced.setText(newdic[each][3])
#update question number
        qnum.setText("Question #{}".format(qupd))
#initialize click, set x counter to 0
        click = backg.checkMouse()
        x = 0
#while the condition x has not been met
        while x!=1:
#continually update click
            click = backg.checkMouse()
#if the correct answer is A
            if newdic[each][4] == 'A':
#if the correct rectangle was clicked, draw all the 'correct' graphics
#and set x to 1 to exit the while loop, update the score
                if isclicked(click,recta):
                    whiteback.draw(backg)
                    yay.draw(backg)
                    hooray.draw(backg)
                    continu.draw(backg)
                    x = 1
                    score += 1
#otherwise display 'incorrect' graphics, 
#and update the score to minus 1 if it's wrong
#set x to 1 to exit the while loop
                elif (isclicked(click,rectb)):
                    whiteback.draw(backg)
                    boo.draw(backg)
                    sorry.draw(backg)
                    continu.draw(backg)
                    x = 1
                    score -=1
                elif (isclicked(click,rectc)):
                    whiteback.draw(backg)
                    boo.draw(backg)
                    sorry.draw(backg)
                    continu.draw(backg)
                    x = 1
                    score -=1
                elif (isclicked(click,rectd)):
                    whiteback.draw(backg)
                    boo.draw(backg)
                    sorry.draw(backg)
                    continu.draw(backg)
                    x = 1
                    score -=1
#repeat for all letters
            if newdic[each][4] == 'B':
                if isclicked(click,rectb):
                    whiteback.draw(backg)
                    yay.draw(backg)
                    hooray.draw(backg)
                    continu.draw(backg)
                    x = 1
                    score += 1
                elif (isclicked(click,recta)):
                    whiteback.draw(backg)
                    boo.draw(backg)
                    sorry.draw(backg)
                    continu.draw(backg)
                    x = 1
                    score -=1
                elif (isclicked(click,rectc)):
                    whiteback.draw(backg)
                    boo.draw(backg)
                    sorry.draw(backg)
                    continu.draw(backg)
                    x = 1
                    score -=1
                elif (isclicked(click,rectd)):
                    whiteback.draw(backg)
                    boo.draw(backg)
                    sorry.draw(backg)
                    continu.draw(backg)
                    x = 1
                    score -=1
            if newdic[each][4] == 'C':
                if isclicked(click,rectc):
                    whiteback.draw(backg)
                    yay.draw(backg)
                    hooray.draw(backg)
                    continu.draw(backg)
                    x = 1
                    score += 1
                elif (isclicked(click,rectb)):
                    whiteback.draw(backg)
                    boo.draw(backg)
                    sorry.draw(backg)
                    continu.draw(backg)
                    x = 1
                    score -=1
                elif (isclicked(click,recta)):
                    whiteback.draw(backg)
                    boo.draw(backg)
                    sorry.draw(backg)
                    continu.draw(backg)
                    x = 1
                    score -=1
                elif (isclicked(click,rectd)):
                    whiteback.draw(backg)
                    boo.draw(backg)
                    sorry.draw(backg)
                    continu.draw(backg)
                    x = 1
                    score -=1
            if newdic[each][4] == 'D':
                if isclicked(click,rectd):
                    whiteback.draw(backg)
                    yay.draw(backg)
                    hooray.draw(backg)
                    continu.draw(backg)
                    x = 1
                    score += 1
                elif (isclicked(click,rectb)):
                    whiteback.draw(backg)
                    boo.draw(backg)
                    sorry.draw(backg)
                    continu.draw(backg)
                    x = 1
                    score -=1
                elif (isclicked(click,recta)):
                    whiteback.draw(backg)
                    boo.draw(backg)
                    sorry.draw(backg)
                    continu.draw(backg)
                    x = 1
                    score -=1
                elif (isclicked(click,rectc)):
                    whiteback.draw(backg)
                    boo.draw(backg)
                    sorry.draw(backg)
                    continu.draw(backg)
                    x = 1
                    score -=1
#update the correct: with the score. if it's negative, make it 0.
        if score < 0:
            score = 0
        correct.setText("Correct: {}".format(score))
#again check mouse, while loop to detect a click in the popup box
        click = backg.checkMouse()
        while not(isclicked(click,yay) or isclicked(click,boo)):
            click = backg.checkMouse()
#undraw everything and move on to next question
        boo.undraw()
        yay.undraw()
        whiteback.undraw()
        hooray.undraw()
        sorry.undraw()
        continu.undraw()
        qupd +=1
#create/draw all the all done graphics
    whiteback.draw(backg)
    alldonee = Rectangle(Point(100,100),Point(300,200))
    alldonee.setFill('gold')
    alldonee.draw(backg)
    final = Text(Point(200,135),"Your final score is: {}".format(score))
    final.setSize(13)
    final.setStyle('bold')
    final.draw(backg)
    continu.draw(backg)
    qnum.setText('All done!')
#new click, while the box is not clicked keep checking, then close
    click2 = backg.checkMouse()
    while not isclicked(click2,alldonee):
        click2 = backg.checkMouse()
    backg.close()
#return score variable
    return score

#main calls everything
def main():
#calls all the important objects from control
    playbox,exitbox,controlwin,hardbox = control()
#check for a mouse click
    mouse = controlwin.checkMouse()
#while the exit box is not clicked
    while not isclicked(mouse,exitbox):
        mouse = controlwin.checkMouse()
#if the play is clicked
        if isclicked(mouse,playbox):
#close the control window
            controlwin.close()
#call the take quiz, return the # correct
            score = takeQuiz()
#call the board and bins/pins using the game window returned
            gamewin,chiptext,scoretext, = board()
            bins(gamewin)
            newlist = pins(gamewin)
#call the drop function using the # correct returned, and the chip/score texts
            drop(score,gamewin,newlist,chiptext,scoretext)
#once again call the control window
            playbox,exitbox,controlwin,hardbox = control()
#if the hard mode is clicked
        elif isclicked(mouse,hardbox):
#everything is the same as previous
            controlwin.close()
#except instead of calling takequiz, call the hard mode version of take quiz
            score2 = takeQuizHard()
            gamewin,chiptext,scoretext = board()
            bins(gamewin)
            newlist = pins(gamewin)
            drop(score2,gamewin,newlist,chiptext,scoretext)
            playbox,exitbox,controlwin,hardbox = control()
#close the control window
    controlwin.close()

main()
