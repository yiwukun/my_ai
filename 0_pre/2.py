import datetime as dt

class MyTimer:

    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.prompt = '未开始计时'
        self.unit = ['年','月','天','小时','分','秒']
        pass

    def start(self):
        self.start_time = dt.datetime.now()
        self.prompt = "\n" + '计时开始:'

    def stop(self):
        if not self.start_time:
            print('计时还没开始，不能结束!')
        else:
            self.end_time = dt.datetime.now()
            self._calc()
            self.prompt += "\n" + '计时结束:'

    def _calc(self):
        self.lasted = []
        """ 
        for index in range(6):
         
         self.lasted.append(self.end_time[index] - self.start_time[index])
         if self.lasted[index]:
             self.status += str(self.lasted[index]) + self.unit[index]
     #print(self.status)
         """

        lastTime =  self.end_time - self.start_time
        self.prompt += "\n总共运行了：" + str(lastTime.total_seconds()) + '秒'

    def __str__(self):
        return self.prompt
    __repr__ = __str__




timer = MyTimer()
timer.start()
for i in range(1000000):
    pass

timer.stop()

print(timer)