#*********************************
# AUTORIDAD DE PENSIONES Y SEGUROS
# AUTOR: SERGIO TORREJON ALBORNOZ
#*********************************
import statistics 

array = [2,3,4,5]
print ("The variance of data is : ",end="") 
print (statistics.mean(array)) 

li = [1.5, 2.5, 2.5, 3.5, 3.5, 3.5] 

print ("The variance of data is : ",end="") 
print (round(statistics.mean(li),2)) 



print ("The variance of data is : ",end="") 
print (round(statistics.fmean(li),2))

print ("The variance of data is : ",end="") 
print (statistics.variance(li)) 

print ("The population variance of data is : ",end="") 
print (statistics.pvariance(li)) 

print (statistics.geometric_mean(li)) 

print (statistics.harmonic_mean([40, 60], weights=[5, 30])) 

print (statistics.median(li)) 

print (statistics.mode(li)) 

print (statistics.pstdev(li)) 

print('-------------------------------------------')
# Con while y los índices

print()
input('presione enter para salir')