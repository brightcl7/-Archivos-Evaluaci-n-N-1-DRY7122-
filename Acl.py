aclNum = int(input("que el numero de la ACL necesita?"))
if aclNum >=1 and aclNum <=99:
    print ("es una ACL de tipo estandar.")
elif aclNum >100 and aclNum <= 199:
    print ("es una ACL de tipo extendida")
else:
    print("el numero ingresado no corresponde a una ACL")
