import functools
def mutate_string(string, position, character):
    k=list(string)
    k[position]=character
    m=functools.reduce(lambda x,y:x+y,k)
    return m
