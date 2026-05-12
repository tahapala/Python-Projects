class Carriage:
    def __init__(self, cargo):
        self.cargo = cargo
        self.next = None

class Train:
    def __init__(self):
        self.head = None

    def add(self, cargo):
        new_carriage = Carriage(cargo)
        
        # if train is empty, this is the first carriage attached to the engine
        if not self.head:
            self.head = new_carriage
            print(f"Train started with: [{cargo}]")
            return
        
        # traverse to the end of the train
        current = self.head
        while current.next:
            current = current.next
            
        # attach to the last carriage
        current.next = new_carriage
        print(f"Attached to back: [{cargo}]")

    def display(self):
        if not self.head:
            print("Train is currently empty.")
            return

        current = self.head
        layout = "Engine -> " 
        
        # build the visual layout string
        while current:
            layout += f"[{current.cargo}] -> "
            current = current.next
            
        layout += "(End)"
        print(f"\n{layout}\n")

if __name__ == "__main__":
    my_train = Train()
    
    # loading up the train
    my_train.add("Coal")
    my_train.add("Oil Barrels")
    my_train.add("Lumber")
    my_train.add("Steel Pipes")
    
    # check the final layout
    my_train.display()
