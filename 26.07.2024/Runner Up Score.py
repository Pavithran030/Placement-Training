if __name__ == '__main__':
    n = int(input())  
    scores = map(int,input().split())  
    scores_list = list(set(scores))  
    sorted_scores = sorted(scores_list, reverse=True)
    print(sorted_scores[1])
