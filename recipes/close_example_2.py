from tkinter import *
import time

# Try setting this to False and look at the printed numbers (1 to 10)
# during the work-loop, if you close the window while the periodic_call
# worker is busy working (printing). It will abruptly end the numbers,
# and kill the periodic callback! That's why you should design most
# applications with a safe closing callback as described in this demo.
safe_closing = True

# ---------

busy_processing = False
close_requested = False

def close_window():
    global close_requested
    close_requested = True
    print("User requested close at:", time.time(), "Was busy processing:", busy_processing)

root = Tk()
if safe_closing:
    root.protocol("WM_DELETE_WINDOW", close_window)
lbl = Label(root)
lbl.pack()

def periodic_call():
    global busy_processing

    if not close_requested:
        busy_processing = True
        for i in range(10):
            print((i+1), "of 10")
            time.sleep(0.2)
            lbl["text"] = str(time.time()) # Will error if force-closed.
            root.update() # Force redrawing since we change label multiple times in a row.
        busy_processing = False
        root.after(500, periodic_call)
    else:
        print("Destroying GUI at:", time.time())
        try: # "destroy()" can throw, so you should wrap it like this.
            root.destroy()
        except:
            # NOTE: In most code, you'll wanna force a close here via
            # "exit" if the window failed to destroy. Just ensure that
            # you have no code after your `mainloop()` call (at the
            # bottom of this file), since the exit call will cause the
            # process to terminate immediately without running any more
            # code. Of course, you should NEVER have code after your
            # `mainloop()` call in well-designed code anyway...
            # exit(0)
            pass

root.after_idle(periodic_call)
root.mainloop()