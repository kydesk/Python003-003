import threading
import queue
import time
import random

class DiningPhilosophers(threading.Thread):
    def __init__(self, philosopher, times, q, leftLock, rightLock):
        super(DiningPhilosophers, self).__init__()
        self.philosopher = philosopher
        self.times = times
        self.q = q
        self.leftLock = leftLock
        self.rightLock = rightLock

    def run(self):

        print(f'哲学家 {self.philosopher} 就座')   

        while self.times > 0:

            # 每次循环开始时进入思考
            self.think()

            # 尝试拿左叉，等待一秒, 如果拿不到则跳到下一次循环
            pickLeftFork = self.leftLock.acquire(timeout=1)           
            if pickLeftFork:
                self.pickLeftFork()
            else:
                continue
            
            # 拿到左叉后尝试拿右叉，等待一秒，拿到则进餐，拿不到则放下左叉，继续思考
            pickRightFork = self.rightLock.acquire(timeout=1)
            if pickRightFork:
                self.pickRightFork()
                self.eat(self.times)
                self.putLeftFork() # 放叉，解锁
                self.putRightFork() # 放叉，解锁
                self.times -= 1
                print(f'哲学家 {self.philosopher} 用餐结束，还需要进餐 {self.times} 次')
            else:
                self.putLeftFork() # 放叉，解锁
                print(f'哲学家 {self.philosopher} 缺右叉, 继续思考')

        print(f'哲学家 {self.philosopher} 离座') 
   
    def pickLeftFork(self):
        print(f'哲学家 {self.philosopher} 拿左叉')
        self.q.put([self.philosopher, 1, 1])
    
    def pickRightFork(self):
        print(f'哲学家 {self.philosopher} 拿右叉')
        self.q.put([self.philosopher, 2, 1])
    
    def eat(self, times):
        print(f'哲学家 {self.philosopher} 第 {times} 次用餐中……')
        time.sleep(random.randint(1,3))
        self.q.put([self.philosopher, 0, 3])
    
    def putLeftFork(self):
        self.q.put([self.philosopher, 1, 2])
        print(f'哲学家 {self.philosopher} 放左叉')
        self.leftLock.release()
    
    def putRightFork(self):      
        self.q.put([self.philosopher, 2, 2])
        print(f'哲学家 {self.philosopher} 放右叉')
        self.rightLock.release()
    
    def think(self):
        print(f'哲学家 {self.philosopher} 思考中……')
        time.sleep( random.randint(1,3))


if __name__ == '__main__':
    
    q = queue.Queue()

    locks = [threading.Lock() for i in range(5)]
    
    philosophers = [i for i in range(5)]

    times = int(input('请输入每个哲学家需要进餐的次数：'))

    t = []

    for i in range(5):
        if i < 4:
            t.append(DiningPhilosophers(philosophers[i],times,q,locks[i], locks[i+1]))
        else:
            t.append(DiningPhilosophers(philosophers[i],times,q,locks[i], locks[0]))
    
    for i in t:
        i.start()
    
    for i in t:
        i.join()

    # 打印记录
    records_list = []
    while not q.empty():
        records_list.append(q.get())
    print(f'\n哲学家行为记录:\n{records_list}')