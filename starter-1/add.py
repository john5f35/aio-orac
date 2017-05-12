import sys

def solve(a, b):
    return a + b

def main(argv):
    with open('addin.txt') as fp:
        line = fp.read().strip()
        a, b = map(int, line.split(' '))
        res = solve(a, b)
        with open('addout.txt', 'w') as fp_out:
            fp_out.write(str(res))
            fp_out.write('\n')

if __name__ == '__main__':
    main(sys.argv)
