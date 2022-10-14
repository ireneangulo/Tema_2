texto= ("un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro")
frases= texto.split(sep= "#") #Separa cada vez que hay un #
for f, frase in enumerate(frases):
    frases[f]= frase.capitalize()