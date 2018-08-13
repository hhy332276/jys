import os
#windows设置环境变量：set SECRET_KEY=111111
a=os.environ.get("SECRET_KE") or '123456'
b=os.environ.get("SECRET_KEY",None)
print(a,b)