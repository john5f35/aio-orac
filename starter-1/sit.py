import sys

file_in = 'sitin.txt'
file_out = 'sitout.txt'

def solve(r, s, n):
    return min(r * s, n), max(n - r * s, 0)

def main(argv):
    with open(file_in) as fp:
        r, s, n = map(int, fp.read().split())
        res = solve(r, s, n)
        with open(file_out, 'w') as fp_out:
            fp_out.write("%d %d\n" % res)

if __name__ == '__main__':
    main(sys.argv)
