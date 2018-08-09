import signal
import sys
import time


# This class helps in taking input from the user
# If the user does not input within one second, it times out
class GetchUnix:
    def __init__(self):
        import tty

    def __call__(self):
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
getCh = GetchUnix()


def handler(signum, frame):
    raise Exception("Timeout")


def getInput():
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(1)
    try:
        text = getCh()
        signal.alarm(0)
        return text
    except Exception:
        print()
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''
