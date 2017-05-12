import sys

file_in = 'bendin.txt'
file_out = 'bendout.txt'

def area(r):
    return abs(r[0] - r[2]) * abs(r[1] - r[3])

def overlap_1dim(a, b):
    l_a = a[1] - a[0]
    l_b = b[1] - b[0]
    tot = max(a + b) - min(a + b)
    ovl = tot - (l_a + l_b)
    return abs(ovl) if ovl < 0 else 0

def overlap(A, B):
    ovl_x = overlap_1dim((A[0], A[2]), (B[0], B[2]))
    ovl_y = overlap_1dim((A[1], A[3]), (B[1], B[3]))
    return ovl_x * ovl_y

def solve(A, B):
    return area(A) + area(B) - overlap(A, B)

def main(argv):
    with open(file_in) as fp:
        lines = map(str.split, fp.readlines())
        rec1 = map(int, lines[0])
        rec2 = map(int, lines[1])
        res = solve(rec1, rec2)
        with open(file_out, 'w') as fp_out:
            fp_out.write("%d\n" % res)

if __name__ == '__main__':
    main(sys.argv)
