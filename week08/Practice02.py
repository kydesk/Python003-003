def add_num(x):
    x += 2
    return x

def custom_map(function, iterable):
    answers =[]
    for i in iterable:
        answer = function(i)
        answers.append(answer)
    return answers.__iter__()

result1 = custom_map(add_num, [1,2,3,4,5])
result2 = custom_map(add_num, (3,5,8,9,0))

print(list(result1))
print(list(result2))