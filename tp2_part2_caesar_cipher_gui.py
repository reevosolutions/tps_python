import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog


def chiffrer_texte(texte, decalage):
    chiffre = ''
    for char in texte:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            char_code = ord(char)
            char_code = shift + (char_code - shift + decalage) % 26
            chiffre += chr(char_code)
        else:
            chiffre += char
    return chiffre

def dechiffrer_texte(texte, decalage):
    return chiffrer_texte(texte, -decalage)

def charger_fichier():
    chemin = filedialog.askopenfilename()
    with open(chemin, 'r', encoding='utf-8') as f:
        contenu = f.read()
    return contenu

def sauvegarder_fichier(contenu):
    chemin = filedialog.asksaveasfilename(defaultextension='.txt')
    with open(chemin, 'w', encoding='utf-8') as f:
        f.write(contenu)

def appliquer_chiffrement():
    decalage = simpledialog.askinteger('Décalage', 'Entrez le décalage pour le chiffrement:')
    contenu = charger_fichier()
    contenu_chiffre = chiffrer_texte(contenu, decalage)
    sauvegarder_fichier(contenu_chiffre)
    messagebox.showinfo('Succès', 'Le fichier a été chiffré et sauvegardé avec succès.')

def appliquer_dechiffrement():
    decalage = simpledialog.askinteger('Décalage', 'Entrez le décalage pour le déchiffrement:')
    contenu = charger_fichier()
    contenu_dechiffre = dechiffrer_texte(contenu, decalage)
    sauvegarder_fichier(contenu_dechiffre)
    messagebox.showinfo('Succès', 'Le fichier a été déchiffré et sauvegardé avec succès.')

app = tk.Tk()
app.title('Chiffrement de César')

btn_chiffrer = tk.Button(app, text='Chiffrer un fichier', command=appliquer_chiffrement)
btn_chiffrer.pack(pady=20)

btn_dechiffrer = tk.Button(app, text='Déchiffrer un fichier', command=appliquer_dechiffrement)
btn_dechiffrer.pack(pady=20)

app.mainloop()
