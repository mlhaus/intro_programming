import csv, random

def process_csv(path, fields):
    delim = get_delimiter(path)
    data = []
    with open(path) as file:
        reader = csv.DictReader(file, delimiter=delim) # DictReader function return each line as a dictionary
        #reader = csv.reader(file, delimiter=delim) # the reader function returns each line as a list
        for row in reader:
            record = [] # I want this to only include the Name and Description
            for field in fields:
                record.append(row[field])
            data.append(record)
    return data

def get_delimiter(path):
    file_extension = path[path.rfind('.') + 1:]
    return "," if file_extension == "csv" else "\t"

def get_data():
    file_name = "the_office.csv"
    needed_fields = ["Name", "Description"] # Name is the actor's name, Description is the character name
    return process_csv(file_name, needed_fields)

def play_game(data):
    score = 0 # correct answers
    total = len(data) # total questions
    while(len(data) > 0):
        rand_character = random.choice(data)
        data.remove(rand_character)
        score += ask_question(rand_character) # will return 0 or 1, 1 if they answer correctly
    print(f"Game over. You scored {score} out of {total}")

def ask_question(character):
    prompt = f"What character did {character[0]} play? "
    guess = input(prompt).strip()
    if(guess.lower() == character[1].lower()):
        print("That's correct!")
        return 1
    else:
        print(f"Incorrect. It was {character[1]}")
        return 0

if __name__ == "__main__":
    data = get_data()
    play_game(data)