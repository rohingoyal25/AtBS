def main():
    out = ""
    with open('madlibs_pre.txt') as file:
        for line in file:
            for word in line.split():
                if "NOUN" in word:
                    inp = input("Please enter a NOUN: ")
                    out += " " + inp
                elif "VERB" in word:
                    inp = input("Please enter a VERB: ")
                    out += " " + inp
                elif "ADJECTIVE" in word:
                    inp = input("Please enter an ADJECTIVE: ")
                    out += " " + inp
                else:
                    out += " " + word
            out += "\n"

    with open('madlibs_post.txt', 'w') as file:
        file.write(out)
    print(out)
    
main()