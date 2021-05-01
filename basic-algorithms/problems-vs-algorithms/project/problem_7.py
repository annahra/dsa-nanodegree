"""
Problem 7: HTTPRouter using a Trie

Version Date: April 14, 2021
"""


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler_root, handler_404):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler_root)
        self.root_handler = handler_root
        self.error_handler = handler_404

    def insert(self, route, the_handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root
        for idx, directory in enumerate(route):
            handler = self.error_handler
            if directory == "":
                handler = self.root_handler
            node.insert(directory, handler)
            node = node.children[directory]
        node.handler = the_handler

    def find(self, route):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root

        if route[0] == "" and len(route) == 1:
            return node.handler

        for directory in route:
            if directory not in node.children:
                return self.error_handler
            node = node.children[directory]
        return node.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, directory, handler):
        # Insert the node as before
        if directory not in self.children:
            self.children[directory] = RouteTrieNode()
        self.handler = handler


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler_root, handler_404):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.web_links = RouteTrie(handler_root, handler_404)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        route = self.split_path(path)
        self.web_links.insert(route, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        route = self.split_path(path)
        return self.web_links.find(route)

    def split_path(self, route):
        # you need to split the path into parts for both the add_handler and loopup functions
        path = route.split('/')
        if path[-1] == "" and len(path) > 1:
            path = path[:-1]
        return path


def main():
    # create the router and add a route
    router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
    router.add_handler("/home/about", "about handler")  # add a route

    # some lookups with the expected output

    # Test Case 1 - Root Handlers
    print("Test Case 1 - Root Handlers")
    print("/ :", router.lookup("/"))  # should print 'root handler'
    print("\"\" :", router.lookup(""))  # should print 'root handler'
    print("End of Test Case 1\n")

    # Test Case 2 - Valid Routes
    print("Test Case 2 - Valid Routes")
    print("/home/about :", router.lookup("/home/about"))  # should print 'about handler'
    print("/home/about/ :", router.lookup("/home/about/"))  # should print 'about handler'
    print("End of Test Case 2\n")

    # Test Case 3 - Non-Valid Routes
    print("Test Case 3 - Non-Valid Routes")
    print("/home :", router.lookup("/home"))  # should print 'not found handler'
    print("/home/about/me :", router.lookup("/home/about/me"))  # should print 'not found handler'
    print("End of Test Case 3\n")


if __name__ == '__main__':
    main()
