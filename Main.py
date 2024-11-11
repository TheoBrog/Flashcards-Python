import json

def clearConsole():
    print(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")

flashcards = "nil"##"flashcards.json"

newFlashcards = []
reviewFlashcards = []

def new():
    with open(flashcards, "r+") as file:
        data = json.load(file)
        for i in newFlashcards:
            for v in data:
                if v["id"] == i:
                    print(v["question"])
                    input("")
                    print("A resposta é " + v["answer"])
                    p = int(input("1 - Acertou \n2 - Errou \n"))
                    if p == 2:
                        reviewFlashcards.append(v["id"])
                    clearConsole()
        newFlashcards.clear()
        print("Sem novos cartões.")

def review():
    with open(flashcards, "r+") as file:
        data = json.load(file)
        for i in reviewFlashcards:
            for v in data:
                if v["id"] == i:
                    print(v["question"])
                    input("")
                    print("A resposta é " + v["answer"])
                    p = int(input("1 - Acertou \n2 - Errou \n"))
                    if p == 2:
                        reviewFlashcards.append(v["id"])
                    clearConsole()
        reviewFlashcards.clear()
        print("Sem novas revisões.")
    
def reset():
    with open(flashcards, "r+") as file:
        data = json.load(file)
        newFlashcards.clear()
        for i in data:
            newFlashcards.append(i["id"])
            print("Adicionado flashcard id: " + str(i["id"]))
        print("Pronto \n")

def select():
    global flashcards
    print("Escreva o nome do arquivo")
    print("(Ele deve estar na mesma pasta que Flashcards.py)")
    a = input("")
    flashcards = a
    clearConsole()
    print(f"{flashcards} selecionado!")

clearConsole()
while True:
    print("1 - Estudar cartões")
    print("2 - Rever cartões")
    print("3 - Carregar cartões")
    print("4 - Selecionar pacote de recursos")
    print("5 - Sair")
    i = input("Destino: ")
    if i == "1":
        clearConsole()
        if len(newFlashcards) > 0:
            new()
        else:
            print("Sem novos cartões.")
    elif i == "2":
        clearConsole()
        if len(reviewFlashcards) > 0:
            review()
        else:
            print("Sem cartões para rever.")
    elif i == "3":
        clearConsole()
        #print("af: " + flashcards)
        if flashcards == "nil":
            print("Sem pacote de recursos.")
        else:
            reset()
    elif i == "4":
        clearConsole()
        select()
    elif i == "5":
        clearConsole()
        exit()
    else:
        clearConsole()