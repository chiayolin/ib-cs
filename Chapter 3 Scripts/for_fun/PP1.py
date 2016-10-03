char1 = input("First character: ")
char2 = input("Second character: ")
char_line = int(input("Characters per line: "))
rep = int(input("Repetitions: "))

counter = 0
while rep != counter:
    char_counter = 0
    while char_counter != char_line:
        print(char1, end = '')
        char_counter += 1
    print()
    char_counter = 0
    while char_counter != char_line:
        print(char2, end = '')
        char_counter += 1
    print()
    counter += 1
