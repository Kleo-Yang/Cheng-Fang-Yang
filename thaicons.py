import tkinter as tk
from tkinter import ttk

# List of all Thai consonants and their names
thai_consonants = [
    ("ก", "Gor Gai"), ("ข", "Khor Khai"), ("ฃ", "Khor Khuat"), ("ค", "Khor Khwai"),
    ("ฅ", "Khor Khon"), ("ฆ", "Khor Rakhang"), ("ง", "Ngor Ngu"), ("จ", "Jor Jan"),
    ("ฉ", "Chor Ching"), ("ช", "Chor Chang"), ("ซ", "Sor So"), ("ฌ", "Chor Choe"),
    ("ญ", "Yor Ying"), ("ฎ", "Dor Chada"), ("ฏ", "Tor Patak"), ("ฐ", "Thor Thaan"),
    ("ฑ", "Thor Montho"), ("ฒ", "Nor Nenh"), ("ณ", "Dor Dek"), ("ด", "Tor Tao"),
    ("ต", "Thor Thung"), ("ถ", "Thor Thahan"), ("ท", "Thor Thong"), ("ธ", "Nor Nuu"),
    ("น", "Bor Baimai"), ("บ", "Por Pla"), ("ป", "Phor Phung"), ("ผ", "For Fah"),
    ("ฝ", "Phor Phan"), ("พ", "For Samphao"), ("ฟ", "Mor Ma"), ("ภ", "Yor Yak"),
    ("ม", "Ror Ruea"), ("ย", "Lor Ling"), ("ร", "Wor Waen"), ("ฤ", "Sor Sala"),
    ("ล", "Sor Rusi"), ("ฦ", "Sor Suea"), ("ว", "Hor Hip"), ("ศ", "Lor Chula"),
    ("ษ", "Or Ang"), ("ส", "Hor Nokhuk")
]

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        self.root.geometry("300x200")
        
        self.index = 0
        self.showing_name = False
        
        self.card_frame = ttk.Frame(root, padding=20)
        self.card_frame.pack(expand=True)
        
        self.label = ttk.Label(self.card_frame, text=thai_consonants[self.index][0], font=("Arial", 50))
        self.label.pack()
        
        self.flip_button = ttk.Button(self.card_frame, text="Flip", command=self.flip_card)
        self.flip_button.pack()
        
        self.nav_frame = ttk.Frame(root)
        self.nav_frame.pack()
        
        self.prev_button = ttk.Button(self.nav_frame, text="<", command=self.prev_card)
        self.prev_button.pack(side=tk.LEFT, padx=10)
        
        self.next_button = ttk.Button(self.nav_frame, text=">", command=self.next_card)
        self.next_button.pack(side=tk.RIGHT, padx=10)
    
    def flip_card(self):
        if self.showing_name:
            self.label.config(text=thai_consonants[self.index][0])
        else:
            self.label.config(text=thai_consonants[self.index][1])
        self.showing_name = not self.showing_name
    
    def next_card(self):
        self.index = (self.index + 1) % len(thai_consonants)
        self.showing_name = False
        self.label.config(text=thai_consonants[self.index][0])
    
    def prev_card(self):
        self.index = (self.index - 1) % len(thai_consonants)
        self.showing_name = False
        self.label.config(text=thai_consonants[self.index][0])

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()

