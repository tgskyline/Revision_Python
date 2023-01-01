
# lista_aninhada = [ [1,2,3],[4,5,6,7],[8,9],[ [10,11,12], [13, 14, 15] ] ]

# print (lista_aninhada[3][1][0])


# d = {'a': 0, 'b': 1, 'c': 0} 
# if d['a'] > 0:
#    print('ok')
# elif d['b'] > 0:
#    print('ok')
# elif d['c'] > 0:
#    print('ok')
# elif d['d'] > 0:
#    print('ok')
# else:
#    print('not ok')

# numeros = [n for n in range(1, 16)]
# filter(lambda x: x%3 ==0, numeros)


# bissextos = list(range(1900, 2021, 4))

# # bissextos = [ano for ano in range(1900, 2021, 4) if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)]

# # bissextos = list(filter(lambda ano: (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0), range(1900, 2021, 4)))

# bissextos = [ano for ano in range(1900, 2021, 4) if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)]

# print(bissextos)
        
        
        
# dic = {"MG": "Minas Gerais", "SP":"São Paulo", "AC":"Acre", "MA":"Maranhão"}
# regioes = ["SE", "SE", "NO", "NE"]
# estados = list(zip(dic, dic.values(), regioes))

# print(estados)




# A = [9, 2, 5, 7]
# B = [x for x in range(12,21,3)]
# A.append(B)
# print(A)




# estrutura_aninhada = ( [1,2,3],(4,5,6,7),[8,9],( [10,11,12], [(13, 14), 15] ) )

# # print(estrutura_aninhada[3][1][0][0])

# print(estrutura_aninhada[3][1][0][0])




# x = range(7)
# print(x)

# soma = sum(filter(lambda x_i: x_i % 2 == 0, x))
# print(x)
# print(soma)



# L=[]
# for i in range(10,1,-1):
#     L.append(i)
# print(L[3:])




# from functools import reduce
# teste = [1, 9, 8, 2, 3, 7, 6, 4, 5]
# print(reduce(lambda n1, n2: n1 if n1 > n2 else n2, teste))




# def func():
#     x = 1
#     print(x)

# x = 10
# func()
# print(x)

number =3
print (f"the number is number ")

from math import sin(x)