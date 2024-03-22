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
    if LANG == "ENG":
        window.title("Hobbitle")
    elif LANG == "RU":
        window.title("Хоббитли")
    window.iconphoto(True, PhotoImage(file="img/logo.png"))
    window.resizable(False, False)
    if THEME == "LIGHT":
        window.config(background="#f0f0f0")
    elif THEME == "DARK":
        window.config(background="#111111")

    def newGame():
        window.destroy()

    logo = PhotoImage(file="img/logo_about.png")
    stats = PhotoImage(file="img/stats.png")
    statsLight = PhotoImage(file="img/stats_light.png")
    settings = PhotoImage(file="img/settings.png")
    settingsLight = PhotoImage(file="img/settings_light.png")
    enter = PhotoImage(file="img/enter.png")
    enterLight = PhotoImage(file="img/enter_light.png")
    backspace = PhotoImage(file="img/backspace.png")
    backspaceLight = PhotoImage(file="img/backspace_light.png")
    label = PhotoImage(file="img/label.png")
    awesome = PhotoImage(file="img/awesome.png")
    awesomeRu = PhotoImage(file="img/awesome_ru.png")
    excellent = PhotoImage(file="img/excellent.png")
    excellentRu = PhotoImage(file="img/excellent_ru.png")
    greatJob = PhotoImage(file="img/great_job.png")
    greatJobRu = PhotoImage(file="img/great_job_ru.png")
    outstanding = PhotoImage(file="img/outstanding.png")
    outstandingRu = PhotoImage(file="img/outstanding_ru.png")
    wellDone = PhotoImage(file="img/well_done.png")
    wellDoneRu = PhotoImage(file="img/well_done_ru.png")
    theSolWas = PhotoImage(file="img/the_sol_was.png")
    theSolWasRu = PhotoImage(file="img/the_sol_was_ru.png")
    playAgain = PhotoImage(file="img/play_again.png")
    playAgainRu = PhotoImage(file="img/play_again_ru.png")
    imgExit = PhotoImage(file="img/img_exit.png")
    imgExitRu = PhotoImage(file="img/img_exit_ru.png")
    rules = PhotoImage(file="img/rules.png")
    rulesRu = PhotoImage(file="img/rules_ru.png")
    closeR = PhotoImage(file="img/close_r.png")
    settingsList = PhotoImage(file="img/settings_list.png")
    settingsListRu = PhotoImage(file="img/settings_list_ru.png")
    darkButton = PhotoImage(file="img/dark_button.png")
    darkButtonRu = PhotoImage(file="img/dark_button_ru.png")
    lightButton = PhotoImage(file="img/light_button.png")
    lightButtonRu = PhotoImage(file="img/light_button_ru.png")
    englishButton = PhotoImage(file="img/english_button.png")
    englishButtonRu = PhotoImage(file="img/english_button_ru.png")
    russianButton = PhotoImage(file="img/russian_button.png")
    russianButtonRu = PhotoImage(file="img/russian_button_ru.png")
    statsW = PhotoImage(file="img/stats_w.png")
    statsWRu = PhotoImage(file="img/stats_w_ru.png")
    closeSt = PhotoImage(file="img/close_st.png")

    gandalf = PhotoImage(file="img/gandalf.png")
    bilbo = PhotoImage(file="img/bilbo.png")
    thorin = PhotoImage(file="img/thorin.png")
    elrond = PhotoImage(file="img/elrond.png")
    beorn = PhotoImage(file="img/beorn.png")
    balin = PhotoImage(file="img/balin.png")
    dwalin = PhotoImage(file="img/dwalin.png")
    gloin = PhotoImage(file="img/gloin.png")
    fili = PhotoImage(file="img/fili.png")
    kili = PhotoImage(file="img/kili.png")
    troll = PhotoImage(file="img/troll.png")
    gollum = PhotoImage(file="img/gollum.png")
    greatGoblin = PhotoImage(file="img/great_goblin.png")
    smaug = PhotoImage(file="img/smaug.png")

    keyboard = [gandalf, bilbo, thorin, elrond, beorn, balin, dwalin, gloin, fili, kili, troll, gollum, greatGoblin, smaug]
    solution = random.sample(keyboard, 5)
    guess1, g1B = [], []
    guess2, g2B = [], []
    guess3, g3B = [], []
    guess4, g4B = [], []
    guess5, g5B = [], []
    guess6, g6B = [], []

    guesses = [guess1, guess2, guess3, guess4, guess5, guess6]
    gButtons = [g1B, g2B, g3B, g4B, g5B, g6B]

    congratsList = [awesome, excellent, greatJob, outstanding, wellDone]
    congrats = random.choice(congratsList)

    congratsListRu = [awesomeRu, excellentRu, greatJobRu, outstandingRu, wellDoneRu]
    congratsRu = random.choice(congratsListRu)

    def closeInfo():
        global rulesLabel, closeButton
        rulesLabel.destroy()
        closeButton.destroy()

    def rulesCall():
        global rulesLabel, closeButton
        if LANG == "ENG":
            rulesLabel = Label(window, image=rules, bg="#002b82")
            closeButton = Button(window, image=closeR, bg="#002b82", activebackground="#002b82", command=closeInfo)
        elif LANG == "RU":
            rulesLabel = Label(window, image=rulesRu, bg="#002b82")
            closeButton = Button(window, image=closeR, bg="#002b82", activebackground="#002b82", command=closeInfo)
        rulesLabel.place(x=0, y=0), closeButton.place(x=494, y=18)

    aboutButton = Button(window, width=50, height=50, image=logo, command=rulesCall)
    titleLabel = Label(window, text="HOBBITLE", font=("Courier New", 50, "bold"), fg="#daaf00")

    l1 = Label(window, width=110, height=70, image=label, relief=RAISED)
    l2 = Label(window, width=110, height=70, image=label, relief=RAISED)
    l3 = Label(window, width=110, height=70, image=label, relief=RAISED)
    l4 = Label(window, width=110, height=70, image=label, relief=RAISED)
    l5 = Label(window, width=110, height=70, image=label, relief=RAISED)

    l6 = Label(window, width=110, height=70, image=label, relief=RAISED)
    l7 = Label(window, width=110, height=70, image=label, relief=RAISED)
    l8 = Label(window, width=110, height=70, image=label, relief=RAISED)
    l9 = Label(window, width=110, height=70, image=label, relief=RAISED)
    l10 = Label(window, width=110, height=70, image=label, relief=RAISED)

    l11 = Label(window, width=110, height=70, image=label, relief=RAISED)
    l12 = Label(window, width=110, height=70, image=label, relief=RAISED)
    l13 = Label(window, width=110, height=70, image=label, relief=RAISED)
    l14 = Label(window, width=110, height=70, image=label, relief=RAISED)
    l15 = Label(window, width=110, height=70, image=label, relief=RAISED)

    l16 = Label(window, width=110, height=70, image=label, relief=RAISED)
    l17 = Label(window, width=110, height=70, image=label, relief=RAISED)
    l18 = Label(window, width=110, height=70, image=label, relief=RAISED)
    l19 = Label(window, width=110, height=70, image=label, relief=RAISED)
    l20 = Label(window, width=110, height=70, image=label, relief=RAISED)

    l21 = Label(window, width=110, height=70, image=label, relief=RAISED)
    l22 = Label(window, width=110, height=70, image=label, relief=RAISED)
    l23 = Label(window, width=110, height=70, image=label, relief=RAISED)
    l24 = Label(window, width=110, height=70, image=label, relief=RAISED)
    l25 = Label(window, width=110, height=70, image=label, relief=RAISED)

    l26 = Label(window, width=110, height=70, image=label, relief=RAISED)
    l27 = Label(window, width=110, height=70, image=label, relief=RAISED)
    l28 = Label(window, width=110, height=70, image=label, relief=RAISED)
    l29 = Label(window, width=110, height=70, image=label, relief=RAISED)
    l30 = Label(window, width=110, height=70, image=label, relief=RAISED)

    line1, line2 = [l1, l2, l3, l4, l5], [l6, l7, l8, l9, l10]
    line3, line4 = [l11, l12, l13, l14, l15], [l16, l17, l18, l19, l20]
    line5, line6 = [l21, l22, l23, l24, l25], [l26, l27, l28, l29, l30]

    lines = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16,
            l17, l18, l19, l20, l21, l22, l23, l24, l25, l26, l27, l28, l29, l30]
    
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
    l1.place(x=10, y=70), l2.place(x=120, y=70), l3.place(x=230, y=70), l4.place(x=340, y=70), l5.place(x=450, y=70)
    l6.place(x=10, y=140), l7.place(x=120, y=140), l8.place(x=230, y=140), l9.place(x=340, y=140), l10.place(x=450, y=140)
    l11.place(x=10, y=210), l12.place(x=120, y=210), l13.place(x=230, y=210), l14.place(x=340, y=210), l15.place(x=450, y=210)
    l16.place(x=10, y=280), l17.place(x=120, y=280), l18.place(x=230, y=280), l19.place(x=340, y=280), l20.place(x=450, y=280)
    l21.place(x=10, y=350), l22.place(x=120, y=350), l23.place(x=230, y=350), l24.place(x=340, y=350), l25.place(x=450, y=350)
    l26.place(x=10, y=420), l27.place(x=120, y=420), l28.place(x=230, y=420), l29.place(x=340, y=420), l30.place(x=450, y=420)

    count = 0

    def charCall(char):
        global count, guesses, gButtons, guess6, g6B, keyButtons, keyboard
        while count < 30:
            lines[count].config(image=char)
            if count != 30:
                guesses[count // 5].append(char)
                gButtons[count // 5].append(keyButtons[keyboard.index(char)])
            else:
                guess6.append(char)
                g6B.append(keyButtons[keyboard.index(char)])
            count += 1
            break

    def gandalfCall():
        charCall(gandalf)

    def bilboCall():
        charCall(bilbo)

    def thorinCall():
        charCall(thorin)

    def elrondCall():
        charCall(elrond)

    def beornCall():
        charCall(beorn)

    def balinCall():
        charCall(balin)

    def dwalinCall():
        charCall(dwalin)

    def gloinCall():
        charCall(gloin)

    def filiCall():
        charCall(fili)

    def kiliCall():
        charCall(kili)

    def trollCall():
        charCall(troll)

    def gollumCall():
        charCall(gollum)

    def greatGoblinCall():
        charCall(greatGoblin)

    def smaugCall():
        charCall(smaug)

    def enterCall():
        global count, guess1, guess2, guess3, guess4, guess5, guess6, congratsLabel, theSolWasLabel
        global newGameButton, exitButton, ALL_TRIES, ALL_WINS, STREAKS, CURRENT_STREAK, BEST_STREAK
        if LANG == "ENG":
            congratsLabel = Label(window, image=congrats, width=554, height=215, bg="#179923")
            theSolWasLabel = Label(window, image=theSolWas, width=554, height=215, bg="#9a0000")
            newGameButton = Button(window, image=playAgain, bg="#002b82", command=newGame)
            exitButton = Button(window, image=imgExit, bg="#f0a510", command=quit)
        elif LANG == "RU":
            congratsLabel = Label(window, image=congratsRu, width=554, height=215, bg="#179923")
            theSolWasLabel = Label(window, image=theSolWasRu, width=554, height=215, bg="#9a0000")
            newGameButton = Button(window, image=playAgainRu, bg="#002b82", command=newGame)
            exitButton = Button(window, image=imgExitRu, bg="#f0a510", command=quit)
        if count == 5:
            if guess1 == solution:
                for character in line1:
                    character.config(bg="#08c700")
                for keyButton in g1B:
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
                for character in guess1:
                    if character in solution:
                        if guess1.index(character) == solution.index(character):
                            line1[guess1.index(character)].config(bg="#08c700")
                            g1B[guess1.index(character)].config(bg="#08c700", activebackground="#08c700")
                        else:
                            line1[guess1.index(character)].config(bg="#ffcd00")
                            g1B[guess1.index(character)].config(bg="#ffcd00", activebackground="#ffcd00")
                    else:
                        line1[guess1.index(character)].config(bg="#9e9e9e")
                        g1B[guess1.index(character)].config(bg="#9e9e9e", activebackground="#9e9e9e")
        elif count == 10:
            if guess2 == solution:
                for character in line2:
                    character.config(bg="#08c700")
                for keyButton in g2B:
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
                for character in guess2:
                    if character in solution:
                        if guess2.index(character) == solution.index(character):
                            line2[guess2.index(character)].config(bg="#08c700")
                            g2B[guess2.index(character)].config(bg="#08c700", activebackground="#08c700")
                        else:
                            line2[guess2.index(character)].config(bg="#ffcd00")
                            g2B[guess2.index(character)].config(bg="#ffcd00", activebackground="#ffcd00")
                    else:
                        line2[guess2.index(character)].config(bg="#9e9e9e")
                        g2B[guess2.index(character)].config(bg="#9e9e9e", activebackground="#9e9e9e")
        elif count == 15:
            if guess3 == solution:
                for character in line3:
                    character.config(bg="#08c700")
                for keyButton in g3B:
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
                for character in guess3:
                    if character in solution:
                        if guess3.index(character) == solution.index(character):
                            line3[guess3.index(character)].config(bg="#08c700")
                            g3B[guess3.index(character)].config(bg="#08c700", activebackground="#08c700")
                        else:
                            line3[guess3.index(character)].config(bg="#ffcd00")
                            g3B[guess3.index(character)].config(bg="#ffcd00", activebackground="#ffcd00")
                    else:
                        line3[guess3.index(character)].config(bg="#9e9e9e")
                        g3B[guess3.index(character)].config(bg="#9e9e9e", activebackground="#9e9e9e")
        elif count == 20:
            if guess4 == solution:
                for character in line4:
                    character.config(bg="#08c700")
                for keyButton in g4B:
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
                for character in guess4:
                    if character in solution:
                        if guess4.index(character) == solution.index(character):
                            line4[guess4.index(character)].config(bg="#08c700")
                            g4B[guess4.index(character)].config(bg="#08c700", activebackground="#08c700")
                        else:
                            line4[guess4.index(character)].config(bg="#ffcd00")
                            g4B[guess4.index(character)].config(bg="#ffcd00", activebackground="#ffcd00")
                    else:
                        line4[guess4.index(character)].config(bg="#9e9e9e")
                        g4B[guess4.index(character)].config(bg="#9e9e9e", activebackground="#9e9e9e")
        elif count == 25:
            if guess5 == solution:
                for character in line5:
                    character.config(bg="#08c700")
                for keyButton in g5B:
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
                for character in guess5:
                    if character in solution:
                        if guess5.index(character) == solution.index(character):
                            line5[guess5.index(character)].config(bg="#08c700")
                            g5B[guess5.index(character)].config(bg="#08c700", activebackground="#08c700")
                        else:
                            line5[guess5.index(character)].config(bg="#ffcd00")
                            g5B[guess5.index(character)].config(bg="#ffcd00", activebackground="#ffcd00")
                    else:
                        line5[guess5.index(character)].config(bg="#9e9e9e")
                        g5B[guess5.index(character)].config(bg="#9e9e9e", activebackground="#9e9e9e")
        elif count == 30:
            if guess6 == solution:
                for character in line6:
                    character.config(bg="#08c700")
                for keyButton in g6B:
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
                for character in guess6:
                    if character in solution:
                        if guess6.index(character) == solution.index(character):
                            line6[guess6.index(character)].config(bg="#08c700")
                            g6B[guess6.index(character)].config(bg="#08c700", activebackground="#08c700")
                        else:
                            line6[guess6.index(character)].config(bg="#ffcd00")
                            g6B[guess6.index(character)].config(bg="#ffcd00", activebackground="#ffcd00")
                    else:
                        line6[guess6.index(character)].config(bg="#9e9e9e")
                        g6B[guess6.index(character)].config(bg="#9e9e9e", activebackground="#9e9e9e")
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
        global count, guesses, gButtons, guess6, g6B
        try:
            while count > 0:
                lines[count - 1].config(image=label)
                if count != 30:
                    guesses[count // 5].remove(guesses[count // 5][-1])
                    gButtons[count // 5].remove(gButtons[count // 5][-1])
                else:
                    guess6.remove(guess6[-1])
                    g6B.remove(g6B[-1])
                count -= 1
                break
        except Exception:
            if LANG == "ENG":
                errorQuit = messagebox.askokcancel(title="Unexpected error!", message="Unexpected error occurred while deleting the character. Would you like to restart the game?")
            elif LANG == "RU":
                errorQuit = messagebox.askokcancel(title="Неожиданная ошибка!", message="Неожиданная ошибка произошла во время удаления персонажа. Перезапустить игру?")
            if errorQuit:
                window.destroy()

    gandalfButton = Button(window, width=110, height=70, image=gandalf, command=gandalfCall)
    bilboButton = Button(window, width=110, height=70, image=bilbo, command=bilboCall)
    thorinButton = Button(window, width=110, height=70, image=thorin, command=thorinCall)
    elrondButton = Button(window, width=110, height=70, image=elrond, command=elrondCall)
    beornButton = Button(window, width=110, height=70, image=beorn, command=beornCall)
    balinButton = Button(window, width=110, height=70, image=balin, command=balinCall)
    dwalinButton = Button(window, width=110, height=70, image=dwalin, command=dwalinCall)
    gloinButton = Button(window, width=110, height=70, image=gloin, command=gloinCall)
    filiButton = Button(window, width=110, height=70, image=fili, command=filiCall)
    kiliButton = Button(window, width=110, height=70, image=kili, command=kiliCall)
    enterButton = Button(window, width=55, height=70, image=enter, command=enterCall)
    trollButton = Button(window, width=110, height=70, image=troll, command=trollCall)
    gollumButton = Button(window, width=110, height=70, image=gollum, command=gollumCall)
    greatGoblinButton = Button(window, width=110, height=70, image=greatGoblin, command=greatGoblinCall)
    smaugButton = Button(window, width=110, height=70, image=smaug, command=smaugCall)
    backspaceButton = Button(window, width=55, height=70, image=backspace, command=backspaceCall)
    
    gandalfButton.place(x=10, y=500), bilboButton.place(x=120, y=500), thorinButton.place(x=230, y=500)
    elrondButton.place(x=340, y=500), beornButton.place(x=450, y=500), balinButton.place(x=10, y=570)
    dwalinButton.place(x=120, y=570), gloinButton.place(x=230, y=570), filiButton.place(x=340, y=570)
    kiliButton.place(x=450, y=570), enterButton.place(x=10, y=640), trollButton.place(x=65, y=640)
    gollumButton.place(x=175, y=640), greatGoblinButton.place(x=285, y=640), smaugButton.place(x=395, y=640)
    backspaceButton.place(x=505, y=640)

    keyButtons = [gandalfButton, bilboButton, thorinButton, elrondButton, beornButton, balinButton, dwalinButton,
                  gloinButton, filiButton, kiliButton, trollButton, gollumButton, greatGoblinButton, smaugButton]

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

    def closeSettings():
        global settingsListLabel, closeButton, lightButtonB, darkButtonB, englishButtonB, russianButtonB
        settingsListLabel.destroy()
        closeButton.destroy()
        lightButtonB.destroy()
        darkButtonB.destroy()
        russianButtonB.destroy()
        englishButtonB.destroy()
    
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
        global settingsListLabel, closeButton, lightButtonB, darkButtonB, englishButtonB, russianButtonB
        if LANG == "ENG":
            settingsListLabel = Label(window, image=settingsList, width=574, height=725, bg="#002b82")
            closeButton = Button(window, image=closeR, bg="#002b82", activebackground="#002b82", command=closeSettings)
            lightButtonB = Button(window, image=lightButton, bg="#002b82", activebackground="#002b82", command=lightTheme)
            darkButtonB = Button(window, image=darkButton, bg="#002b82", activebackground="#002b82", command=darkTheme)
            russianButtonB = Button(window, image=russianButton, bg="#002b82", activebackground="#002b82", command=russian)
            englishButtonB = Button(window, image=englishButton, bg="#002b82", activebackground="#002b82", command=english)
        elif LANG == "RU":
            settingsListLabel = Label(window, image=settingsListRu, width=574, height=725, bg="#002b82")
            closeButton = Button(window, image=closeR, bg="#002b82", activebackground="#002b82", command=closeSettings)
            lightButtonB = Button(window, image=lightButtonRu, bg="#002b82", activebackground="#002b82", command=lightTheme)
            darkButtonB = Button(window, image=darkButtonRu, bg="#002b82", activebackground="#002b82", command=darkTheme)
            russianButtonB = Button(window, image=russianButtonRu, bg="#002b82", activebackground="#002b82", command=russian) 
            englishButtonB = Button(window, image=englishButtonRu, bg="#002b82", activebackground="#002b82", command=english)
        settingsListLabel.place(x=0, y=0), closeButton.place(x=494, y=18), lightButtonB.place(x=300, y=220),
        darkButtonB.place(x=300, y=300), russianButtonB.place(x=300, y=410), englishButtonB.place(x=300, y=490)

    def closeStats():
        global statsWLabel, closeButton1, allTriesLabel, percentageLabel, currentStreakLabel, bestStreakLabel
        statsWLabel.destroy()
        closeButton1.destroy()
        allTriesLabel.destroy()
        percentageLabel.destroy()
        currentStreakLabel.destroy()
        bestStreakLabel.destroy()

    def statsCall():
        global LANG, statsWLabel, closeButton1, allTriesLabel, percentageLabel, currentStreakLabel, bestStreakLabel
        if LANG == "ENG":
            statsWLabel = Label(window, image=statsW, width=560, height=248, bg="#002b82")
        elif LANG == "RU":
            statsWLabel = Label(window, image=statsWRu, width=560, height=248, bg="#002b82")
        statsWLabel.place(x=5, y=242)
        closeButton1 = Button(window, image=closeSt, bg="#002b82", activebackground="#002b82", command=closeStats)
        closeButton1.place(x=498, y=262)
        allTriesLabel = Label(window, bg="#bdd7ee", fg="#002b82", width=3, text=ALL_TRIES, font=("Bandshift", 38))
        allTriesLabel.place(x=44, y=348)
        try:
            percentageLabel = Label(
                window, bg="#bdd7ee", fg="#002b82", width=4,
                text=f"{round((ALL_WINS / ALL_TRIES) * 100)}%",
                font=("Bandshift", 38)
            )
        except ZeroDivisionError:
            percentageLabel = Label(
                window, bg="#bdd7ee", fg="#002b82",
                width=4, text="0%", font=("Bandshift", 38)
            )
        percentageLabel.place(x=142, y=348)
        currentStreakLabel = Label(window, bg="#bdd7ee", fg="#002b82", width=3, text=CURRENT_STREAK, font=("Bandshift", 38))
        currentStreakLabel.place(x=280, y=348)
        bestStreakLabel = Label(window, bg="#bdd7ee", fg="#002b82", width=3, text=BEST_STREAK, font=("Bandshift", 38))
        bestStreakLabel.place(x=420, y=348)

    if THEME == "LIGHT":
        settingsButton = Button(window, width=50, height=50, image=settings, command=settingsCall, bg="#f0f0f0", activebackground="#f0f0f0")
        statsButton = Button(window, width=50, height=50, image=stats, bg="#f0f0f0", activebackground="#f0f0f0", command=statsCall)
    elif THEME == "DARK":
        settingsButton = Button(window, width=50, height=50, image=settingsLight, command=settingsCall, bg="#222222", activebackground="#222222")
        statsButton = Button(window, width=50, height=50, image=statsLight, bg="#222222", activebackground="#222222", command=statsCall)
    settingsButton.place(x=510, y=10)
    statsButton.place(x=450, y=10)
    
    window.mainloop()
