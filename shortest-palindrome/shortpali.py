def smallerPalindrome(forward, backward):
    """
    :param forward: list forward subslist of a string
    :param backward: list backwards representation of string
    :return:
    """
    x = len(backward)
    if forward[: len(backward)] == backward:
        return forward[::-1] + forward[len(backward) :]
    else:
        return smallerPalindrome(forward, backward[1:])


def shortestPalindrome(source_string):
    """
    : param source_string: str  source for determining the shortest palindrome
    : return: str shortest palindrome.
    """
    return smallerPalindrome(source_string, source_string[::-1])


def test_bubble():
    assert shortestPalindrome("bubble") == "elbbubble"


def test_dasndsadmx():
    assert shortestPalindrome("dasndsadmx") == "xmdasdnsadasndsadmx"

if __name__ == "__main__":
    f = open("input.dat","r")
    out = open("output.out","w")
    
    for line in f:
        out.write(shortestPalindrome(line.strip())+"\n")
