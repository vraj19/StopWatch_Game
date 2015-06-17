import simplegui

# define global variables
minutes = 0
seconds = 0
count = 0
a = 0
b = 0
c = 0
d = 0

# in tenths of seconds into formatted string A:BC.D
def format(t):
    global minutes, seconds, count 
    t = count    
    if (t == 10):
        seconds += 1
        count = 0
    if (seconds == 60):
        minutes += 1
        seconds = 0
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_timer():
    global c, d
    if c-d == 0:
        c += 1
        timer.start()

def stop_timer():
    global a, b, c, d
    if c - d == 1:
        d += 1
        timer.stop()
        b += 1
        if count == 0 :
            a += 1
    
def reset_timer():
    global minutes, seconds, count, a, b, c, d
    timer.stop()
    minutes = 0
    seconds = 0
    count = 0
    a = 0
    b = 0
    c = 0
    d = 0
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global count
    count += 1

#define Draw Handler
def draw_handler(canvas):
    global minutes, seconds, count, a, b
    format(count)
    canvas.draw_text(str(a)+"/"+str(b), (100,30),20, "Yellow")
    if (seconds < 10):
        canvas.draw_text(str(minutes)+":"+ "0"+str(seconds)+"."+str(count),(80,100),30,"White")
    else:
        canvas.draw_text(str(minutes)+":"+str(seconds)+"."+str(count),(80,100),30,"White")

# create frame
frame = simplegui.create_frame("Digital Stopwatch Game! ",300,300)


# register event handlers
timer = simplegui.create_timer(100,timer_handler)
frame.add_button("Start",start_timer,100)
frame.add_button("Stop ",stop_timer,100)
frame.add_button("Reset",reset_timer,100)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()
