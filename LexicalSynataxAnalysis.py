"""
TEAM AWESOME
02/28/2023

----------------
Team Members:
----------------
Sarah Barnes
Samuel Han
Jessica Gardner
Jada Sachetti
Erika Sadsad
Adriana Miller
----------------
PROJECT 2: LEXICAL AND SYNTAX ANALYSIS

Write a program (language of your choice) that takes in a Python program as an input and does the 
following tasks:
"""

# Have use input the file to test
input_file = input("Enter a python file (path) to test: ")
print("You entered: " + input_file)

with open(input_file) as file:
    print("Reading file...")
    original_file = str(file)
    read = file.readlines()

    # print(read)
    # TODO 1.) Check to make sure all the indentation in the input program is used correctly. If not, fix it. 

    tabCheck = i = 0 # if val is 0 newline not expected. if val 1 it is
    statement_list = read
    number_of_spaces = 0
    stack = [0]
    conditional_words = ["for ", "if ", "while ", "else ", "def ", "elif "]
    

    # traverse the statement list
    for it in statement_list:
        if it == "\n":
            i += 1
            continue
        string_whithout_whitespace = it.lstrip() # ignore tab before to check statement
        number_of_spaces = len(it) - len(string_whithout_whitespace)

        # if there is no indent and needs to be one
        if number_of_spaces < stack[len(stack) - 1]:
            if not tabCheck == 1:
                while number_of_spaces < stack[len(stack) - 1]:
                    stack.pop()
                statement_list[i] = (" " * stack[len(stack) - 1]) + it.lstrip()

        # if there is a missing, expected indent because of a conditional word
        if tabCheck == 1:
            if not number_of_spaces == stack[len(stack) - 1]:
                statement_list[i] = (" " * stack[len(stack) - 1]) + it.lstrip()
            tabCheck = 0    

        # if there is an indent that is unexpected not after conditional word
        elif number_of_spaces > stack[len(stack) - 1]:
            number_of_spaces = stack[len(stack) - 1]
            statement_list[i] = (" " * stack[len(stack) - 1]) + it.lstrip()

        #checks if there is a conditional word
        for word in conditional_words:
            if string_whithout_whitespace.startswith(word):
                stack.append(number_of_spaces + 4)
                tabCheck = 1
                break
        i += 1 #updates counter

    fixed_code = statement_list
    print(statement_list)

    # TODO 2.) Check to make sure all the function headers are syntactically correct. If not, fix it.

    fixed_code = "fixed code will go here"

    # 3.) Count how many time the keyword “print” is used as keywords in the input program.
    str_file = str(read)
    print_count = str_file.count("print(\"")
    print_space_count = str_file.count("print (\"")
    total_print_count = print_count + print_space_count

    print("Total number of 'print' statements: " + str(total_print_count))
    # 4.) Print to a text file the original input program, the updated input program, and the number of time keyword “print” is used.

    updated_file = (
        "# ORIGINAL CODE:\n" + original_file + 
        "\n\n# FIXED CODE: \n" + fixed_code + 
        "\n\n# Total number of 'print' statements: " + str(total_print_count))
    
    """ This segment of code saves a .txt copy of the input file """
    name = str(input_file)
    txt_file = name[:-3]
    print(txt_file)
    txt_file = txt_file + '.txt'

    with open(txt_file, "w") as file:
        file.write(updated_file)

    file.close
