# Step 1: Create a Node class representing each carriage (vagon)
class CarriageNode:
    def __init__(self, cargo_type):
        self.cargo = cargo_type  # What is inside the carriage (e.g., Coal, Passengers)
        self.next = None         # The mechanical hook pointing to the next carriage

# Step 2: Create the Linked List class representing the entire Train
class TrainSystem:
    def __init__(self):
        self.head = None  # The locomotive (start of the train)

    # Method to attach a new carriage to the END of the train
    def attach_carriage(self, cargo_type):
        new_carriage = CarriageNode(cargo_type)
        
        # If the train is completely empty, the new carriage becomes the first one (connected to locomotive)
        if self.head is None:
            self.head = new_carriage
            print(f"Started the train. First carriage attached: [{cargo_type}]")
            return
        
        # If there are already carriages, we must walk to the end of the train
        current = self.head
        while current.next is not None:
            current = current.next  # Move to the next carriage
            
        # We found the last carriage. Now, hook the new carriage to it.
        current.next = new_carriage
        print(f"New carriage attached to the back: [{cargo_type}]")

    # Method to visually display the train's layout
    def show_train_layout(self):
        print("\n--- Current Train Layout ---")
        
        if self.head is None:
            print("The train has no carriages yet.")
            return

        current = self.head
        # Starting with the locomotive
        layout = "Locomotive -> " 
        
        # Walk through each carriage and add it to our visual layout
        while current is not None:
            layout += f"[{current.cargo}] -> "
            current = current.next
            
        layout += "(End of Train)"
        print(layout)

# --- Program Execution Section ---

# 1. Create a new empty train
my_freight_train = TrainSystem()

# 2. Attach carriages one by one
my_freight_train.attach_carriage("Coal")
my_freight_train.attach_carriage("Oil Barrels")
my_freight_train.attach_carriage("Lumber")
my_freight_train.attach_carriage("Steel Pipes")

# 3. Display the final layout of the train
my_freight_train.show_train_layout()