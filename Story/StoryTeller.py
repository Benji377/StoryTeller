import random
import webbrowser
from tkinter import *


# Colorsection for Textcolors
black = lambda text: '\033[0;30m' + text + '\033[0m'
red = lambda text: '\033[0;31m' + text + '\033[0m'
green = lambda text: '\033[0;32m' + text + '\033[0m'
yellow = lambda text: '\033[0;33m' + text + '\033[0m'
blue = lambda text: '\033[0;34m' + text + '\033[0m'
magenta = lambda text: '\033[0;35m' + text + '\033[0m'
cyan = lambda text: '\033[0;36m' + text + '\033[0m'
white = lambda text: '\033[0;37m' + text + '\033[0m'


root = Tk()
root.title("Menu")
root.geometry("900x800+0+0")
root.resizable(0, 0)
var = StringVar()


# Welcome!
def vorstellung():
    var.set("Willkommen auf Benji's Geschichtenerzähler!\n")


# Stops everything
def anhalter():
    var.set("Programm wird angehalten")
    sys.exit("Programm angehalten")


# Stories from txt files
def story1():
    s1 = open("Story1.txt", "r")
    if s1.mode == "r":
        var.set("Deine Geschichte ist in kürze bereit\n")
        print("Programm funktioniert")
        p = s1.readlines()
        for x in p:
            var.set(x)
    else:
        var.set("Leider gab es ein Fehler, wir konnten keine Geschichte finden")
        print("Fehler Story1")


def story2():
    s2 = open("Story2.txt", "r")
    if s2.mode == "r":
        var.set("Deine Geschichte ist in kürze bereit")
        print("Programm funktioniert")
        p = s2.readlines()
        for x in p:
            var.set(x)
    else:
        var.set("Leider gab es ein Fehler, wir konnten keine Geschichte finden")
        print("Fehler in Story2")


def story3():
    s3 = open("Story3.txt", "r")
    if s3.mode == "r":
        var.set("Deine Geschichte ist in kürze bereit")
        print("Programm funktioniert")
        p = s3.readlines()
        for x in p:
            var.set(x)
    else:
        var.set("Leider gab es ein Fehler, wir konnten keine Geschichte finden")
        print("Fehler in Story3")


def story4():
    s3 = open("Story4.txt", "r")
    if s3.mode == "r":
        var.set("Deine Geschichte ist in kürze bereit")
        print("Programm funktioniert")
        p = s3.readlines()
        for x in p:
            var.set(x)
    else:
        var.set("Leider gab es ein Fehler, wir konnten keine Geschichte finden")
        print("Fehler in story4")


def story5():
    s3 = open("Story5.txt", "r")
    if s3.mode == "r":
        var.set("Deine Geschichte ist in kürze bereit")
        print("Programm funktioniert")
        p = s3.readlines()
        for x in p:
            var.set(x)
    else:
        var.set("Leider gab es ein Fehler, wir konnten keine Geschichte finden")
        print("Fehler in Story5")


def story6():
    s3 = open("Story6.txt", "r")
    if s3.mode == "r":
        var.set("Deine Geschichte ist in kürze bereit")
        print("Programm funktioniert")
        p = s3.readlines()
        for x in p:
            var.set(x)
    else:
        var.set("Leider gab es ein Fehler, wir konnten keine Geschichte finden")
        print("Fehler in Story6")


def story7():
    s3 = open("Story7.txt", "r")
    if s3.mode == "r":
        var.set("Deine Geschichte ist in kürze bereit")
        print("Programm funktioniert")
        p = s3.readlines()
        for x in p:
            var.set(x)
    else:
        var.set("Leider gab es ein Fehler, wir konnten keine Geschichte finden")
        print("Fehler in Story7")


def story8():
    s3 = open("Story8.txt", "r")
    if s3.mode == "r":
        var.set("Deine Geschichte ist in kürze bereit")
        print("Programm funktioniert")
        p = s3.readlines()
        for x in p:
            var.set(x)
    else:
        var.set("Leider gab es ein Fehler, wir konnten keine Geschichte finden")
        print("Fehler in Story8")


def story9():
    s3 = open("Story9.txt", "r")
    if s3.mode == "r":
        var.set("Deine Geschichte ist in kürze bereit")
        print("Programm funktioniert")
        p = s3.readlines()
        for x in p:
            var.set(x)
    else:
        var.set("Leider gab es ein Fehler, wir konnten keine Geschichte finden")
        print("Fehler in Story9")


def story10():
    s3 = open("Story10.txt", "r")
    if s3.mode == "r":
        var.set("Deine Geschichte ist in kürze bereit")
        print("Programm funktioniert")
        p = s3.readlines()
        for x in p:
            var.set(x)
    else:
        yield("Leider gab es ein Fehler, wir konnten keine Geschichte finden")
        var.set("Fehler in Story10")


# randomly picks a story from 1 to 10
def generator():
    print("Zufallsgenerator läuft")
    stories = ["s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10"]
    z = random.choice(stories)
    if z == "s1":
        story1()
    elif z == "s2":
        story2()
    elif z == "s3":
        story3()
    elif z == "s4":
        story4()
    elif z == "s5":
        story5()
    elif z == "s6":
        story6()
    elif z == "s7":
        story7()
    elif z == "s8":
        story8()
    elif z == "s9":
        story9()
    elif z == "s10":
        story10()
    else:
        var.set("Fehler im Code")
        print("Fehler beim Zufallsgenerator")


# Links to external sites
def musik():
    print("Playlist ist an")
    var.set("Du wirst jetzt auf Benji's persönliche Musikplaylist weitergeleitet")
    webbrowser.open('https://www.youtube.com/playlist?list=PLIdk2M44Rqh-a46zFXar6ExeNtW7QXAQp')


def redd():
    print("Email")
    var.set("Du wirst jetzt zur Email weitergeleitet")
    webbrowser.open('https://www.reddit.com/u/Benben377')


def insta():
    print("Instagram")
    var.set("Du wirst jetzt auf Benji's Instagramseite weitergeleitet")
    webbrowser.open('https://www.instagram.com/benben377/')


def face():
    print("Discord")
    var.set("Du wirst jetzt auf Discord weitergeleitet")
    webbrowser.open('https://www.facebook.com/Benben377')


# Full GUI with Tkinter
heading = Label(root, text="Geschichtenerzähler", font=("arial", 40, "bold"), fg="steelblue").pack()

# All labels(Text)
label1 = Label(root, text="Willkommen auf den Geschichtenerzähler programmiert von Benji!\n"
                          " Klicke auf eine Geschichte um sie dir anzuhören \noder klicke auf"
                          " \"Zufall\" um eine zufällige Geschichte anzuhören", font=("arial", 10, "bold"),
               fg="red").place(x=220, y=80)
label2 = Label(root, text="Liste aller Geschichten:").place(x=10, y=140)
label3 = Label(root, text="Zufallsgenerator").place(x=390, y=160)
label4 = Label(root, text="Achtung! Stoppt alles!").place(x=390, y=240)
label5 = Label(root, text="Musikalische Unterhaltung").place(x=390, y=320)
label6 = Label(root, text="Hier kannst du mich kontaktieren").place(x=650, y=140)

# Geschichten
stopper = Button(root, text="Stop", width=10, height=2, bg="red", command=anhalter).place(x=400, y=260)
gesch1 = Button(root, text="Apotropäisch", width=10, height=2, bg="green", command=story1).place(x=20, y=160)
gesch2 = Button(root, text="Schwarz", width=10, height=2, bg="green", command=story2).place(x=20, y=210)
gesch3 = Button(root, text="Geld...", width=10, height=2, bg="green", command=story3).place(x=20, y=260)
gesch4 = Button(root, text="Neunzigern", width=10, height=2, bg="green", command=story4).place(x=20, y=310)
gesch5 = Button(root, text="Mein Tag", width=10, height=2, bg="green", command=story5).place(x=20, y=360)
gesch6 = Button(root, text="Stille", width=10, height=2, bg="green", command=story6).place(x=110, y=160)
gesch7 = Button(root, text="Bürostuhlfront", width=10, height=2, bg="green", command=story7).place(x=110, y=210)
gesch8 = Button(root, text="Triumph", width=10, height=2, bg="green", command=story8).place(x=110, y=260)
gesch9 = Button(root, text="Schutzengel", width=10, height=2, bg="green", command=story9).place(x=110, y=310)
gesch10 = Button(root, text="Ratten", width=10, height=2, bg="green", command=story10).place(x=110, y=360)

# Text
title = Label(root, text="Geschichte", font=("arial", 10, "bold")).place(x=50, y=530)
text = Text(root, bg="skyblue", relief=RAISED, width=100, height=15)
text.place(x=50, y=550)

# Anderes
zufall = Button(root, text="Zufall", width=10, height=2, bg="cyan", command=generator).place(x=400, y=180)
music = Button(root, text="Musik", width=10, height=2, bg="gold", command=musik).place(x=400, y=340)

# Social
reddit = Button(root, text="Reddit", width=10, height=2, bg="white", command=redd).place(x=700, y=170)
instagram = Button(root, text="Instagram", width=10, height=2, bg="white", command=insta).place(x=700, y=220)
facebook = Button(root, text="Facebook", width=10, height=2, bg="white", command=face).place(x=700, y=270)

vorstellung()
root.mainloop()