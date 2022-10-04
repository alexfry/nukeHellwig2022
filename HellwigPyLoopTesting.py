import colour

print('########### loop test')
inputXYZ = [0.4, 0.1, 0.1]

L_B = 0.1

result =         colour.appearance.hellwig2022.XYZ_to_Hellwig2022(inputXYZ,[95.05,100,108.88],318.31,20,L_B=L_B)
invertedResult = colour.appearance.hellwig2022.Hellwig2022_to_XYZ(result,  [95.05,100,108.88],318.31,20,L_B=L_B)

print(inputXYZ)
print('\n')
print('J = '+ str(result.J))
print('M = '+ str(result.M))
print('h = '+ str(result.h))
print('\n')
print(invertedResult)
