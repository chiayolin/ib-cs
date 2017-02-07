# D1.py - Parentheses Matching Program
#
# Implement and test a Python program that determines if all parentheses 
# in an entered line of code form matching pairs. Note: Pairs of parent-
# heses may be nested.
# 
# date:    01/23/2017
# author:  Chiayo Lin
# license: GPL 3.0

def parenMatch(string):
    
    """ Returns True if all parentheses match else returns False.
    
        The parenMatch() function determines if all parentheses in a string
        match. This includes the following charecter pairs:

            "{"    "}"    "["    "]"    "("    ")"
        
        Pairs of parentheses may be nested.
    """

    def _tokenize(string):
        return [*filter(lambda x: x in "{[()]}", string)]
        
    def _parenMatch(tokens, index = 0):
        if not len(tokens):            return True
        elif index == len(tokens) - 1: return False
        
        return (tokens[index] == '(' and tokens[index + 1] == ')') or  \
               (tokens[index] == '[' and tokens[index + 1] == ']') or  \
               (tokens[index] == '{' and tokens[index + 1] == '}') and \
               _parenMatch(tokens[:index] + tokens[index + 2:]) or  \
               _parenMatch(tokens, index + 1)
        
    return _parenMatch(_tokenize(string))

# Tests
if __name__ == "__main__":
    test_cases = ["", "(]", "((])", "{[()]}", "{}{}()()[]", "{}{",
                  "(define add2 (lambda x (+ x 2)))", "int main() { return 0 }",
                  ")(", ")))[}(((", "{}[[[{{})", "range(1, 2", ")))(("]
    
    for case in test_cases:
        print(format(case, '<30'), end='--> ')

        if parenMatch(case):
            print("All parentheses matched")
        else:
            print("Parentheses unmatched") 
