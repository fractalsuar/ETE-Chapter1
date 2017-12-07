aclNum=int(input ("what is the IPv4 ACL number?"))
if aclNum >=1 and aclNum <=99:
    print("this is a standard IPv4 ACL")
elif aclNum >= 100 and aclNum <= 199:
    print("this is a extended IPv4 ACL")
else:
    print("this is not a standard IPv4 ACL.")
    
