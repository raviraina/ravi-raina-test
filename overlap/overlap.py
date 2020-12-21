"""
Question A
Your goal for this question is to write a program that accepts two lines
(x1,x2) and (x3,x4)on the x-axis and returns whether they overlap.
As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).
"""

# function to determine whether two points overlap
def overlap(p1, p2):
    if len(p1) != 2 or len(p2) != 2:
        raise ValueError('Must be tuples of length 2')

    p1 = fix_order(p1)
    p2 = fix_order(p2)

    if p1[0] < p2[1] and p1[1] >= p2[0]:
        return True

    return False

# function to fix the order s.t x[0] < x[1]
def fix_order(p):
    if p[0] > p[1]:
        q = p
        p = (q[1], q[0])

    return p

# quick test with main
def main():
    p1 = (1, 2)
    p2 = (2, 4)
    print(overlap(p1, p2))


if __name__ == "__main__":
    main()
