def average(array):

    k1=set(array)
    m=format((sum(k1)/len(k1)),'.3f')
    return m

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
