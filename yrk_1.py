# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 00:16:53 2023

@author: jfsym
"""

from random import randint
from random import random

season_names_list = ["", "Winter", "Growing", "Harvest"]
#Dim vx(3) = (0, 13, 21, 22) ' Village x-coordinates
#Dim vy(3) = (0,  8, 12, 18) ' Village y-coordinates
#Variables:
#food                    ' Food.
#people                  ' Population.
#turn                    ' Turn.
#season                  ' Season.
#year                    ' Year.
#workers                 ' People defending the dyke.
#farmers                 ' People working in the fields.
#soldiers                ' People defending the villages.
#planted!                 ' Baskets of rice planted in the fields.
#flooded(3)              ' Is a village flooded ? (boolean)
#flood_deaths            ' Number of deaths caused by flooding.
#flood_losses            ' Food lost to flooding.
#thief_deaths            ' Number of deaths caused by thieves.
#thief_losses            ' Food lost to thieves.
#starvation_deaths       ' Number of deaths caused by starvation.
#num_flooded             ' Number of flooded villages.
#was_attacked            ' Was there an attack ? (boolean)
#was_flooded             ' Was there a flood ? (boolean)

def titlepage():
    pass

def instructions():
    print("The kingdom is three villages. It")
    print("is between the Yellow River and")
    print("the mountains.")
    print("You have been chosen to take")
    print("all the important decisions. Your")
    print("poor predecessor was executed by")
    print("thieves who live in the nearby")
    print("mountains.")
    print("These thieves live off the ")
    print("villagers and often attack. The")
    print("rice stored in the villages must")
    print("be protected at all times.")
    x = input("Press any key to continue")
    print("The year consists of three long ")
    print("seasons, Winter, Growing and")
    print("Harvest. Rice is planted every")
    print("Growing Season. You must decide")
    print("how much is planted.")    
    print("The river is likely to flood the")
    print("fields and the villages. The high")
    print("dyke between the river and the")
    print("fields must be kept up to prevent")
    print("a serious flood.")
    print("The people live off the rice that")
    print("they have grown. It is a very poor")
    print("living. You must decide what the")
    print("people will work at each season")
    print("so that they prosper under your")
    print("leadership.")


 

while play_again = True:
    gameloop()

def gameloop():
    pass
'''
Sub procTITLEPAGE()
  procMAP()
  Pause 2000
  print( 11, Space$(200))
  twm.foreground(twm.YELLOW)
  twm.bold(1)
  twm.print_at(12, 12, "YELLOW RIVER")
  twm.print_at(12, 13, "   KINGDOM    ")
  twm.bold(0)
  twm.print_at(18 - Len(VERSION$) \ 2, 14, VERSION$)
  Local i = fnINKEY(10000, 1) ' 10 seconds
End Sub

Sub procMAP()
  Local i
  twm.switch(win1)
  twm.cls()

  ' Print river.
  twm.foreground(twm.YELLOW)
  For i = 3 To 23
    twm.print_at(1, i, Chr$(219))
  Next

  ' Print dam.
  twm.foreground(twm.CYAN)
  For i = 3 To 23
    twm.print_at(3, i, Chr$(221) + Chr$(221))
  Next

  ' Print mountains.
  twm.foreground(twm.RED)
  For i = 3 To 21 Step 2
    twm.print_at(29, i, Chr$(222))
    twm.print_at(28, i + 1, Chr$(220) + Chr$(219) + Chr$(219) + Chr$(220) + "  " + Chr$(222))
    twm.print_at(33, i + 2, Chr$(220) + Chr$(219) + Chr$(219) + Chr$(220))
  Next

  ' Print thieves.
  For i = 13 To 15 : twm.print_at(30, i, "  ") : Next
  twm.print_at(30, 14, "THIEVES")
  twm.print_at(31, 13, "TT")
  twm.print_at(31, 15, "T")
  twm.print_at(32, 16, "T")
  twm.print_at(32, 17, "T")

  ' Print villages.
  For i = 1 To 3 : procVDRAW(i) : Next

  twm.foreground(twm.white)
  print( 23, "   DYKE        VILLAGES      MOUNTAINS")
End Sub

Sub procVDRAW(i)
  twm.foreground(twm.GREEN)
  twm.print_at(vx(i) - 1, vy(i), Chr$(138) + Chr$(165))
  twm.print_at(vx(i) - 1, vy(i) + 1, Chr$(165) + Chr$(138))
End Sub
'''


def reinit():
    food = 5000 + randint(0,2000)
    people = 300 + randint(0,100)
    turn = 0

Sub procGAMELOOP()
  Do

    procNEWTURN()
    procBEGINSEASON()
    procMAP()
    procHEADER()

    If fnRND(2) = 1 Then
      procATTACK()
      procFLOOD()
    Else
      procFLOOD()
      procATTACK()
    EndIf

    procCALCULATE()
    procENDSEASON()

    If people <= 0 Or food <= 0 Then Exit Do

    If turn Mod 12 = 0 Then
      If Not fnRITUAL() Then Exit Do
    EndIf

    If people < 200 And fnRND(3) = 1 Then procADDTHIEVES()

    ' Make babies.
    people = Int(people * 1.045)

  Loop
End Sub

def newturn()
    Inc turn
    season = (turn - 1)%3 + 1
    year = (turn - 1) \ 3 + 1
    
    for i in range(1,3):
        flooded(i) = 0
    flood_deaths = 0
    flood_losses = 0
    thief_deaths = 0
    thief_losses = 0
    num_flooded = 0
    was_flooded = 0
    was_attacked = 0

def beginseason():
    print("Census Results")
    if turn == 1:
        print("You have inherited this situation")
        print("from your unlucky predecessor. It")
        print("is the start of the Winter Season.")
    else:
        print("At the start of the " + season_name(season) + " Season")
        print("of year "+ str(year) + " of your reign this is")
        print("the situation.")
    
    
      print("Allowing for births and deaths,")
      print("the population is " + str(people) + ".")
    
      print("There are " + str(food) + " baskets of rice")
      print("in the village stores.")
    
      print("How many people should:")
      print(" A) Defend the dyke......")
      print(" B) Work in the fields...")
      print(" C) Protect the villages.")

    # Prompt for number of people to defend the dyke.
    Do
      twm.print_at(26, 14)
      workers = fnNUMINP()
      If workers > people Then procIMPOS() Else Exit Do
    Loop
    
    # Prompt for number of people to work in the fields.
    If workers = people Then
      farmers = 0
      twm.print_at(26, 15, "0")
    Else
      Do
        twm.print_at(26, 15)
        farmers = fnNUMINP()
        If workers + farmers > people Then procIMPOS() Else Exit Do
      Loop
    EndIf
  ' Calculate the number of people to protect the villages.
  soldiers = people - workers - farmers
  twm.print_at(26, 16, Str$(soldiers))

  If season = 2 Then
    print( 18, "How many baskets of rice will be")
    print( 19, "planted in the fields.....")
    Do
      twm.print_at(26, 19)
      planted! = fnNUMINP()
      If planted! > food Then procIMPOS()
    Loop Until planted! <= food
    Inc food, -planted!
  EndIf

  procSPACE()
End Sub

Sub procIMPOS()
  twm.inverse(1)
  twm.bold(1)
  twm.print_at(5, 20, " I M P O S S I B L E ")
  twm.inverse(0)
  twm.bold(0)
  Pause 2000
  procSPACE()
  twm.print_at(5, 20, "                     ")
End Sub

Sub procHEADER()
  twm.foreground(twm.WHITE)
  twm.bold(1)
  twm.print_at(1,  1, season_name$(season) + " Season")
  twm.print_at(28, 1, "Year " + Str$(year))
  twm.bold(0)
End Sub

def attack():
# There can be no attack if all the villages have been flooded.
    if num_flooded == 3:
        return

#  Select Case season
    Case 1    : If Rnd() < 0.5 Then Exit Sub ' 50 likely to attack in winter
    Case 2    : If Rnd() < 0.2 Then Exit Sub ' 80 likely to attack in growing season
    Case 3    : If Rnd() < 0.6 Then Exit Sub ' 40 likely to attack in harvest season
    Case Else : Error "Unknown season " + Str$(season)
  End Select

  ' There has been an attack.
  was_attacked = 1

  ' Select an unflooded village to attack.
  Local village
  Do
    village = fnRND(3)
  Loop Until Not flooded(village)

  Local x = 32, y
  Local wx = vx(village)
  Local wy = vy(village) - 1
  Local d ' direction
  If wy < 17 Then
    y = 13 : d = -1
  Else
    y = 17 : d = 1
  EndIf
  Local sy = y

  twm.foreground(twm.RED)

  ' Move the thief vertically towards village.
  Do
    twm.print_at(x, y, " ")
    If y = wy Then Exit Do
    Inc y, d
    twm.print_at(x, y, "T")
    Pause 50
  Loop

  ' Move the thief horizontally toward village.
  Do While x > wx
    Inc x, -1
    twm.print_at(x, y, "T")
    Pause 1000 * (1 - Min(0.9, (x - wx) / 5))
    twm.print_at(x, y, Choice(x = 29, Chr$(222), " "))
  Loop

  ' Attack the village.
  twm.foreground(twm.GREEN)
  Local i
  For i = 1 To 40
    twm.print_at(x, y + 1, Mid$("\|/-", 1 + i Mod 4, 1))
    Pause 40
  Next

  procVDRAW(village)

  twm.foreground(twm.RED)

  ' Move the thief horizontally back to the mountains.
  Do While x < 32
    twm.print_at(x, y, Choice(x = 29, Chr$(222), " "))
    Inc x
    twm.print_at(x, y, "T")
    Pause 40
  Loop

  ' Move the thief vertically back to the mountains.
  Do While y <> sy
    twm.print_at(x, y, " ")
    Inc y, -d
    twm.print_at(x, y, "T")
    Pause 50
  Loop

  ' How effective were the thieves ?
  Select Case season
    Case 1 : i = 200 + fnRND(70) - soldiers
    Case 2 : i = 30 + fnRND(200) - soldiers
    Case 3 : i = fnRND(400) - soldiers
    Case Else
      Error "Unknown season: " + Str$(season)
  End Select
  If i < 0 Then i = 0

  ' Thieves kill people.
  thief_deaths = Int(soldiers * i / 400)
  soldiers = soldiers - thief_deaths

  ' Thieves steal food.
  thief_losses = Int(i * food / 729 + fnRND(2000 - soldiers) / 10)
  If thief_losses < 0 Then
    thief_losses = 0
  ElseIf thief_losses > 2000 Then
    thief_losses = 1900 + fnRND(200)
  EndIf
  Inc food, -thief_losses
End Sub

def flood():
    #Flood severity.
    fs=0
    if season == 1:
        fs = randint(1,330) / (workers + 1)
    elif season ==2:
        fs = (randint(1,100) + 60) / (workers + 1)
    elif season == 3:
        return
    else:
        print ("Unknown season " + str(season))
    
    if fs < 1.0:
        return
    
    was_flooded = 1
    
    x = 6
    y = randint(1,8) + 10
    twm.foreground(twm.YELLOW)
    twm.print_at(1, y, Chr$(219) + Chr$(219) + Chr$(219) + Chr$(219) + Chr$(219) + Chr$(219))
    
    Local k, key = -1, v, w1, w2
    fs! = fnRND(Choice(fs! < 2.0, 2.0, 4.0))
For k = 1 To fs! * 100
    Do
      Select Case fnRND(4)
        Case 1 : If x < 25 Then Inc x     : Exit Do
        Case 2 : If x > 6  Then Inc x, -1 : Exit Do
        Case 3 : If y < 22 Then Inc y     : Exit Do
        Case 4 : If y > 3  Then Inc y, -1 : Exit Do
      End Select
    Loop

    ' Have any of the villages flooded ?
    For v = 1 To 3
      w1 = vx(v) - x
      w2 = y - vy(v)
      If w2 = 0 Or w2 = 1 Then
        If w1 = 0 Or w1 = 1 Then flooded(v) = 1 : Inc num_flooded
        If w1 = -1 Then Exit For
      EndIf
    Next

    twm.print_at(x, y, Chr$(219))

    If key = -1 Then key = fnINKEY(100, k = 1)
  Next

  ' Deaths.
  Local orig_pop  = workers + farmers + soldiers
  workers = Int((workers / 10) * (10 - fs!))
  farmers = Int((farmers / 10) * (10 - fs!))
  soldiers = Int((soldiers / 6) * (6 - num_flooded))
  flood_deaths = orig_pop - workers - farmers - soldiers

  ' Loss of food from the villages.
  flood_losses = Int(food * num_flooded / 6)
  Inc food, -flood_losses

  ' Loss of rice in the fields.
  Select Case season
    Case 1    : ' Nothing
    Case 2    : planted! = planted! * (20 - fs!) / 20
    Case 3    : planted! = planted! * (10 - fs!) / 10
    Case Else : Error "Unknown season " + Str$(season)
  End Select
End Sub

Sub procCALCULATE()

  ' How much grain have we grown ?
  If farmers = 0 Then
    planted! = 0
  Else
    Select Case season
      Case 1 : ' No grain grown during the winter.
      Case 2
        If planted! > 1000 Then planted! = 1000
        planted! = planted! * (farmers - 10) / farmers
      Case 3
        If planted! > 0 Then planted! = 18 * (11 + fnRND(3)) * (0.05 - 1 / farmers) * planted!
        If planted! > 0 Then food = food + Int(planted!)
      Case Else
        Error "Unknown season " + Str$(season)
    End Select
  EndIf

  ' How many people have starved ?
  starvation_deaths = 0
  people = workers + farmers + soldiers
  If people <= 0 Then Exit Sub ' Everyone is dead!

  Local t! = food / people
  If t! > 5 Then
    t! = 4
  ElseIf t! < 2 Then
    people = 0
  ElseIf t! > 4 Then
    t! = 3.5
  Else
    starvation_deaths = Int(people * (7 - t!) / 7)
    t! = 3
  EndIf

  If people > 0 Then
    Inc people, -starvation_deaths
    food = Int(food - people * t! - starvation_deaths * t! / 2)
    If food < 0 Then food = 0
  EndIf
End Sub

Sub procENDSEASON()
  Pause 2000
  If food <= 0 Then
    procYELLOW()
    print(  7, "There was no food left. All of the")
    print(  8, "people have run off and joined up")
    print(  9, "with the thieves after " + Str$(turn) + " seasons")
    print( 10, "of your misrule")
    procSPACE()
    Exit Sub
  EndIf

  If people <= 0 Then
    procYELLOW()
    print(  8, "There is no-one left! They have all")
    print(  9, "been killed off by your decisions ")
    print( 10, "after only " + Str$(year) + Choice(year = 1, " year.", " years."))
    procSPACE()
    Exit Sub
  EndIf

  Local f1! = people / (flood_deaths + thief_deaths + starvation_deaths + 1)
  Local f2! = food / (flood_losses + thief_losses + 1)
  Local msg$
  If f2! < f1! Then f1! = f2!
  If f2! < 2 Then
    msg$ = "Disastrous Losses!"
  ElseIf f1! < 4 Then
    msg$ = "Worrying losses!"
  ElseIf f1! < 8 Then
    msg$ = "You got off lightly!"
  ElseIf food / people < 4 Then
    msg$ = "Food supply is low."
  ElseIf food / people < 2 Then
    msg$ = "Starvation Imminent!"
  ElseIf was_attacked + was_flooded + starvation_deaths > 0 Then
    msg$ = "Nothing to worry about."
  Else
    twm.bold(1)
    twm.print_at(1, 11, "                                      ")
    twm.print_at(1, 12, "             A quiet season           ")
    twm.print_at(1, 13, "                                      ")
    twm.bold(0)
    Pause 2000
    Exit Sub
  EndIf

  procYELLOW()
  twm.print_at(3, 2, "Village Leader's Report")

  twm.inverse(1)
  twm.print_at(13 - Len(msg$) / 2, 4, " " + msg$ + " ")
  twm.inverse(0)

  print(  6, "In the " + season_name$(season) + " Season of year " + Str$(year))
  print(  7, "of your reign, the kingdom has")
  print(  8, "suffered these losses:")

  print( 10, "Deaths from floods......... " + Str$(flood_deaths))
  print( 11, "Deaths from the attacks.... " + Str$(thief_deaths))
  print( 12, "Deaths from starvation..... " + Str$(starvation_deaths))
  print( 13, "Baskets of rice")
  print( 14, "  lost during the floods... " + Str$(flood_losses))
  print( 15, "Baskets of rice")
  print( 16, "  lost during the attacks.. " + Str$(thief_losses))

  print( 18, "The village census follows.")
  procSPACE()
End Sub

Function fnRITUAL()
  procYELLOW()

  print(  3, "We have survived for " + Str$(year) + " years")
  print(  4, "under your glorious control.")
  print(  5, "By an ancient custom we must")
  print(  6, "offer you the chance to lay")
  print(  7, "down this terrible burden and")
  print(  8, "resume a normal life.")

  print( 10, "In the time honoured fashion")
  print( 11, "I will now ask the ritual")
  print( 12, "question:")

  Pause 2000

  print( 14, "Are you prepared to accept")
  print( 15, "the burden of decision again?")

  print( 17, "You need only answer Yes or No")
  print( 18, "for the people will understand")
  print( 19, "your reasons.")

  print( 21)
  fnRITUAL = fnYESORNO()
End Function

Sub procADDTHIEVES()
  procYELLOW()
  print(  8, "Thieves have come out of the")
  print(  9, "mountain to join you. They")
  print( 10, "have decided that it will be")
  print( 11, "easier to grow the rice than")
  print( 12, "to steal it!")
  procSPACE()
  people = people + 50 + fnRND(100)
End Sub

' Prompts the user to play again.
'
' @return  1 if the user wants to play again, otherwise 0.
Function fnPLAYAGAIN()
  procYELLOW()
  print(  9, "Press the ENTER key to start again.")
  print( 11, "Press the ESCAPE key to leave the")
  print( 12, "program.")

  procKCL()
  Do
    Select Case Inkey$
      Case Chr$(10), Chr$(13) : fnPLAYAGAIN = 1 : Exit Function
      Case Chr$(27)           : fnPLAYAGAIN = 0 : Exit Function
    End Select
  Loop
End Function

Sub procYELLOW()
  twm.switch(win1)
  twm.cls()
  twm.switch(win2)
  twm.cls()
  twm.foreground(twm.YELLOW)
End Sub

' Waits approximately 'duration' milliseconds for a key press.
'
' @param  duration   milliseconds to wait.
' @param  clear_buf  if 1 then clear the keyboard buffer first.
' @return             ASCII code of the key pressed, or -1 if none was pressed.
Function fnINKEY(duration, clear_buf)
  If clear_buf Then procKCL()

  Local i, k$
  Do
    k$ = Inkey$
    If k$ <> "" Then Exit Do
    Pause 10
    Inc i, 10
  Loop Until i >= duration
  fnINKEY = Choice(k$ = "", -1, Asc(k$))
End Function

' Clears the keyboard buffer.
Sub procKCL()
  Do While Inkey$ <> "" : Loop
  Pause 100 ' Make sure we deal with any delayed LF following a CR.
  Do While Inkey$ <> "" : Loop
End Sub

' General purpose input routine.
Function fnGPI$(expect_num, max_length)
  Local x = twm.x, y = twm.y
  twm.print_at(x, y, String$(max_length, " "))
  twm.print_at(x - 1, y, " ")
  twm.enable_cursor(1)

  procKCL()
  Local k$, kcode

  Do
    Do : k$ = Inkey$ : Loop Until k$ <> ""
    kcode = Asc(k$)

    Select Case kcode
      Case 10, 13 ' Enter
        Exit Do

      Case 8, 127 ' Delete and backspace
        If fnGPI$ <> "" Then
          fnGPI$ = Left$(fnGPI$, Len(fNGPI$) - 1)
          twm.print_at(x, y, String$(max_length, " "))
          twm.print_at(x - 1, y, " " + fnGPI$)
        EndIf

      Case < 32, > 126
        twm.bell();

      Case Else
        If expect_num And (kcode < 48 Or kcode > 57) Then
          twm.bell();
        ElseIf Len(fnGPI$) = max_length Then
          twm.bell();
        Else
          twm.print(k$)
          Cat fnGPI$, k$
        EndIf

    End Select

  Loop

  twm.enable_cursor(0)
End Function

' Gets 'Yes' / 'No' input from user.
'
' @return  1 if 'Yes', 0 if 'No'.
Sub fnYESORNO()
  Local x = twm.x
  Do
    twm.x = x
    Select Case Left$(fnGPI$(0, 3), 1)
      Case "y", "Y" : fnYESORNO = 1 : Exit Do
      Case "n", "N" : fnYESORNO = 0 : Exit Do
    End Select
  Loop
End Function

' Gets number input from user.
Function fnNUMINP()
  Local x = twm.x, y = twm.y
  fnNUMINP = Val(fnGPI$(1, 6))
  If fnNUMINP = 0 Then twm.print_at(x, y, "0")
End Function

' Generates a random integer between 1 and x.
Function fnRND(x)
  fnRND = Int(Rnd() * x) + 1
End Function
' END:       #Include "kingdom.bas" --------------------------------------------

Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
