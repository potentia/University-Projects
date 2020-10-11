import itertools
import time
import sys
import hashlib
import threading



class threadMaker(threading.Thread):
    def __init__(self, threadID, name, startValue, endValue, stepValue, chars):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.startValue = startValue
        self.endValue = endValue
        self.step = stepValue
        self.chars = chars
    def run(self):
        print("Starting Programme")
        print ("Starting " + self.name)
        hashChecker(self.name, termHash, self.startValue, self.endValue, self.step, self.chars)



def hashChecker(threadnum, hashedPassoword ,start, end, step, seq):
    one = time.time()
    for counter in range (start, end, step):
        for products in itertools.product(seq, repeat=counter):
           #print(threadnum)
           #print("".join(products))
            saltedString = "{0}{1}".format(SALT, "".join(products))
            hashedPW = hashlib.md5(saltedString.encode())
            if hashedPW.hexdigest() == hashedPassoword:
                print("The password is: " , "".join(products))
                two = time.time()
                print("The Password Has Been Found In " + str(two - one) + " Seconds Trust Me")
                print("Press CTRL-C To Exit")
                print("Or Just Do Nothing If You Want To Keep Threads Open I Guess ¯\_(ᐛ)_/¯")

if __name__ == "__main__":
    termHash = sys.argv[1]
    chars = ""
    SALT = "FOOBAR"
    
    if len(termHash) > 32:
        termHash = termHash[1:]

    for char in range(126, 31, -1):
        chars += chr(char)
    chars += "£€"
    
    thread1 = threadMaker(1,"Thread 1", 3, 7, 1, chars)
    thread2 = threadMaker(2,"Thread 2", 7, 9, 1, chars)

    thread1.start()
    thread2.start()
    
    
    
    



