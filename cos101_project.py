import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Example dictionary data
translations = {}

spanish_dictionary = {
    "hola": "hello",
    "adiós": "goodbye",
    "gracias": "thank you",
    "por favor": "please",
    "perdón": "sorry",
    "sí": "yes",
    "no": "no",
    "amigo": "friend",
    "familia": "family",
    "comida": "food",
    "agua": "water",
    "casa": "house",
    "escuela": "school",
    "trabajo": "work",
    "feliz": "happy",
    "triste": "sad",
    "rápido": "fast",
    "lento": "slow",
    "grande": "big",
    "pequeño": "small"
}
french_dictionary = {
    "bonjour": "hello",
    "au revoir": "goodbye",
    "merci": "thank you",
    "s'il vous plaît": "please",
    "pardon": "sorry",
    "oui": "yes",
    "non": "no",
    "ami": "friend",
    "famille": "family",
    "nourriture": "food",
    "eau": "water",
    "maison": "house",
    "école": "school",
    "travail": "work",
    "heureux": "happy",
    "triste": "sad",
    "rapide": "fast",
    "lent": "slow",
    "grand": "big",
    "petit": "small"
}
German_dictionary = {
    "hallo": "hello",
    "auf wiedersehen": "goodbye",
    "danke": "thank you",
    "bitte": "please/you're welcome",
    "entschuldigung": "sorry",
    "ja": "yes",
    "nein": "no",
    "freund": "friend",
    "familie": "family",
    "essen": "food",
    "wasser": "water",
    "haus": "house",
    "schule": "school",
    "arbeit": "work",
    "glücklich": "happy",
    "traurig": "sad",
    "schnell": "fast",
    "langsam": "slow",
    "groß": "big",
    "klein": "small"
}
italian_dictionary = {
    "ciao": "hello",
    "arrivederci": "goodbye",
    "grazie": "thank you",
    "per favore": "please",
    "scusa": "sorry",
    "sì": "yes",
    "no": "no",
    "amico": "friend",
    "famiglia": "family",
    "cibo": "food",
    "acqua": "water",
    "casa": "house",
    "scuola": "school",
    "lavoro": "work",
    "felice": "happy",
    "triste": "sad",
    "veloce": "fast",
    "lento": "slow",
    "grande": "big",
    "piccolo": "small"
}
hausa_dictionary = {
    "sannu": "hello",
    "sai anjima": "goodbye",
    "na gode": "thank you",
    "don Allah": "please",
    "yi hakuri": "sorry",
    "eh": "yes",
    "a'a": "no",
    "aboki": "friend",
    "iyali": "family",
    "abinci": "food",
    "ruwa": "water",
    "gida": "house",
    "makaranta": "school",
    "aiki": "work",
    "farin ciki": "happy",
    "baƙin ciki": "sad",
    "da sauri": "fast",
    "a hankali": "slow",
    "babba": "big",
    "ƙarami": "small"
}

# Populate the translations dictionary
for word, meaning in spanish_dictionary.items():
    if meaning not in translations:
        translations[meaning] = {}
    translations[meaning]["Spanish"] = word

for word, meaning in french_dictionary.items():
    if meaning not in translations:
        translations[meaning] = {}
    translations[meaning]["French"] = word

for word, meaning in German_dictionary.items():
    if meaning not in translations:
        translations[meaning] = {}
    translations[meaning]["German"] = word

for word, meaning in italian_dictionary.items():
    if meaning not in translations:
        translations[meaning] = {}
    translations[meaning]["Italian"] = word

for word, meaning in hausa_dictionary.items():
    if meaning not in translations:
        translations[meaning] = {}
    translations[meaning]["Hausa"] = word


def translate_word():
    """Translate the word into the selected language."""
    word = word_entry.get().strip().lower()
    selected_language = language_combobox.get()

    if word == "":
        messagebox.showerror("Error", "Please enter a word to translate.")
        return

    if word not in translations:
        messagebox.showerror("Error", f"The word '{word}' is not in the dictionary.")
        return

    if selected_language not in translations[word]:
        messagebox.showerror(
            "Error",
            f"The word '{word}' does not have a translation in {selected_language}.",
        )
        return

    translated_word = translations[word][selected_language]
    result_label.config(
        text=f"The translation of '{word}' in {selected_language} is: {translated_word}"
    )


# Root window
root = tk.Tk()
root.title("Multi-Language Dictionary")
root.geometry("400x300")

# Heading
heading_label = tk.Label(root, text="Multi-Language Dictionary", font=("Arial", 16))
heading_label.pack(pady=10)

# Input for word
word_label = tk.Label(root, text="Enter Word:")
word_label.pack()
word_entry = tk.Entry(root, width=30)
word_entry.pack()

# Language selection
language_label = tk.Label(root, text="Select Language:")
language_label.pack()
language_combobox = ttk.Combobox(
    root, values=["French", "Spanish", "German", "Italian", "Hausa"], state="readonly"
)
language_combobox.set("French")
language_combobox.pack()

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate_word)
translate_button.pack(pady=10)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

# Run the main loop
root.mainloop()
