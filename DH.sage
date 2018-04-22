#-*-coding=utf-8-*-
#选取q的上界
largest=2^50
#选取q的下界
lowest=2^28
#选取素数q
q=random_prime(largest,lbound=lowest)
#选取本原根a
while True:
    a=randint(1,q-1)
    if(multiplicative_order(mod(a,q))==q-1):
	break
#选取私钥
X_A=randint(1,q-1)
#计算公钥
Y_A=mod(a,q)^X_A
#选取私钥
X_B=randint(1,q-1)
#计算公钥
Y_B=mod(a,q)^X_B
#计算密钥
K1=mod(Y_B,q)^X_A
K2=mod(Y_A,q)^X_B
#验证密钥是否相等
if(K1==K2):
    print("True!")
else :
    print("False!")
