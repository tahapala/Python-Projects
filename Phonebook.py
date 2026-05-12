class ContactNode:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.left = None
        self.right = None

class PhoneBook:
    def __init__(self):
        self.root = None

    def add(self, name, phone):
        if not self.root:
            self.root = ContactNode(name, phone)
            print(f"Added root: {name}")
        else:
            self._add_node(self.root, name, phone)

    def _add_node(self, node, name, phone):
        if name < node.name:
            if not node.left:
                node.left = ContactNode(name, phone)
                print(f"Added {name} (Left of {node.name})")
            else:
                self._add_node(node.left, name, phone)
                
        elif name > node.name:
            if not node.right:
                node.right = ContactNode(name, phone)
                print(f"Added {name} (Right of {node.name})")
            else:
                self._add_node(node.right, name, phone)
                
        else:
            print(f"{name} is already in the phonebook!")

    def search(self, name):
        print(f"\n--- Searching: {name} ---")
        result = self._search_node(self.root, name)
        
        if result:
            print(f"Found {name}! Number: {result.phone}")
        else:
            print(f"{name} not found.")

    def _search_node(self, node, name):
        if not node:
            return None

        if node.name == name:
            return node
            
        if name < node.name:
            print(f" -> '{name}' < '{node.name}'. Going left...")
            return self._search_node(node.left, name)
        else:
            print(f" -> '{name}' > '{node.name}'. Going right...")
            return self._search_node(node.right, name)

if __name__ == "__main__":
    pb = PhoneBook()
    
    # adding contacts
    pb.add("Michael", "555-1001")  # root
    pb.add("Alice", "555-1002")    # goes left
    pb.add("Zack", "555-1003")     # goes right
    pb.add("David", "555-1004")    # goes left then right
    
    # test searches
    pb.search("David")
    pb.search("Zack")
    pb.search("Sarah")
