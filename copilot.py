if __name__ == '__main__':
    student = [] 
    min = 0
    _2min = -1
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if(min < score):
            _2min = min
            min = score
        student.append([name,score])

    if(_2min == float('inf')):
        _2min = min

    required_list = []
    for s in student:
        if (s[1] == _2min):
            required_list.append(s[0])
    
    print(required_list)
    required_list.sort()
    for st in required_list:
        print(st)
    
