import sys
import base64
user = sys.argv[1]
password = sys.argv[2]
encoded = base64.b64encode(user +":"+password)
result = "Basic+" + encoded
print result


