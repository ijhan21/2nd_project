import sys
sys.path.append("kiosk/")

print(sys.path)

from models import *
a = Company.objects.get(id=1)
print(a)

