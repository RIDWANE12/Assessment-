count=0
with open('/content/Text.txt') as f:
    lines = f.readlines()
    for line in lines:
        if 'data analytics' in line:  
            true=1
            count+=true
    print(count)
    print(count/204)


