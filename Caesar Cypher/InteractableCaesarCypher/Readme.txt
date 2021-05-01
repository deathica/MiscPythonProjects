Note: The UI design is horrid. This is known and intentional.
Prerequisites
-------------
Python 3

Installation
-------------
Simply extract the files to the desired destination and run. The GUI will provide entry boxes for data entry and relevant labels as descriptors ascertaining to the purpose of the entry boxes.
***MAKE SURE TO OPEN THE SCRIPT WITH PYTHON 3, NOT 2!!***

Usage
-------------
This simple program allows you to encrypt or decrypt something using a simple Shift Cypher, referred to as the Caesar Cypher for fun.
Each version will have a default entry into the charset box. Use the version without any extra characters at the end to start with a completely empty version.
If you're intending to cypher something, start by entering what text you want to be cyphered in the top entry box. Then, insert the charset in the exact order you intend to encrypt using.
Note: You MUST include every character that comes with the original text inside the charset, otherwise the program will NOT work as intended. This includes space!
Once you've inserted your text to be cyphered, and the charset, insert the shift number you wish to shift each character by, then press the Cypher! button to receive your cyphered text!
Each time you click Cypher, it will clear out the text box, so make sure to extract what information you need from it.
If your intention is to attempt to decypher something, enter the cyphered text into the first entry box under the "Caeser Decypherer" header, then provide the charset to attempt the decyphering with.
There is no guarentee there will be a legible output, as it all depends on your knowledge of the charset used for the original cypher, however it WILL print out EVERY attempted output, the shift value,
and the original cyphered text. This might help you with discerning patterns, or provide more gibberish, depending. However, there's no limit to how many charsets you can test, so if you're willing, 
go ahead and keep trying. The "clear" button will clear all the text in the Decypher Output text box.