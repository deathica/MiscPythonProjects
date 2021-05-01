# Programmer: Deathica
# Date: 4/23/2021
# Program: Variable Caesar Cypher/Decypher
# This version comes with the lowercase and uppercase alphabet characters, including space, placed by default within the decypher "charset" box.

from string import ascii_lowercase as lc, ascii_uppercase as uc
default_txt = lc + uc + " "
import tkinter.scrolledtext as tkscrolled
import tkinter as tk
# Creates a global variable to be used in Cypher and the read-only entry box for the output
# Defines the function used to process a string through a shift cypher using the provided charset.
def Split(word):
    return [char for char in word]
def ClearBox():
    decypher_output.delete(1.0, tk.END)
def Cypher():
    encrypt = str("")
    # Captures what's in the entry boxes into variables
    word = word_entry.get()
    shift = int(shift_entry.get())
    charset = charset_entry.get()
    charset_index = Split(charset)
    # Creates a variable to set an index value limit based on the length of the given shift
    shiftmax = len(charset_index)
    for character in word:
        msgPos = charset_index.index(character)
        shiftPos = msgPos + shift
        
        if shiftPos > shiftmax:
            shiftPos -= shiftmax
        encrypt = encrypt + charset_index[shiftPos]
    print(encrypt)
    # Clears the text box cypher_output and then replaces it with the contents of the encrypt string
    cypher_output.delete(1.0, tk.END)
    cypher_output.insert(1.0, encrypt)
# Defines the function used to pass each variable over to the Decypher function and contains the for loop that will run through each possible shift value
def CaptureDecypher():
    # Retrieves the values within the entryboxes and captures them into variables
    dword = str(dword_entry.get())
    dcharset = dcharset_entry.get()
    dcharset_index = Split(dcharset)
    dshiftmax = len(dcharset_index)
    # The for loop runs for each character within the charset
    for c in range(dshiftmax):
        # Inserts text into the empty text box, showing what is being decyphered and the shift value being tested for keeping track.
        decypher_output.insert(1.0, "Message attempting to be decyphered: " + dword + "\nShift value being tested: " + str(c) + "\n")
        Decypher(dword, dcharset, dcharset_index, dshiftmax, c)
# Defines the function that processes the dword string through the cypher
def Decypher(dword, dcharset, dcharset_index, dshiftmax, shift):
    # Creates an empty string to put the output of the decrypt attempt into
    decrypt = str("")
    # For each character in the dword string, it gets the index position based on the charset index, and replaces it with the character that is as many places ahead as is equal to the shift.
    for character in dword:
        msgPos = dcharset_index.index(character)
        shiftPos = msgPos + shift
        # Assures there is never an index out of range function by preventing it from getting higher than the index
        if shiftPos > (dshiftmax-1):
            shiftPos -= dshiftmax
        decrypt = decrypt + dcharset_index[shiftPos]
    decypher_output.insert(1.0, decrypt + "\n")
    # Provides some basic debugging output. Was useful for trying to figure out problem variables during testing
    print("Shift value is: " + str(shift))
    print("The index value of the current character is: " + str(msgPos))
    print("The position of the shifted value within the index is: " + str(shiftPos))
    print("-" * 30)
        

window = tk.Tk()
window.title("Caesar Cypher")
window.maxsize(800, 800)
default_bg = "purple"

# Creates the master frame with a size of 800x800
frame1 = tk.Frame(master = window, height = 800, width = 800, bg = default_bg)
frame1.grid_propagate(False)
frame1.pack()

# Creates the label for the Cipher section's header
title = tk.Label(master = frame1, text = "Caesar Cypher", font = ("impact", "20", "bold"), bg = default_bg)
title.place(relx=.5, y = 20, anchor="center")
# Creates a label to show what the first entry box is for
word_label = tk.Label(master = frame1, text = "Text to be Cyphered:", font = ("impact", "14", "bold"), bg = default_bg)
word_label.place(relx=.2, y = 48)
# Creates the first entry box to set the word for cyphering
word_entry = tk.Entry(master = frame1, width = 50)
word_entry.place(relx = .5, y = 50)
# Creates a label to show what the second entry box is for
charset_label = tk.Label(master = frame1, text = "Cypher charset:", font = ("impact", "14", "bold"), bg = default_bg)
charset_label.place(relx = .2, y = 98)
# Creates the second entry box used to set the charset
charset_entry = tk.Entry(master = frame1, width = 50)
charset_entry.place(relx = .5, y = 100)
# Creates a label to show what the third entry box is for
shift_label = tk.Label(master = frame1, text = "Cypher shift:", font = ("impact", "14", "bold"), bg = default_bg)
shift_label.place(relx = .2, y = 148)
# Creates the third entry box used to set the shift
shift_entry = tk.Entry(master =frame1, width = 50)
shift_entry.place(relx = .5, y = 150)
# Creates the button used to call the Cypher function that will do the cyphering using the variables within the first three entry boxes.
cypher_button = tk.Button(master = frame1, text = "Cypher!", font=("impact", "14", "bold"), width = 30, height= 1, bg = "black", fg = "blue", activebackground = "grey", command = Cypher)
cypher_button.place(relx = .5, y = 200, anchor = "center")
# Creates a label to show what the fourth entry box is for
cypher_result = tk.Label(master = frame1, text ="Cypher Result:", font=("impact", "14", "bold"), bg = default_bg)
cypher_result.place(relx = .2, y = 248)
# Creates a text box that is set to be cleared and replaced with the encryption output every time Cypher is called
cypher_output = tk.Text(master = frame1, width = 38, height = 1)
cypher_output.place(relx = .5, y = 250)
# Creates the label for the title of the second half of the window, the Decypher section.
title2 = tk.Label(master = frame1, text = "Caesar Decypherer", font = ("impact", "20", "bold"), bg = default_bg)
title2.place(relx = .5, y = 300, anchor="center")
# Creates and places the label that shows what the 5th box is for
dword_label = tk.Label(master = frame1, text = "Text to be Decyphered:", font = ("impact", "14", "bold"), bg = default_bg)
dword_label.place(relx = .2, y = 348)
# Creates and places the entry box for the cyphered text
dword_entry = tk.Entry(master = frame1, width = 50)
dword_entry.place(relx = .5, y = 350)
# Creates and places the label that shows what the 6th box is for
dcharset_label = tk.Label(master = frame1, text = "Decypher charset:", font = ("impact", "14", "bold"), bg = default_bg)
dcharset_label.place(relx = .2, y = 398)
# Creates the entry box for the charset that is used to attempt decyphering
dcharset_entry = tk.Entry(master = frame1, width = 50)
dcharset_entry.place(relx = .5, y = 400)
# Inserts the default text into the dcharset_entry box.
dcharset_entry.insert(0, default_txt)
# Creates and places the label marking what will appear within the textbox
decypher_output_txt = tk.Label(master = frame1, text = "Decypher Output", font = ("impact", "20", "bold"), bg = default_bg)
decypher_output_txt.place(relx = .5, y = 450, anchor = "center")
# Creates a large, scrollable text box that will be filled with decypher attempts.
decypher_output = tkscrolled.ScrolledText(master = frame1, height = 10, width = 78)
decypher_output.place(relx = .1, y = 500)
# Creates and places a button labelled "Decypher" that calls the Decypher command.
decypher_button = tk.Button(master = frame1, text = "Decypher!", font = ("impact", "14", "bold"), width = 30, height = 1, bg = "black", fg = "blue", activebackground = "grey", command = CaptureDecypher)
decypher_button.place(relx = .5, y = 700, anchor = "center")
# Creates and places a button labelled "Clear" that calls the Clear command to clear the text within the Decypher Output text box
clear_button = tk.Button(master = frame1, text = "Clear", font = ("impact", "14", "bold"), width = 30, height = 1, bg = "black", fg = "blue", activebackground = "grey", command = ClearBox)
clear_button.place(relx = .5, y = 750, anchor = "center")
window.mainloop()