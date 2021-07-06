# 6. Create a class SelfManaged such that it keeps track of the number of objects currently alive.
# Create a class method get_current_count(), that gives the number of objects currently alive in
# memory.

class SelfManaged:
    count = 0

    def __init__(self):
        SelfManaged.count += 1

    def __del__(self):
        SelfManaged.count -= 1


s1 = SelfManaged()
s2 = SelfManaged()
s3 = SelfManaged()

print(SelfManaged.count)

del s1

print(SelfManaged.count)
