import time
import datetime as funcDate
from datetime import datetime as dt
# ts = time.time()
# print(ts)
ts = dt.now()
print(str(ts).replace("-", "").replace(" ", "").replace(":", "").replace(".", ""))
# print(funcDate.datetime.now())
