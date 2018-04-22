#-*-coding=utf-8-*-

# This file was *autogenerated* from the file DH.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_28 = Integer(28); _sage_const_1 = Integer(1); _sage_const_50 = Integer(50)#选取q的上界
largest=_sage_const_2 **_sage_const_50 
#选取q的下界
lowest=_sage_const_2 **_sage_const_28 
#选取素数q
q=random_prime(largest,lbound=lowest)
#选取本原根a
while True:
    a=randint(_sage_const_1 ,q-_sage_const_1 )
    if(multiplicative_order(mod(a,q))==q-_sage_const_1 ):
	break
#选取私钥
X_A=randint(_sage_const_1 ,q-_sage_const_1 )
#计算公钥
Y_A=mod(a,q)**X_A
#选取私钥
X_B=randint(_sage_const_1 ,q-_sage_const_1 )
#计算公钥
Y_B=mod(a,q)**X_B
#计算密钥
K1=mod(Y_B,q)**X_A
K2=mod(Y_A,q)**X_B
#验证密钥是否相等
if(K1==K2):
    print("True!")
else :
    print("False!")

