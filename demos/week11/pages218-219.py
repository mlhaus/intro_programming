import csv

def process_csv(path):
    delim = get_delimiter(path)
    with open(path) as file:
        reader = csv.DictReader(file, delimiter=delim) # DictReader function return each line as a dictionary
        #reader = csv.reader(file, delimiter=delim) # the reader function returns each line as a list
        for row in reader:
            print(row)

def get_delimiter(path):
    file_extension = path[path.rfind('.') + 1:]
    return "," if file_extension == "csv" else "\t"

if __name__ == "__main__":
    file_name = "movies.csv"
    process_csv(file_name)