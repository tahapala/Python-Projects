from collections import deque
import time

class KeyboardBuffer:
    def __init__(self):
        # deque is the most efficient way to implement a queue in Python
        self.buffer = deque()

    def press_key(self, key):
        # Enqueue: Adding a new keystroke to the end of the queue
        self.buffer.append(key)
        print(f"[Hardware] Keystroke registered: '{key}'")

    def show_buffer(self):
        # Displaying the keys currently waiting in the memory
        if not self.buffer:
            print("[System] Buffer is empty. No pending inputs.")
        else:
            print(f"\n[System] Current Queue in RAM: {list(self.buffer)}\n")

    def process_inputs(self):
        # Dequeue: Processing inputs in FIFO (First In, First Out) order
        if not self.buffer:
            print("[OS] No inputs to process.")
            return

        print("[OS] System unfreezing... Processing buffered inputs:")
        
        # As long as there are items in the buffer, process them
        while self.buffer:
            # popleft() removes and returns the first element on the left
            current_key = self.buffer.popleft()
            print(f" -> Executing: [{current_key}]")
            time.sleep(0.5)  # Simulating a slight delay for processing each key
            
        print("[OS] All buffered inputs processed successfully.\n")

if __name__ == "__main__":
    kb = KeyboardBuffer()
    
    print("--- Simulating System Freeze ---")
    
    # User spams keys while the game/system is lagging
    kb.press_key("W")
    kb.press_key("A")
    kb.press_key("Spacebar")
    kb.press_key("Left Mouse Click")
    
    # Let's see what is waiting in the queue
    kb.show_buffer()
    
    # The system recovers and processes everything in the exact order it was pressed
    kb.process_inputs()
    
    # Verifying the buffer is empty after processing
    kb.show_buffer()