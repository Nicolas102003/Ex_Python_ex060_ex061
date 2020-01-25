pri = int(input('Primeiro termo'))
r  =int(input('Razão'))
termo = pri
c= 1
while c <= 10:
    print('{} '.format(termo), end='')
    termo = termo + r
    c+=1

