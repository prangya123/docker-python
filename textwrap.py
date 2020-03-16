#################################################################################################
# require python3
# -----------    ----------------  -------------------------------------
#  Date           Author            Comment
# -----------    ----------------  -------------------------------------
#  Mar-15-2019  Prangya Parmita Kar  Initial Version,
#
#  python3 hel2p\ -h
#  python3 textwrap.py
#  Sample input:
#  Paragraph = This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works.
#  Page Width = 20
#################################################################################################

import sys
import getopt

def string_justify(input_string,max_width):
    for s in input_string.split("\n"):
        if s == "":
            print("")
        else:
            list1 = []
            list2 = []
            count = 0
            for w in s.split():
                if len(w) > max_width:
                    print("Word size/length is bigger than the Page Width: Page Width:",max_width, "Word Size:", len(w))
                    print("Please increase the Page Width appropriately")
                    print("Exiting out...")
                    print("")
                    exit(1)

                if count + len(w) <= max_width:
                    list1.append(w)
                    count += len(w) + 1
                else:
                    list2.append(list1)
                    list1 = [w]
                    count = len(w) + 1

            list2.append(list1)
            #print(list2)

            # process list2:
            array = 1
            for i in list2:
                if len(i) == 1:
                    gap = len(i) #num of words/elemnets
                else:
                    gap = len(i) - 1 #num of words/elemnets - 1
                num_of_char = len(''.join(i))

                free_space = max_width - num_of_char #minus the width ftom total char
                filler = int(free_space / gap)
                rem = free_space % gap

                if len(i) == 1:
                    var1 = i[0].ljust(max_width,' ')
                else:
                    var1 = ((filler * ' ').join(i))
                if rem > 0:
                    if rem == 1:
                        rem = rem + 1  # 2
                    var1 = var1.replace(' ', rem * ' ', 1)
                print("Array [", array, "] \"", var1, "\"", sep="")
                # print(var1)
                array += 1


def main(argv):
    try:
        opts,args = getopt.getopt(argv,"h",["help="])

    except getopt.GetoptError as exc:
        print(exc.msg)
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit(0)
    try:
        input_string=input("Paragraph = ")
        max_width=int(input("Page_Width = "))
        # input_string="""This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works."""
        #max_width=20
        string_justify(input_string,max_width)
    except:
        print("error")
    finally:
        print("")
        #print("THANK YOU!")


def usage():
    print("""
    can     accept     a
    paragraph string and
    page     width    as
    parameters       and
    return   an array of
    left    AND    right
    justified    strings.
     """)

if __name__ == "__main__":
    main(sys.argv[1:])




