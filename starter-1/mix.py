import sys

file_in = 'mixin.txt'
file_out = 'mixout.txt'

def solve(n, d):
    a = n / d
    b = n % d
    return a, b

def main(argv):
    with open(file_in) as fp:
        lines = map(str.split, fp.readlines())
        n, d = map(int, lines[0])
        a, b = solve(n, d)
        with open(file_out, 'w') as fp_out:
            if b:
                fp_out.write('%d %d/%d\n' % (a, b, d))
            else:
                fp_out.write('%d\n' % a)

if __name__ == '__main__':
    main(sys.argv)
