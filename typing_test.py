import time
import random
import curses

# --- ENTERPRISE ENGINE BANNER ---
BANNER = r"""
 ██████╗███╗   ███╗███████╗    ████████╗███████╗███████╗████████╗
██╔════╝████╗ ████║██╔════╝    ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
██║     ██╔████╔██║███████╗       ██║   █████╗  ███████╗   ██║   
██║     ██║╚██╔╝██║╚════██║       ██║   ██╔══╝  ╚════██║   ██║   
╚██████╗██║ ╚═╝ ██║███████║       ██║   ███████╗███████║   ██║   
 ╚═════╝╚═╝     ╚═╝╚══════╝       ╚═╝   ╚══════╝╚══════╝   ╚═╝   
                     >> TYPE-SPEED ENGINE v1.0 <<
"""

TEST_PROMPTS = [
    "The quick brown fox jumps over the lazy dog.",
    "Parallel computing structures bypass traditional instruction bottlenecks.",
    "Automated defensive shell scripts accelerate open source intelligence mapping.",
    "Python environments leverage virtual package wrappers to protect system baselines.",
    "An elegant architecture prioritizes clean error exceptions over nested conditional branches."
]

def display_home(stdscr):
    """Renders the stylized menu welcome screen using standard curses dimensions"""
    stdscr.clear()
    
    # Render the text banner line-by-line safely
    for idx, line in enumerate(BANNER.split('\n')):
        if idx < curses.LINES - 2:
            stdscr.addstr(idx, 0, line, curses.color_pair(1))
            
    start_y = len(BANNER.split('\n')) + 2
    stdscr.addstr(start_y, 0, "==========================================================", curses.color_pair(2))
    stdscr.addstr(start_y + 1, 0, " [SYSTEM READY] Press any key to ignite the test engine...", curses.color_pair(3))
    stdscr.addstr(start_y + 2, 0, " [EXIT COMMAND] Press ESC to abort execution.", curses.color_pair(2))
    stdscr.addstr(start_y + 3, 0, "==========================================================", curses.color_pair(2))
    stdscr.refresh()

def execute_test_loop(stdscr):
    """Manages the main typing engine logic and live performance analytics"""
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)

    while True:
        display_home(stdscr)
        key = stdscr.getch()
        
        if key == 27:  # ESC Key mapping
            break
            
        # Initialize target challenge parameters
        target_text = random.choice(TEST_PROMPTS)
        user_input = []
        start_time = None
        
        while True:
            stdscr.clear()
            
            # Draw header metrics placeholder
            stdscr.addstr(1, 0, "=== RUNTIME MONITOR ===", curses.color_pair(1))
            
            # Render target challenge phrase string
            stdscr.addstr(3, 0, target_text, curses.color_pair(4))
            
            # Render user input string overlay with real-time feedback
            for idx, char in enumerate(user_input):
                if idx < len(target_text):
                    if char == target_text[idx]:
                        stdscr.addstr(5, idx, char, curses.color_pair(3)) # Correct (Green)
                    else:
                        stdscr.addstr(5, idx, target_text[idx] if target_text[idx] != " " else "_", curses.color_pair(2)) # Mismatch (Red)
            
            stdscr.refresh()
            
            # Wait for user input interaction
            in_key = stdscr.getch()
            
            if start_time is None and in_key not in [27, 10, 8, 127, 263]:
                start_time = time.time()
                
            if in_key == 27: # ESC out to main menu
                break
            elif in_key in (8, 127, curses.KEY_BACKSPACE): # Structural backspacing hooks
                if len(user_input) > 0:
                    user_input.pop()
            elif in_key in (10, 13) or len(user_input) >= len(target_text): # Execution break on Enter or string saturation
                elapsed_time = max(time.time() - start_time if start_time else 0, 0.001)
                
                # Metrics Calculation
                typed_chars = len(user_input)
                correct_chars = sum(1 for u, t in zip(user_input, target_text) if u == t)
                
                wpm = round((typed_chars / 5) / (elapsed_time / 60))
                accuracy = round((correct_chars / max(typed_chars, 1)) * 100)
                
                # Show results summary stage
                stdscr.clear()
                stdscr.addstr(2, 0, "🏁 CORE STATISTICS ANALYSIS CAPTURED", curses.color_pair(1))
                stdscr.addstr(4, 0, f"⏱️ Elapsed Duration : {elapsed_time:.2f} seconds")
                stdscr.addstr(5, 0, f"🚀 Typing Velocity   : {wpm} WPM (Words Per Minute)")
                stdscr.addstr(6, 0, f"🎯 Precision Metric  : {accuracy}% Accuracy")
                stdscr.addstr(8, 0, "--> Press any key to loop back to home terminal...", curses.color_pair(3))
                stdscr.refresh()
                stdscr.getch()
                break
            else:
                if len(user_input) < len(target_text):
                    # Filter out non-printable artifacts from key captures
                    if 32 <= in_key <= 126:
                        user_input.append(chr(in_key))

def main():
    # Wrap screen management to handle safe terminal restoration on exit loops
    curses.wrapper(execute_test_loop)

if __name__ == "__main__":
    main()
