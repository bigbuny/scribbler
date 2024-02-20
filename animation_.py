import curses
import time

def loading_animation(win):
    curses.curs_set(0)  # Hide the cursor
    win.clear()

    height, width = win.getmaxyx()
    x = width // 2 - 6
    y = height // 2

    for i in range(1, 101):
        progress_bar = "[" + "=" * (i // 2) + ">" + " " * ((100 - i) // 2) + "]"
        win.addstr(y, x, f"Loading... {progress_bar} {i}%", curses.A_BOLD)
        win.refresh()
        time.sleep(0.1)

    win.addstr(height - 1, 0, "Loading complete!", curses.A_BOLD)
    win.refresh()
    time.sleep(2)

def main(stdscr):
    loading_animation(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)

