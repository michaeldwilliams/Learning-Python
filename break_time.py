import webbrowser
import time

totalBreaks = 3
breakCount = 0

print "Start time: ",time.ctime()
while (breakCount < totalBreaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=PMivT7MJ41M")
    breakCount = breakCount + 1
    print "Break count is now: ",breakCount
