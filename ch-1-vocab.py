## Practice Activity -- Chapter 1 Vocabulary
    Due: Friday, Jan 10 in class
## NOTE: This activity will be performed IN LAB on the scheduled day; a worksheet will be handed out at the beginning of lab.

## Write a short answer for each of the following:

# What is a software? List at least 3 categories/kinds of software.
    Software is a program, or an organized set of instructions for a computer that solves a task.
        web applications
        databases
        artificial intelligence 

# What is a hardware? List at least 3 categories/kinds of hardware.
    Hardware is physical equipment that runs or supports the running of software.

# What is the difference between a low-level programming language and a high-level programming language? What kind of language is Python?
    A low-level programming language is one which operates directly on the hardware.
        e.g., C++, COBAL, Fortran
    A high-level programming language is one which needs to be compiled to run on a low-level language.
        e.g., C#, JavaScript, Java
# What is a key word? Define the term in your own words and give at least one example.
    A keyword is word that is used by a programming language for things like functions and syntax

# What is an operator? Define the term in your own words and give at least one example.
    An operator is highly trained soldier in an elite military service.
    But in programming, an operator is special character that performs mathematical operations.
        e.g., +, -, *, /, %, <, >, etc.

# Define the word syntax.
    Syntax means the exact way and exact keywords to use in order for a program to be executed by a computer. Although syntax differs from language to language, many languages share many aspects of syntax.

# What does the word statement mean in computer programming?
    A statement is an instruction to the computer.

# What is a bit? What is a byte?
    A bit is a one or a zero that is used to open or close circuts on a computer chip.
    A byte is a series of 8 bits.

# Convert the following numbers from base 2 to base 10. Show your work:

    To convert base 2 number into a base 10 number we have a couple of basic rules
        
        Every digit's place value, starting at the right where the place value is 0 and increase by 1 for each digit as we move to the left.

        We take the digit and multiply it by the product we get from multiplying the base we are converting to (which is 10) to the power of the place value.

        Then we sum all the products from the operation above, and this is the answer

    10110 base 2

        Working backwards from the right:
            0 has an exponent of 0      0 * (2^0) = 0 * 1  = 0
            1 has an exponent of 1      1 * (2^1) = 1 * 2  = 2
            1 has an exponent of 2      1 * (2^2) = 1 * 4  = 4
            0 has an exponent of 3      0 * (2^3) = 0 * 8  = 0
            1 has an exponent of 4      1 * (2^4) = 1 * 16 = 16
                                                       ---------
                                                       sum = 22          
        So 10110 base 2 is converted to 22 base 10

    100011 base 2

        Working backwards from the right:
            1 has an exponent of 0      1 * (2^0) = 1 * 1  = 1
            1 has an exponent of 1      1 * (2^1) = 1 * 2  = 2
            0 has an exponent of 2      0 * (2^2) = 0 * 4  = 0
            0 has an exponent of 3      0 * (2^3) = 0 * 8  = 0
            0 has an exponent of 4      0 * (2^4) = 0 * 16 = 0
            1 has an exponent of 5      1 * (2^5) = 1 * 32 = 32
                                                       ---------
                                                       sum = 35          
        So 100011 base 2 is converted to 35 base 10

# Convert the following numbers from base 10 to base 2. Show your work:

    To convert a number from base 10 to base 2 we follow a few simple rules:

        We divide the number we want to convert into base 2 by 2, and save the remainder
        Next we divide the quotient by 2, and append the remainder to the last remainder
        We continue this process of dividing the quotient by 2 until we finally get a quotient of 0, and we append this final remainder to the list of remainders
        The answer is the series of remainders read backwards

    44 base 10	
        First divide the number to convert by 2,                    44 / 2 = 22     Remainder is 0
        Next divide the quotient by 2,                              22 / 2 = 11     Remainder is 0
        Again divide the quotient by 2,                             11 / 2 = 5      Remainder is 1
        Again divide the quotient by 2,                             5 / 2 = 2       Remainder is 1
        Again divide the quotient by 2,                             2 / 2 = 1       Remainder is 0
        Again divide quotient by 2, but quotient is 0 so we stop    1 / 2 = 0       Remainder is 1
                                                                                    series of remainders is 001101
        So 44 base 10 converted to base 2, is the series of remainders in reversed order: 101100
    
    21 base 10	
        First divide the number to convert by 2,                    21 / 2 = 10     Remainder is 1
        Next divide the quotient by 2,                              10 / 2 = 5      Remainder is 0
        Again divide the quotient by 2,                             5 / 2 = 2       Remainder is 1
        Again divide the quotient by 2,                             2 / 2 = 1       Remainder is 0
        Again divide quotient by 2, but quotient is 0 so we stop    1 / 2 = 0       Remainder is 1
                                                                                    series of remainders is 10101
        So 21 base 10 converted to base 2, is the series of remainders in reversed order: 10101

# State in your own words the class policy on copying code from another student? (You can find this information on the course syllabus; be sure to read the whole syllabus carefully.)
    Don't burn yourself, just don't do it... it's not allowed!
# What section number are you in?  (Be sure to always show this number in the comment block you write at the beginning of each program.)
    Section 03
# What is the scheduled date and time for the final exam for your section?  (You can find this information at the bottom of the General Course Information section on the class home page; plan to take the final exam at the scheduled time.)
    March 23, 2020 @1:30pm

## NOTE: Most lab deadlines are set at 11pm on the day of the lab meeting.  When electronic submission is required, this is the actual deadline.  When the submission is on paper (as it is for this lab), the worksheet must be turned in no later than the very beginning of the next class meeting.  So, for this lab, be sure to turn in your completed worksheet at the end of lab, or at the very latest at the beginning or our next class meeting.  A complete solution will be posted after that.