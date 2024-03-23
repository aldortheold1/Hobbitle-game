from tkinter import *
from tkinter import messagebox
import random

LANG = "ENG"
THEME = "LIGHT"

ALL_TRIES = 0
ALL_WINS = 0
CURRENT_STREAK = 0
STREAKS = [0]
BEST_STREAK = max(STREAKS)

while True:
    window = Tk()
    window.geometry("574x725")
    from images import *
    if LANG == "ENG":
        window.title("Hobbitle")
    elif LANG == "RU":
        window.title("Хоббитли")
    window.iconphoto(True, gameLogo)
    window.resizable(False, False)
    if THEME == "LIGHT":
        window.config(background="#f0f0f0")
    elif THEME == "DARK":
        window.config(background="#111111")

    def newGame():
        window.destroy()

    keyboard = [
        gandalf, bilbo, thorin, elrond, beorn, balin, dwalin,
        gloin, fili, kili, troll, gollum, greatGoblin, smaug
    ]
    solution = random.sample(keyboard, 5)

    guesses, gButtons = [[], [], [], [], [], []], [[], [], [], [], [], []]

    congrats = random.choice([awesome, excellent, greatJob, outstanding, wellDone])
    congratsRu = random.choice([awesomeRu, excellentRu, greatJobRu, outstandingRu, wellDoneRu])

    def rulesCall():

        def closeInfo():
            rulesLabel.destroy()
            closeButton.destroy()

        rulesLabel = Label(window, bg="#002b82")
        closeButton = Button(window, bg="#002b82", activebackground="#002b82", command=closeInfo)
        if LANG == "ENG":
            rulesLabel.config(image=rules), closeButton.config(image=closeR)
        elif LANG == "RU":
            rulesLabel.config(image=rulesRu), closeButton.config(image=closeR)
        rulesLabel.place(x=0, y=0), closeButton.place(x=494, y=18)

    aboutButton = Button(window, width=50, height=50, image=logo, command=rulesCall)
    titleLabel = Label(window, text="HOBBITLE", font=("Courier New", 50, "bold"), fg="#daaf00")

    lines = [Label(window, width=110, height=70, image=label, relief=RAISED) for _ in range(30)]
    lineGroups = [lines[:5], lines[5:10], lines[10:15], lines[15:20], lines[20:25], lines[25:]]
    
    if THEME == "LIGHT":
        aboutButton.config(bg="#f0f0f0", activebackground="#f0f0f0")
        if LANG == "ENG":
            titleLabel.config(text="HOBBITLE", bg="#f0f0f0")
        elif LANG == "RU":
            titleLabel.config(text="ХОББИТЛИ", bg="#f0f0f0")    
        for field in lines:
            field.config(bg="#f0f0f0")
    elif THEME == "DARK":
        aboutButton.config(bg="#222222", activebackground="#222222")
        if LANG == "ENG":
            titleLabel.config(text="HOBBITLE", bg="#111111")
        elif LANG == "RU":
            titleLabel.config(text="ХОББИТЛИ", bg="#111111")
        for field in lines:
            field.config(bg="#222222")

    aboutButton.place(x=10, y=10), titleLabel.place(x=100, y=0)

    xPlace, yPlace = 10, 70
    for yAxis in range(6):
        for xAxis in range(1, 6):
            lines[xAxis + yAxis * 5 - 1].place(x=xPlace, y=yPlace)
            xPlace += 110
        xPlace = 10
        yPlace += 70

    count = 0

    def charCall(char: PhotoImage):
        global count, guesses, gButtons, keyButtons, keyboard
        currentGuess = min(count // 5, 5)
        while count < 30:
            lines[count].config(image=char)
            guesses[currentGuess].append(char)
            gButtons[currentGuess].append(keyButtons[keyboard.index(char)])
            count += 1
            break

    def enterCall():
        global count, lineGroups, guesses, gButtons
        global ALL_TRIES, ALL_WINS, STREAKS, CURRENT_STREAK, BEST_STREAK
        congratsLabel = Label(window, width=554, height=215, bg="#179923")
        theSolWasLabel = Label(window, width=554, height=215, bg="#9a0000")
        newGameButton = Button(window, bg="#002b82", command=newGame)
        exitButton = Button(window, bg="#f0a510", command=quit)
        currentGuess = count // 5 - 1
        guessedCombo = guesses[currentGuess]
        currentLine, currentGButton = lineGroups[currentGuess], gButtons[currentGuess]
        if LANG == "ENG":
            congratsLabel.config(image=congrats), theSolWasLabel.config(image=theSolWas)
            newGameButton.config(image=playAgain), exitButton.config(image=imgExit)
        elif LANG == "RU":
            congratsLabel.config(image=congratsRu), theSolWasLabel.config(image=theSolWasRu)
            newGameButton.config(image=playAgainRu), exitButton.config(image=imgExitRu)
        if count % 5 == 0:
            if guessedCombo == solution:
                for character in currentLine:
                    character.config(bg="#08c700")
                for keyButton in currentGButton:
                    keyButton.config(bg="#08c700", activebackground="#08c700")
                congratsLabel.place(x=10, y=500)
                newGameButton.place(x=62, y=610)
                exitButton.place(x=312, y=610)
                ALL_TRIES += 1
                ALL_WINS += 1
                CURRENT_STREAK += 1
                STREAKS.append(CURRENT_STREAK)
                BEST_STREAK = max(STREAKS)
            else:
                for character in guessedCombo:
                    if character in solution:
                        if guessedCombo.index(character) == solution.index(character):
                            currentLine[guessedCombo.index(character)].config(bg="#08c700")
                            currentGButton[guessedCombo.index(character)].config(bg="#08c700", activebackground="#08c700")
                        else:
                            currentLine[guessedCombo.index(character)].config(bg="#ffcd00")
                            currentGButton[guessedCombo.index(character)].config(bg="#ffcd00", activebackground="#ffcd00")
                    else:
                        currentLine[guessedCombo.index(character)].config(bg="#9e9e9e")
                        currentGButton[guessedCombo.index(character)].config(bg="#9e9e9e", activebackground="#9e9e9e")
                if count == 30:
                    theSolWasLabel.place(x=10, y=500)
                    Label(window, image=solution[0], width=104, height=68, bg="#ff9165").place(x=28, y=550)
                    Label(window, image=solution[1], width=104, height=68, bg="#ff9165").place(x=130, y=550)
                    Label(window, image=solution[2], width=104, height=68, bg="#ff9165").place(x=233, y=550)
                    Label(window, image=solution[3], width=104, height=68, bg="#ff9165").place(x=336, y=550)
                    Label(window, image=solution[4], width=104, height=68, bg="#ff9165").place(x=439, y=550)
                    newGameButton.place(x=62, y=625)
                    exitButton.place(x=312, y=625)
                    ALL_TRIES += 1
                    CURRENT_STREAK = 0

    def backspaceCall():
        global count, guesses, gButtons
        currentGuess = min(count // 5, 5)
        try:
            while count > 0:
                lines[count - 1].config(image=label)
                guesses[currentGuess].remove(guesses[currentGuess][-1])
                gButtons[currentGuess].remove(gButtons[currentGuess][-1])
                count -= 1
                break
        except IndexError:
            if LANG == "ENG":
                errorQuit = messagebox.askokcancel(
                    title="Unexpected error!",
                    message="Unexpected error occurred while deleting the character. Would you like to restart the game?"
                )
            elif LANG == "RU":
                errorQuit = messagebox.askokcancel(
                    title="Неожиданная ошибка!",
                    message="Неожиданная ошибка произошла во время удаления персонажа. Перезапустить игру?"
                )
            if errorQuit:
                window.destroy()

    gandalfButton = Button(window, width=110, height=70, image=gandalf, command=lambda: charCall(gandalf))
    bilboButton = Button(window, width=110, height=70, image=bilbo, command=lambda: charCall(bilbo))
    thorinButton = Button(window, width=110, height=70, image=thorin, command=lambda: charCall(thorin))
    elrondButton = Button(window, width=110, height=70, image=elrond, command=lambda: charCall(elrond))
    beornButton = Button(window, width=110, height=70, image=beorn, command=lambda: charCall(beorn))
    balinButton = Button(window, width=110, height=70, image=balin, command=lambda: charCall(balin))
    dwalinButton = Button(window, width=110, height=70, image=dwalin, command=lambda: charCall(dwalin))
    gloinButton = Button(window, width=110, height=70, image=gloin, command=lambda: charCall(gloin))
    filiButton = Button(window, width=110, height=70, image=fili, command=lambda: charCall(fili))
    kiliButton = Button(window, width=110, height=70, image=kili, command=lambda: charCall(kili))
    enterButton = Button(window, width=55, height=70, image=enter, command=enterCall)
    trollButton = Button(window, width=110, height=70, image=troll, command=lambda: charCall(troll))
    gollumButton = Button(window, width=110, height=70, image=gollum, command=lambda: charCall(gollum))
    greatGoblinButton = Button(window, width=110, height=70, image=greatGoblin, command=lambda: charCall(greatGoblin))
    smaugButton = Button(window, width=110, height=70, image=smaug, command=lambda: charCall(smaug))
    backspaceButton = Button(window, width=55, height=70, image=backspace, command=backspaceCall)
    
    gandalfButton.place(x=10, y=500), bilboButton.place(x=120, y=500), thorinButton.place(x=230, y=500)
    elrondButton.place(x=340, y=500), beornButton.place(x=450, y=500), balinButton.place(x=10, y=570)
    dwalinButton.place(x=120, y=570), gloinButton.place(x=230, y=570), filiButton.place(x=340, y=570)
    kiliButton.place(x=450, y=570), enterButton.place(x=10, y=640), trollButton.place(x=65, y=640)
    gollumButton.place(x=175, y=640), greatGoblinButton.place(x=285, y=640), smaugButton.place(x=395, y=640)
    backspaceButton.place(x=505, y=640)

    keyButtons = [
        gandalfButton, bilboButton, thorinButton, elrondButton, beornButton, balinButton, dwalinButton,
        gloinButton, filiButton, kiliButton, trollButton, gollumButton, greatGoblinButton, smaugButton
    ]

    if THEME == "LIGHT":
        for keyButton in keyButtons:
            keyButton.config(bg="#f0f0f0", activebackground="#f0f0f0")
        enterButton.config(image=enter, bg="#f0f0f0", activebackground="#f0f0f0")
        backspaceButton.config(image=backspace, bg="#f0f0f0", activebackground="#f0f0f0")
    
    elif THEME == "DARK":
        for keyButton in keyButtons:
            keyButton.config(bg="#222222", activebackground="#222222")
        enterButton.config(image=enterLight, bg="#222222", activebackground="#222222")
        backspaceButton.config(image=backspaceLight, bg="#222222", activebackground="#222222")
    
    def russian():
        global LANG
        LANG = "RU"
        titleLabel.config(text="ХОББИТЛИ"), window.title("Хоббитли")

    def english():
        global LANG
        LANG = "ENG"
        titleLabel.config(text="HOBBITLE"), window.title("Hobbitle")

    def lightTheme():
        global THEME
        THEME = "LIGHT"
        for line in lines:
            line.config(bg="#f0f0f0")
        for keyButton in keyButtons:
            keyButton.config(bg="#f0f0f0", activebackground="#f0f0f0")
        window.config(background="#f0f0f0"), titleLabel.config(bg="#f0f0f0")
        aboutButton.config(bg="#f0f0f0", activebackground="#f0f0f0")
        statsButton.config(bg="#f0f0f0", activebackground="#f0f0f0", image=stats)
        settingsButton.config(bg="#f0f0f0", activebackground="#f0f0f0", image=settings)
        enterButton.config(bg="#f0f0f0", activebackground="#f0f0f0", image=enter)
        backspaceButton.config(bg="#f0f0f0", activebackground="#f0f0f0", image=backspace)

    def darkTheme():
        global THEME
        THEME = "DARK"
        for line in lines:
            line.config(bg="#222222")
        for keyButton in keyButtons:
            keyButton.config(bg="#222222", activebackground="#222222")
        window.config(background="#111111"), titleLabel.config(bg="#111111")
        aboutButton.config(bg="#222222", activebackground="#222222")
        statsButton.config(bg="#222222", activebackground="#222222", image=statsLight)
        settingsButton.config(bg="#222222", activebackground="#222222", image=settingsLight)
        enterButton.config(bg="#222222", activebackground="#222222", image=enterLight)
        backspaceButton.config(bg="#222222", activebackground="#222222", image=backspaceLight)

    def settingsCall():

        def closeSettings():
            settingsListLabel.destroy(), closeButton.destroy()
            lightButtonB.destroy(), darkButtonB.destroy()
            russianButtonB.destroy(),englishButtonB.destroy()

        settingsListLabel = Label(window, width=574, height=725, bg="#002b82")
        closeButton = Button(window, image=closeR, bg="#002b82", activebackground="#002b82", command=closeSettings)
        lightButtonB = Button(window, bg="#002b82", activebackground="#002b82", command=lightTheme)
        darkButtonB = Button(window, bg="#002b82", activebackground="#002b82", command=darkTheme)
        russianButtonB = Button(window, bg="#002b82", activebackground="#002b82", command=russian)
        englishButtonB = Button(window, bg="#002b82", activebackground="#002b82", command=english)
        if LANG == "ENG":
            settingsListLabel.config(image=settingsList), lightButtonB.config(image=lightButton)
            darkButtonB.config(image=darkButton), russianButtonB.config(image=russianButton) 
            englishButtonB.config(image=englishButton)
        elif LANG == "RU":
            settingsListLabel.config(image=settingsListRu), lightButtonB.config(image=lightButtonRu)
            darkButtonB.config(image=darkButtonRu), russianButtonB.config(image=russianButtonRu) 
            englishButtonB.config(image=englishButtonRu)
        settingsListLabel.place(x=0, y=0), closeButton.place(x=494, y=18), lightButtonB.place(x=300, y=220),
        darkButtonB.place(x=300, y=300), russianButtonB.place(x=300, y=410), englishButtonB.place(x=300, y=490)

    def statsCall():

        def closeStats():
            statsWLabel.destroy(), closeButton1.destroy()
            allTriesLabel.destroy(), percentageLabel.destroy()
            currentStreakLabel.destroy(), bestStreakLabel.destroy()
        statsWLabel = Label(window, width=560, height=248, bg="#002b82")

        if LANG == "ENG":
            statsWLabel.config(image=statsW)
        elif LANG == "RU":
            statsWLabel.config(image=statsWRu)
        statsWLabel.place(x=5, y=242)
        closeButton1 = Button(window, image=closeSt, bg="#002b82", activebackground="#002b82", command=closeStats)
        closeButton1.place(x=498, y=262)
        allTriesLabel = Label(window, bg="#bdd7ee", fg="#002b82", width=3, text=ALL_TRIES, font=("Bandshift", 38))
        allTriesLabel.place(x=44, y=348)
        percentageLabel = Label(window, bg="#bdd7ee", fg="#002b82", width=4, font=("Bandshift", 38))
        try:
            percentageLabel.config(text=f"{round((ALL_WINS / ALL_TRIES) * 100)}%")
        except ZeroDivisionError:
            percentageLabel.config(text="0%")
        percentageLabel.place(x=142, y=348)
        currentStreakLabel = Label(window, bg="#bdd7ee", fg="#002b82", width=3, text=CURRENT_STREAK, font=("Bandshift", 38))
        currentStreakLabel.place(x=280, y=348)
        bestStreakLabel = Label(window, bg="#bdd7ee", fg="#002b82", width=3, text=BEST_STREAK, font=("Bandshift", 38))
        bestStreakLabel.place(x=420, y=348)
    
    settingsButton = Button(window, width=50, height=50, command=settingsCall)
    statsButton = Button(window, width=50, height=50, command=statsCall)
    
    if THEME == "LIGHT":
        settingsButton.config(image=settings, bg="#f0f0f0", activebackground="#f0f0f0")
        statsButton.config(image=stats, bg="#f0f0f0", activebackground="#f0f0f0")
    elif THEME == "DARK":
        settingsButton.config(image=settingsLight, bg="#222222", activebackground="#222222")
        statsButton.config(image=statsLight, bg="#222222", activebackground="#222222")

    settingsButton.place(x=510, y=10), statsButton.place(x=450, y=10)
    
    window.mainloop()
