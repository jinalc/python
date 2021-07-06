# Write a script called diff.py that take two file names as arguments and checks if the content of
# both the files is same and prints true or false.
import filecmp


def diff(f1, f2):
    # shallow comparison
    result = filecmp.cmp(f1, f2)
    print(result)

    # deep comparison
    result = filecmp.cmp(f1, f2, shallow=False)
    print(result)


def diff2(fi1, fi2):
    f1 = open(fi1, "r")
    f2 = open(fi2, "r")
    i = 0
    for line1 in f1:
        i += 1
        for line2 in f2:
            # matching line1 from both files
            if line1 == line2:
                # print IDENTICAL if similar
                print("Line ", i, ": IDENTICAL")
            else:
                print("Line ", i, ":")
                # else print that line from both files
                print("\tFile 1:", line1, end='')
                print("\tFile 2:", line2, end='')
            break
    # closing files
    f1.close()
    f2.close()


diff("a.txt", "b.txt")
diff2("a.txt", "b.txt")
