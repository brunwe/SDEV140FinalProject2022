import tkinter as tk
from tkinter import *


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.initUI()
        self.pack()

        # all the variables I am using for dimensions are here so everything lines up
        self.height = 460  # the height of the main window
        self.width = 765  # width of main window
        self.gemx = 38  # x position of top-left most image
        self.gemy = 30  # y position of top-left most image
        self.recwid = 700  # this, recy1 and recy0 help me line up the lines drawn on the canvas
        self.recy1 = 54  # ^
        self.recy0 = 5  # ^
        self.textx = 120  # helps me line up static text
        self.texty = 29  # ^

        self.topaz_value = 0  # stores the number inputted for topaz
        self.amethyst_value = 0  # stores the number inputted for amethyst
        self.aquamarine_value = 0  # stores the number inputted for aquamarine
        self.jade_value = 0  # stores the number inputted for jade
        self.emerald_value = 0  # stores the number inputted for emerald
        self.ruby_value = 0  # stores the number inputted for ruby
        self.diamond_value = 0  # stores the number inputted for diamond
        self.prism_value = 0  # stores the number inputted for prismatic shard

        self.grand_total = 0  # stores the grand total

        self.gemologist = False  # the variable toggled upon selecting or de-selecting the checkbox

        # this retrieves the images from the project folder
        self.topaz = PhotoImage(file='Topaz.png')
        self.amethyst = PhotoImage(file='Amethyst.png')
        self.aquamarine = PhotoImage(file='Aquamarine.png')
        self.jade = PhotoImage(file='Jade.png')
        self.emerald = PhotoImage(file='Emerald.png')
        self.ruby = PhotoImage(file='Ruby.png')
        self.diamond = PhotoImage(file='Diamond.png')
        self.prism = PhotoImage(file='Prismatic_Shard.png')
        self.currency = PhotoImage(file='SDGold.png')
        self.chicken = PhotoImage(file='White_Chicken.png')

        # instances the main canvas that everything is built upon
        self.canvas = tk.Canvas(self, height=self.height, width=self.width, bg="Light Gray")

        # the resource amount is printed on the canvas here, these values are modified by the buttons
        self.t_text = self.canvas.create_text(self.textx + 250, self.texty + 2, text=self.topaz_value,
                                              font=('Courier New', 22))
        self.am_text = self.canvas.create_text(self.textx + 250, self.texty + 50, text=self.amethyst_value,
                                               font=('Courier New', 22))
        self.aq_text = self.canvas.create_text(self.textx + 250, self.texty + 100, text=self.aquamarine_value,
                                               font=('Courier New', 22))
        self.j_text = self.canvas.create_text(self.textx + 250, self.texty + 150, text=self.jade_value,
                                              font=('Courier New', 22))
        self.e_text = self.canvas.create_text(self.textx + 250, self.texty + 200, text=self.emerald_value,
                                              font=('Courier New', 22))
        self.r_text = self.canvas.create_text(self.textx + 250, self.texty + 250, text=self.ruby_value,
                                              font=('Courier New', 22))
        self.d_text = self.canvas.create_text(self.textx + 250, self.texty + 300, text=self.diamond_value,
                                              font=('Courier New', 22))
        self.p_text = self.canvas.create_text(self.textx + 250, self.texty + 350, text=self.prism_value,
                                              font=('Courier New', 22))
        self.grand_total_text = self.canvas.create_text(self.textx + 445, self.texty + 403, text=self.grand_total,
                                                        font=('Courier New', 22))

        # this instances the about and quit buttons
        self.quit_button = tk.Button(self, text="Exit Program", fg="Light Gray", bg="FireBrick", command=self.quit)
        self.quit_button.pack()
        self.about_button = tk.Button(self, text="About", bg="SkyBlue", command=about_window)
        self.about_button.pack()

        # Here is where the plus buttons for each resource are instanced
        self.t_plus_button = tk.Button(self, height=1, width=2, text="+", font=['Courier New', 17], command=self.plus_T)
        self.t_plus_button.pack()
        self.am_plus_button = tk.Button(self, height=1, width=2, text="+", font=['Courier New', 17],
                                        command=self.plus_AM)
        self.am_plus_button.pack()
        self.aq_plus_button = tk.Button(self, height=1, width=2, text="+", font=['Courier New', 17],
                                        command=self.plus_AQ)
        self.aq_plus_button.pack()
        self.j_plus_button = tk.Button(self, height=1, width=2, text="+", font=['Courier New', 17], command=self.plus_J)
        self.j_plus_button.pack()
        self.e_plus_button = tk.Button(self, height=1, width=2, text="+", font=['Courier New', 17], command=self.plus_E)
        self.e_plus_button.pack()
        self.r_plus_button = tk.Button(self, height=1, width=2, text="+", font=['Courier New', 17], command=self.plus_R)
        self.r_plus_button.pack()
        self.d_plus_button = tk.Button(self, height=1, width=2, text="+", font=['Courier New', 17], command=self.plus_D)
        self.d_plus_button.pack()
        self.p_plus_button = tk.Button(self, height=1, width=2, text="+", font=['Courier New', 17], command=self.plus_P)
        self.p_plus_button.pack()
        # minus
        self.t_minus_button = tk.Button(self, height=1, width=2, text="-", font=['Courier New', 17],
                                        command=self.minus_T)
        self.t_minus_button.pack()
        self.am_minus_button = tk.Button(self, height=1, width=2, text="-", font=['Courier New', 17],
                                         command=self.minus_AM)
        self.am_minus_button.pack()
        self.aq_minus_button = tk.Button(self, height=1, width=2, text="-", font=['Courier New', 17],
                                         command=self.minus_AQ)
        self.aq_minus_button.pack()
        self.j_minus_button = tk.Button(self, height=1, width=2, text="-", font=['Courier New', 17],
                                        command=self.minus_J)
        self.j_minus_button.pack()
        self.e_minus_button = tk.Button(self, height=1, width=2, text="-", font=['Courier New', 17],
                                        command=self.minus_E)
        self.e_minus_button.pack()
        self.r_minus_button = tk.Button(self, height=1, width=2, text="-", font=['Courier New', 17],
                                        command=self.minus_R)
        self.r_minus_button.pack()
        self.d_minus_button = tk.Button(self, height=1, width=2, text="-", font=['Courier New', 17],
                                        command=self.minus_D)
        self.d_minus_button.pack()
        self.p_minus_button = tk.Button(self, height=1, width=2, text="-", font=['Courier New', 17],
                                        command=self.minus_P)
        self.p_minus_button.pack()
        # equals
        self.equals_button = tk.Button(self, height=1, width=9, text="=", font=['Courier New', 17],
                                       command=self.calculate_total)
        self.equals_button.pack()

        # These place the about and quit buttons on the main canvas
        self.canvas.create_window(self.width - 55, 10, anchor=NW, window=self.about_button)
        self.canvas.create_window(10, self.height - 42, anchor=NW, window=self.quit_button)

        # The images of each gem (and the gold coin by the total + the chicken) are printed here
        self.canvas.create_image(self.gemx, self.gemy - 3, image=self.topaz)
        self.canvas.create_image(self.gemx, self.gemy + 48, image=self.amethyst)
        self.canvas.create_image(self.gemx, self.gemy + 101, image=self.aquamarine)
        self.canvas.create_image(self.gemx, self.gemy + 148, image=self.jade)
        self.canvas.create_image(self.gemx, self.gemy + 198, image=self.emerald)
        self.canvas.create_image(self.gemx, self.gemy + 249, image=self.ruby)
        self.canvas.create_image(self.gemx, self.gemy + 298, image=self.diamond)
        self.canvas.create_image(self.gemx, self.gemy + 349, image=self.prism)
        self.canvas.create_image(self.gemx + 430, self.gemy + 402, image=self.currency)
        self.canvas.create_image(self.gemx + 694, self.gemy + 402, image=self.chicken)

        # Here, the boxes are drawn that grid out the entire GUI
        self.canvas.create_rectangle(5, self.recy0, self.recwid, self.recy1, width=2)
        self.canvas.create_rectangle(5, self.recy0 + 49, self.recwid, self.recy1 + 51, width=2)
        self.canvas.create_rectangle(5, self.recy0 + 49, self.recwid, self.recy1 + 100, width=2)
        self.canvas.create_rectangle(5, self.recy0 + 49, self.recwid, self.recy1 + 150, width=2)
        self.canvas.create_rectangle(5, self.recy0 + 49, self.recwid, self.recy1 + 200, width=2)
        self.canvas.create_rectangle(5, self.recy0 + 49, self.recwid, self.recy1 + 250, width=2)
        self.canvas.create_rectangle(5, self.recy0 + 49, self.recwid, self.recy1 + 300, width=2)
        self.canvas.create_rectangle(5, self.recy0 + 49, self.recwid, self.recy1 + 350, width=2)
        self.canvas.create_rectangle(300, self.recy0, self.recwid, self.height - 1, width=2)
        self.canvas.create_rectangle(441, self.recy0, self.recwid, self.height - 1, width=2)
        self.canvas.create_rectangle(5, 5, self.width - 1, self.height - 1, width=2)

        # This is where the static text is printed on the canvas.
        self.canvas.create_text(self.textx, self.texty, text="Topaz", font=('Courier New', 22))
        self.canvas.create_text(self.textx + 27, self.texty + 50, text="Amethyst", font=('Courier New', 22))
        self.canvas.create_text(self.textx + 43, self.texty + 100, text="Aquamarine", font=('Courier New', 22))
        self.canvas.create_text(self.textx - 10, self.texty + 150, text="Jade", font=('Courier New', 22))
        self.canvas.create_text(self.textx + 16, self.texty + 200, text="Emerald", font=('Courier New', 22))
        self.canvas.create_text(self.textx - 8, self.texty + 250, text="Ruby", font=('Courier New', 22))
        self.canvas.create_text(self.textx + 16, self.texty + 300, text="Diamond", font=('Courier New', 22))
        self.canvas.create_text(self.textx + 60, self.texty + 350, text="Prism. Shard", font=('Courier New', 22))
        self.canvas.create_text(self.textx + 390, self.texty, text="* 80 G", font=('Courier New', 22))
        self.canvas.create_text(self.textx + 398, self.texty + 50, text="* 100 G", font=('Courier New', 22))
        self.canvas.create_text(self.textx + 398, self.texty + 100, text="* 180 G", font=('Courier New', 22))
        self.canvas.create_text(self.textx + 398, self.texty + 150, text="* 200 G", font=('Courier New', 22))
        self.canvas.create_text(self.textx + 398, self.texty + 200, text="* 250 G", font=('Courier New', 22))
        self.canvas.create_text(self.textx + 398, self.texty + 250, text="* 250 G", font=('Courier New', 22))
        self.canvas.create_text(self.textx + 398, self.texty + 300, text="* 750 G", font=('Courier New', 22))
        self.canvas.create_text(self.textx + 407, self.texty + 350, text="* 2000 G", font=('Courier New', 22))

        # these place all the plus and minus (and equals) buttons on the canvas
        self.canvas.create_window(420, 30, window=self.t_plus_button)
        self.canvas.create_window(420, 80, window=self.am_plus_button)
        self.canvas.create_window(420, 130, window=self.aq_plus_button)
        self.canvas.create_window(420, 180, window=self.j_plus_button)
        self.canvas.create_window(420, 230, window=self.e_plus_button)
        self.canvas.create_window(420, 280, window=self.r_plus_button)
        self.canvas.create_window(420, 330, window=self.d_plus_button)
        self.canvas.create_window(420, 380, window=self.p_plus_button)
        self.canvas.create_window(322, 30, window=self.t_minus_button)
        self.canvas.create_window(322, 80, window=self.am_minus_button)
        self.canvas.create_window(322, 130, window=self.aq_minus_button)
        self.canvas.create_window(322, 180, window=self.j_minus_button)
        self.canvas.create_window(322, 230, window=self.e_minus_button)
        self.canvas.create_window(322, 280, window=self.r_minus_button)
        self.canvas.create_window(322, 330, window=self.d_minus_button)
        self.canvas.create_window(322, 380, window=self.p_minus_button)
        self.canvas.create_window(371, 432, window=self.equals_button)

        # this is the gemologist checkbox
        self.gcheck = tk.Checkbutton(self, text='Gemologist Skill (1.3x)', bg="Light Gray",
                                     activebackground="Light Gray", command=self.gemo_check)
        self.gcheck.pack()
        self.canvas.create_window(215, 431, window=self.gcheck)

        self.canvas.pack()

    # this allows me to modify the attributes of the master window that is made when the Class instances
    def initUI(self):
        self.master.title("Stardew Valley Ore Value Calculator")
        self.master.iconbitmap('Iridium_Ore.ico')
        self.master.resizable(False, False)

    # everything from this point on is a brute-force way to make the buttons do something
    def plus_T(self):
        self.topaz_value += 1
        self.canvas.itemconfig(self.t_text, text=self.topaz_value)

    def plus_AM(self):
        self.amethyst_value += 1
        self.canvas.itemconfig(self.am_text, text=self.amethyst_value)

    def plus_AQ(self):
        self.aquamarine_value += 1
        self.canvas.itemconfig(self.aq_text, text=self.aquamarine_value)

    def plus_J(self):
        self.jade_value += 1
        self.canvas.itemconfig(self.j_text, text=self.jade_value)

    def plus_E(self):
        self.emerald_value += 1
        self.canvas.itemconfig(self.e_text, text=self.emerald_value)

    def plus_R(self):
        self.ruby_value += 1
        self.canvas.itemconfig(self.r_text, text=self.ruby_value)

    def plus_D(self):
        self.diamond_value += 1
        self.canvas.itemconfig(self.d_text, text=self.diamond_value)

    def plus_P(self):
        self.prism_value += 1
        self.canvas.itemconfig(self.p_text, text=self.prism_value)

    def minus_T(self):
        if self.topaz_value >= 1:
            self.topaz_value -= 1
            self.canvas.itemconfig(self.t_text, text=self.topaz_value)
        else:
            return

    def minus_AM(self):
        if self.amethyst_value >= 1:
            self.amethyst_value -= 1
            self.canvas.itemconfig(self.am_text, text=self.amethyst_value)
        else:
            return

    def minus_AQ(self):
        if self.aquamarine_value >= 1:
            self.aquamarine_value -= 1
            self.canvas.itemconfig(self.aq_text, text=self.aquamarine_value)
        else:
            return

    def minus_J(self):
        if self.jade_value >= 1:
            self.jade_value -= 1
            self.canvas.itemconfig(self.j_text, text=self.jade_value)
        else:
            return

    def minus_E(self):
        if self.emerald_value >= 1:
            self.emerald_value -= 1
            self.canvas.itemconfig(self.e_text, text=self.emerald_value)
        else:
            return

    def minus_R(self):
        if self.ruby_value >= 1:
            self.ruby_value -= 1
            self.canvas.itemconfig(self.r_text, text=self.ruby_value)
        else:
            return

    def minus_D(self):
        if self.diamond_value >= 1:
            self.diamond_value -= 1
            self.canvas.itemconfig(self.d_text, text=self.diamond_value)
        else:
            return

    def minus_P(self):
        if self.prism_value >= 1:
            self.prism_value -= 1
            self.canvas.itemconfig(self.p_text, text=self.prism_value)
        else:
            return

    # this switches the boolean value of the gemologist variable based on the checkbox status
    def gemo_check(self):
        if not self.gemologist:
            self.gemologist = True
        else:
            self.gemologist = False

    # this calculates the grand total
    def calculate_total(self):
        if not self.gemologist:
            self.grand_total = (self.topaz_value * 80) + (self.amethyst_value * 100) + (self.aquamarine_value * 180) + (self.jade_value * 200) + (self.emerald_value * 250) + (self.ruby_value * 250) + (self.diamond_value * 750) + (self.prism_value * 2000)
            self.canvas.itemconfig(self.grand_total_text, text=self.grand_total)
            return
        else:
            self.grand_total = (self.topaz_value * 80) + (self.amethyst_value * 100) + (self.aquamarine_value * 180) + (self.jade_value * 200) + (self.emerald_value * 250) + (self.ruby_value * 250) + (self.diamond_value * 750) + (self.prism_value * 2000)
            self.grand_total = int((self.grand_total * 1.3))
            self.canvas.itemconfig(self.grand_total_text, text=self.grand_total)
            return


# this is the setup for my about window that is opened upon button press
def about_window():
    txt: str = "This is my final project for my SDEV140 class at Ivy Tech. I wanted to make an ore calculator \n" \
               "for the video game Stardew Valley since there aren't any that show the value of items in game \n" \
               "until you sell at the end of each day. I would like to eventually finish the project entirely, \n" \
               "covering other parts of the game and possibly even export as an application for free download. \n" \
               "It's pretty airtight, but if you find any problems please dm me on twitter @brunnerwe. Thanks." \
               "\n \nCreated by Will Brunner 5/6/22 @ 3:52 AM (lol)"
    window = tk.Tk()
    window.title("About")
    window.iconbitmap('Iridium_Ore.ico')
    window.resizable(False, False)
    main_canvas = tk.Canvas(window, width=600, height=150, bg="Light Gray")
    quit_button = tk.Button(window, text="Return", fg="Light Gray", bg="FireBrick", command=window.destroy, anchor=S)
    main_canvas.create_window(550, 122, anchor=NW, window=quit_button)
    main_canvas.create_text(300, 75, text=txt)

    main_canvas.pack()


root = tk.Tk()
myapp = App(root)
myapp.mainloop()

# That's all folks
