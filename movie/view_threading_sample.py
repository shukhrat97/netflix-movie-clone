from rest_framework.decorators import api_view
from rest_framework.response import Response
import threading
import time

# shunchaki bu misol uchun qilingan api.
# threading qanday ishlashi bo'yicha misol.


class MyThreadingThread(threading.Thread):
    def __init__(self, total):
        threading.Thread.__init__(self)
        self.total = total

    def run(self):
        print('thread started and it will sleep')
        time.sleep(self.total)
        print("Do something")
        print(self.total)


@api_view(['GET'])
def threading_sample_api(request):
    count = 20
    MyThreadingThread(count).start()
    return Response({"message": "successsss"})
