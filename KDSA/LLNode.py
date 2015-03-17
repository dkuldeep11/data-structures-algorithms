__author__ = 'Kuldeep'
class Node:
    """This is a Node class which is basic entity to hold the data

        Attributes:
            value (int): it's the value stored in node
            nxt (Node): it points to the next node

        """
    def __init__(self, value = None):
            """It instantiates the Node object

            Args:
                value (int): this is an optional paramter, default value is None
            """
            self.value = value
            self.nxt = None


    def set_value(self, value):
        """It sets the value of the node

        Args:
            value (int): it is used to store the value for current node
        """
        self.value = value


    def get_value(self):
        """It returns the value of node"""
        return self.value


    def set_next(self, nxt):
        """It sets the nxt value"""
        self.nxt = nxt


    def get_next(self):
        """It gets the value of nxt"""
        return self.nxt