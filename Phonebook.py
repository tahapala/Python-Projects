# Step 1: Create a Node class representing a single contact
class ContactNode:
    def __init__(self, name, phone_number):
        self.name = name                  # The contact's name (Used for alphabetical sorting)
        self.phone_number = phone_number  # The contact's phone number
        self.left = None                  # Pointer to the alphabetically smaller contact
        self.right = None                 # Pointer to the alphabetically larger contact

# Step 2: Create the Binary Search Tree class to manage the phonebook
class PhoneBookTree:
    def __init__(self):
        self.root = None  # The very first contact in our phonebook

    # Method to add a new contact
    def add_contact(self, name, phone_number):
        # If the phonebook is totally empty, this contact becomes the root
        if self.root is None:
            self.root = ContactNode(name, phone_number)
            print(f"Added root contact: [{name}]")
        else:
            # If not empty, use our helper function to find the right spot
            self._add_recursive(self.root, name, phone_number)

    # Helper method that physically traverses the tree to add the node
    def _add_recursive(self, current_node, name, phone_number):
        # In Python, string comparison ("A" < "B") checks alphabetical order automatically!
        if name < current_node.name:
            # Go LEFT
            if current_node.left is None:
                current_node.left = ContactNode(name, phone_number)
                print(f"Added [{name}] to the LEFT of [{current_node.name}]")
            else:
                self._add_recursive(current_node.left, name, phone_number)
                
        elif name > current_node.name:
            # Go RIGHT
            if current_node.right is None:
                current_node.right = ContactNode(name, phone_number)
                print(f"Added [{name}] to the RIGHT of [{current_node.name}]")
            else:
                self._add_recursive(current_node.right, name, phone_number)
                
        else:
            print(f"Contact [{name}] already exists in the phonebook!")

    # Method to search for a contact's phone number
    def search_contact(self, name):
        print(f"\n--- Searching for: {name} ---")
        result_node = self._search_recursive(self.root, name)
        
        if result_node is not None:
            print(f"FOUND! {name}'s phone number is: {result_node.phone_number}")
        else:
            print(f"NOT FOUND! {name} is not in the phonebook.")

    # Helper method to find the contact quickly (O(log n) time complexity)
    def _search_recursive(self, current_node, name):
        # Base case: We reached a dead end, the contact is not here
        if current_node is None:
            return None

        # Base case: We found the exact contact!
        if current_node.name == name:
            return current_node
            
        # If the target name is alphabetically smaller, ONLY search the left side
        elif name < current_node.name:
            print(f" -> '{name}' is before '{current_node.name}'. Going LEFT...")
            return self._search_recursive(current_node.left, name)
            
        # If the target name is alphabetically larger, ONLY search the right side
        else:
            print(f" -> '{name}' is after '{current_node.name}'. Going RIGHT...")
            return self._search_recursive(current_node.right, name)


# --- Program Execution Section ---

# 1. Create our Binary Search Tree Phonebook
my_phonebook = PhoneBookTree()

# 2. Add contacts in a random alphabetical order
# 'Michael' will be our root. 
my_phonebook.add_contact("Michael", "555-1001")

# 'Alice' comes before 'Michael', so it goes LEFT
my_phonebook.add_contact("Alice", "555-1002")

# 'Zack' comes after 'Michael', so it goes RIGHT
my_phonebook.add_contact("Zack", "555-1003")

# 'David' comes before 'Michael' but after 'Alice', so it goes LEFT of Michael, then RIGHT of Alice
my_phonebook.add_contact("David", "555-1004")

# 3. Test the high-speed search functionality
my_phonebook.search_contact("David")
my_phonebook.search_contact("Zack")
my_phonebook.search_contact("Sarah") # This one does not exist