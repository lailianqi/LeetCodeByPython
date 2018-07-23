
def get_next(pattern):
    '''
    KMP算法的next数组的求法
    '''
    next = []
    m, k, j = len(pattern), -1, 0
    next[0] = -1
    while j < m-1:
        if k == -1 or pattern[j] == pattern[k]:
            k += 1
            j += 1
            next[j] = k
        else:
            k = next[k]
