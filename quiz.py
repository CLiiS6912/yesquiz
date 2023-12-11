questions = [{"question":"Hovedstaden i England?",
               "Options":["Oslo","Bagdad","London","Dallas"],
               "correct":"London"},

               {"question":"Hovedstaden i Norge?",
               "Options":["Oslo","Bagdad","London","Dallas"],
               "correct":"Oslo"},

]

def quiztime():
    score = 0

    print("Hei og velkommen til Quiztime")

    for q, Dict in enumerate(questions):
        print("Question ",q+1, ": ",Dict["question"])

        for opt in range(len(Dict["Options"])):
            print("Option",opt+1,": ",Dict["Options"][opt])
            
        user_answer = input("Skriv inn et tall mellom 1 og 4: ")

        if user_answer.isdigit() and 1<= int(user_answer) <=4:
            if Dict["correct"] == Dict["Options"][int(user_answer)-1]:
                print("Riktig! Vi går videre")
                score += 1
            else:
                print("Det var desverre feil... vi går videre")
        else:
            print("Du tastet noe ugyldig. Går videre til neste spørsmål")

    print("Din score ble: ", score, "/",len(questions))

quiztime()