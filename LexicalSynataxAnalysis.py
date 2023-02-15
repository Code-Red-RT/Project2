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

    # traverse the statement list
    for it in statement_list: 
        if tabCheck == 1: # to check if indentation expected.
            if it.startswith("  "): # checks for indentation
                tabCheck = 0 # resets to unexpected indentation
            else:
                statement_list[i] = "   " + it # changes indentation
                tabCheck = 0 # resets to unexpected indentation
        i += 1

        #Checks for keywords that indicate indentation after the next newline
        if "for " in it or "if " in it or "else " in it or "while " in it or "def " in it:
            tabCheck = 1 # to set expectation for indentation in the next lne

    fixed_code = statement_list

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
