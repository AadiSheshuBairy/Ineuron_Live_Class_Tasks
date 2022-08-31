
s = "this is My First Python programming class and i am learNING python string and its function"
'''1 . Try to extract data from index one to index 300 with a jump of 3
2. Try to reverse a string without using reverse function
3. Try to split a string after conversion of entire string in uppercase
4. try to convert the whole string into lower case
5 . Try to capitalize the whole string
6 . Write a diference between isalnum() and isalpha()
7. Try to give an example of expand tab
8 . Give an example of strip , lstrip and rstrip
9.  Replace a string charecter by another charector by taking your own example
"sudhanshu"
10 . Try  to give a defination of string center function with and exmple
11 . Write your own definition of compiler and interpretor without copy paste form internet in your own language
12 . Python is a interpreted of compiled language give a clear ans with your understanding
13 . Try to write a usecase of python with your understanding .'''


import logging
logging.basicConfig(filename="test_task",level=logging.DEBUG,
                    format='%(asctime)s %(name)s %(levelname)s %(message)s')

class Task_string :
    def __init__(self, s):
        self.s = s


    def extract(self):
        try:
            logging.info("Trying to extract data(s)from index one to 300 with a jump of 3")
            extracted_string=s[1:300:3]
            logging.info("the jumpping of 3 steps : {}".format(extracted_string))
            return extracted_string
        except Exception as e:
            logging.exception(e)


    def reverse(self):
        try:
            logging.info(" Trying to reverse a string without using reverse function")
            reversed_string=s[::-1]
            logging.info("the reversed string of the given data is :{}".format(reversed_string))
            return reversed_string
        except Exception as e:
            logging.exception(e)


    def upper_case(self):
        try:
            logging.info("Trying converting the entire string in uppercase")
            upper_string=s.upper()
            logging.info("After converting a string to upper case:{}".format(upper_string))
            return upper_string
        except Exception as e:
            logging.exception(e)


    def split_string(self):
        try:
            logging.info("Trying to split the data given")
            splited=s.split()
            logging.info("After spliting the string:{}".format(splited))
            return splited
        except Exception as e:
            logging.exception(e)


    def lower_case(self):
        try:
            logging.info("Trying converting the entire string in lower case")
            lower_string=s.lower()
            logging.info("After converting a string to lower case:{}".format(lower_string))
            return lower_string
        except Exception as e:
            logging.exception(e)


    def cap_string(self):
        try:
            logging.info("Trying converting the entire string to capitalize")
            capitalize_string=s.capitalize()
            logging.info("After converting a string to capitailize:{}".format(capitalize_string))
            return capitalize_string
        except Exception as e:
            logging.exception(e)


    def diff_bw_isalnum_isalpha(self):
        try:
            logging.info("the difference b/w isalnum() & isalpha() ")
            value=s.isalnum()
            if value==True:
                logging.info("Yes this data is alpha_numeric")
                logging.info("if the string contains alphabets and numbers then it is alphanumeric "
                             "if it contains only alphabets then it is isalph")
                logging.info("if the output is true then the given data is isalnum:{}".format(value))
            else:
                logging.info("No this is not alpha_numeric")
                logging.info("if the string contains alphabets and numbers then it is alphanumeric "
                             "if it contains only alphabets then it is isalph")
                logging.info("if the output is true then the given data is isalnum:{}".format(value))
                return value
        except Exception as e:
            logging.exception(e)


    def eg_expand_tab(self):
        try:
            logging.info("Example for expand tab")
            tab=  "Iam\tstudent\tat\tineuron "
            eg=tab.expandtabs()
            logging.info("the example of expand tabs is :{}".format(eg))
            return eg
        except Exception as e:
            logging.exception(e)


    def example_strip(self):
        try:
            logging.info("Example for strip")
            val=  "                 Iam student at ineuron                    "
            example=val.lstrip()
            logging.info("the example of lstrip is :{}".format(example))
            example = val.rstrip()
            logging.info("the example of rstrip is :{}".format(example))
            example = val.strip()
            logging.info("the example of strip is :{}".format(example))
            return example
        except Exception as e:
            logging.exception(e)


    def center_defination(self):
        try:
            logging.info("center is the string function in python which we can bring the value to center using our own elements and length")
            center_string=self.s.center(10,"*")
            logging.info("The centred output of the given string is:{}".format(center_string))
            return center_string
        except Exception as e:
            logging.exception(e)


    def Interpreter_Compiler(self):
        try:
            logging.info("Compiler is the program which checks the block of code at a time and gives output/error")
            logging.info("Interpreter is the program which checks the block of code line by line and gives the output/error")
            defination="Compiler and Interpreter"
            logging.info("python is a interpreted of compiled language because in interpreter itself it has compiler which compiles the code to byte code and then to virtual machine code this all process is done in intrepreter itself so the python is a interpreted of compiled language")
            return defination
        except Exception as e:
            logging.exception(e)


output=Task_string(s)
output.upper_case()
output.split_string()
output.lower_case()
output.cap_string()
output.diff_bw_isalnum_isalpha()
output.eg_expand_tab()
output.example_strip()
output.center_defination()
output.Interpreter_Compiler()












