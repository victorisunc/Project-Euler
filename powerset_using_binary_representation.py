# power set generator using binary representation

def powerset(s):
    def bin_rep(bin_len):
        return ['{number:0{width}b}'.format(width=len(s), number=i) for i in range(bin_len)]
    return [[s[idx] for idx, r in enumerate(rep) if int(r)] for rep in bin_rep(2**len(s))]

if __name__ == '__main__':
    print powerset((1, 2, 3))

