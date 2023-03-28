from Stack import Stack

def delims(instring:str) -> bool:
    open: str = '([{'
    closed: str = ')]}'

    match: bool = True
    stack: Stack[str] = Stack[str]()
    
    for c in instring:
        if c in open:
            stack.push(c)
        elif c in closed:
            if stack.empty():
                match = False
            elif closed.index(c) != open.index(stack.pop()):
                if not stack.empty():
                    match = False
    return match

def isPalindrome(instring: str) -> bool:
    match: bool = True
    stack: Stack[str] = Stack[str]()

    instring = instring.lower()

    for c in instring:
        if c.isalpha():
            stack.push(c)
    
    for c in instring:
        if c.isalpha():
            c2 = stack.pop()
            if c != c2:
                match = False
            else:
                match = True
    return match

def main(args: list[str]) -> int:
    # Palindromes
    assert isPalindrome('')
    assert isPalindrome('I')
    assert isPalindrome('eye')
    assert isPalindrome('Hannah')
    assert isPalindrome('ABBA')
    assert isPalindrome("Madam, I'm Adam.")
    assert isPalindrome('A man, a plan, a canal: Panama!')
    assert isPalindrome('Alastair')
    assert isPalindrome('Garfield')
    assert isPalindrome('Park')

    print('Tests completed successfully')

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)
