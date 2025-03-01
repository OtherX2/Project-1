meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "Una respuesta ante algo gracioso",
            "ROFL": "una respuesta a una broma"
            }
while True:
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("lo siento! no hemos podido recinocer la palabra, asegurece de haberla escribido bien")
