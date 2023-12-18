def longestCommonPrefix(self, strs: List[str]) -> str:
    # Edge Case #3, empty list
    if strs == []:
        return ""
    
    # Edge Case #2, list only has 1 item
    if len(strs) == 1:
        return strs[0]
    
    strs.sort()
    shortest_string = strs[0]
    prefix = ""

    # Main check
    for x in range(len(shortest_string)):
        return TODO

    return 1 # string


def main():
    strings = ["bla", "blaaa", "bleee"] # Should return "bl"
    check = longestCommonPrefix(strings) 
    return 1


if __name__ == "__main__":
    main()