from tkinter import *

window = Tk()
window.title("SupercoolBotPickerino")
window.configure(bg="black" )
bg = PhotoImage(file='bg.png')
brt = PhotoImage(file="stpbtn.gif")
starta = PhotoImage(file="btn.gif")
#bg= Label(window, image=photo).place(x=0, y=0)

window.wm_maxsize(width=500, height=500,)



def clack():
    window.destroy()
    exit()

def click():
    import cv2 as cv
    import numpy as np
    import pyautogui
    import time
    import keyboard


    nadel = cv.imread('Sachen/op1.png', cv.IMREAD_UNCHANGED)
    Heu = cv.imread('Sachen/Opn.png', cv.IMREAD_UNCHANGED)
    Eisen = cv.imread('Sachen/Eisen.png', cv.IMREAD_UNCHANGED)
    Rose = cv.imread('Sachen/Rose.png', cv.IMREAD_UNCHANGED)

    while True:
        screeny = pyautogui.screenshot()
        screeny = np.array(screeny)
        screeny = cv.cvtColor(screeny, cv.COLOR_RGB2BGR)
        res = cv.matchTemplate(screeny, nadel, cv.TM_CCOEFF_NORMED)
        # cv.waitKey()
        # trash = 0.8
        # loc = np.where(res >= trash)
        maxmin = cv.minMaxLoc(res)
        # print(cv.minMaxLoc(res))
        # stronk = np.where(res>=trash)
        # stronk = list(zip(*stronk[::-1]))

        maxymil = maxmin

        # print(maxy)
        maxmax = maxymil[3]

        for i in maxmin:

            trashy = maxmin[1]

            if 0.9 <= trashy <= 1.05 and maxmax[1] <= 600:
                # print('Yeas')
                maxy = maxmin

                # print(maxy)
                max = maxy[3]
                # print(max)
                # print(max[0])
                # print(max[1])

                if max[1] <= 600:
                    keyboard.press('Shift')
                    time.sleep(0.00001)

                    pyautogui.mouseDown(button='right', x=max[0], y=max[1])
                    time.sleep(0.000001)
                    pyautogui.mouseUp(button='right')
                    time.sleep(0.0000001)
                    keyboard.release('Shift')

        resy = cv.matchTemplate(screeny, Eisen, cv.TM_CCOEFF_NORMED)
        cv.waitKey()
        # trash = 0.8
        # loc = np.where(resy >= trash)
        maxminy = cv.minMaxLoc(resy)
        # print(cv.minMaxLoc(res))
        # stronk = np.where(res>=trash)
        # stronk = list(zip(*stronk[::-1]))
        maxmaxy = maxminy

        for i in maxminy:

            trashy2 = maxminy[1]

            if 0.9 < trashy2 <= 1.05 and maxmaxy[1] <= 500:
                # print('Yeas')
                maxy = maxminy

                # print(maxy)
                max = maxy[3]
                # print(max)
                # print(max[0])
                # print(max[1])

                if max[1] <= 600:
                    keyboard.press('Shift')
                    time.sleep(0.00001)
                    pyautogui.mouseDown(button='right', x=max[0], y=max[1])
                    time.sleep(0.000001)
                    pyautogui.mouseUp(button='right')
                    time.sleep(0.0000001)
                    keyboard.release('Shift')

        resys = cv.matchTemplate(screeny, Rose, cv.TM_CCOEFF_NORMED)
        # cv.waitKey()
        # trash = 0.8
        # oc = np.where(resys >= trash)
        maxminys = cv.minMaxLoc(resys)
        # print(cv.minMaxLoc(res))
        # stronk = np.where(res>=trash)
        # stronk = list(zip(*stronk[::-1]))
        maxmaxys = maxminys

        for i in maxminys:

            trashy2 = maxminys[1]

            if 0.9 < trashy2 <= 1.05 and maxmaxy[1] <= 500:
                # print('Yeas')
                maxy = maxminys

                # print(maxy)
                max = maxy[3]
                # print(max)
                # print(max[0])
                # print(max[1])

                if max[1] <= 600:
                    keyboard.press('Shift')
                    time.sleep(0.00001)
                    pyautogui.mouseDown(button='right', x=max[0], y=max[1])
                    time.sleep(0.000001)
                    pyautogui.mouseUp(button='right')
                    time.sleep(0.0000001)
                    keyboard.release('Shift')

        if (keyboard.is_pressed('n')):
            break




canvas1 = Canvas(window, width=500,
                 height=500)

canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=bg,
                     anchor="nw")

# Add Text
#canvas1.create_text(200, 250, text="Welcome")

# Create Buttons

Startbtn = Button(window, image=starta,command=click, borderwidth=0)
button2 = Button(window, image=brt,  command=clack,borderwidth=0)
label1 = Label(window,text="Hold n pressed ingame to interrupt pickerino", fg="White", bg="black")


# Display Buttons


#button2_canvas = canvas1.create_window(100, 40,
                                       #anchor="nw",
                                       #window=button2)

button3_canvas = canvas1.create_window(100, 30, anchor="nw",
                                       window=Startbtn)




button2_canvas = canvas1.create_window(300, 30, anchor="nw",
                                       window=button2)

window.mainloop()

