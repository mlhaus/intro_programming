from user_input import get_float

def main():
    get_float("Give me a number")
    get_float("What is your age?", 0)
    get_float("What is your grade level?", 1, 12)
    
if __name__ == "__main__":
    main()