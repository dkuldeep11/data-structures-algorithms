# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

__author__ = 'Kuldeep'
from LLNode import Node

class LinkList:
    """This is a LinkList class implementation.

        Attributes:
            head (Node): It is the starting point of LinkList
    """
    def __init__(self, value=None):
        """It instantiates the object of LinkList

        Args:
            value (int): this is an optional parameter, default is None
        """
        if value:
            self.head = Node(value)
        else:
            self.head = None



    def is_empty(self):
        """It checks if LinkList is empty

        Returns:
            Boolean True/False
        """
        if self.head:
            return False
        return True


    def add_node(self, value=None):
        """It adds the node to the LinkList"""

        new_node = Node(value)

        if self.is_empty():
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node


    def show(self):
        """It prints the linklist"""

        curr = self.head
        contents = ''

        while curr != None:
            contents += str(curr.get_value()) + " -> "
            curr = curr.get_next()

        print contents + " null"


    def insert_value_at_position(self, value, position):

        if position < 1:
            print "Invalid position ..."
            return

        new_node = Node(value)

        if position == 1:
            new_node.set_next(self.head)
            self.head = new_node
        else:
            i = 1
            curr = self.head

            while i < position - 1:
                i += 1
                curr = curr.get_next()

            new_node.set_next(curr.get_next())
            curr.set_next(new_node)


    def remove(self):
        """It deletes the head node."""

        if self.is_empty():
            print "LL is empty"
            return

        temp = self.head
        self.head = temp.get_next()

        del temp



    def remove_by_position(self, position):
        """It removes the node from position.

         Args:
            position (int): location from which node is removed

        """

        if position < 1:
            print "Invalid position..."
            return

        if position == 1:
            temp = self.head
            self.head = temp.get_next()
            del temp
        else:
            i = 1
            curr = self.head

            while i < position-1:
                i +=1
                curr = curr.get_next()

            temp = curr.get_next()
            curr.set_next(temp.get_next())
            del temp

        print "deleted from position ", position


    def size(self):
        """calculates the size of LL.

        Returns:
            size (int): size value

        """
        if self.is_empty():
            return 0
        else:
            curr = self.head
            size = 0

            while curr:
                size += 1
                curr = curr.get_next()

            return size


    def search(self, value):
        """searches the value in linklist

        Args:
            value (int): value to be searched

        """
        if self.is_empty():
            print "LL is empty!"
            return

        curr = self.head

        while curr and curr.get_value() != value:
            curr = curr.get_next()

        if curr:
            print value, " is present..."
        else:
            print value, " is not present..."


    def reverse(self):
        pass

    def sort(self):
        pass

if __name__ == "__main__":

    print "Welcome to LinkList..."

    #c1: create linklist
    l1 = LinkList()

    #add_node
    l1.add_node(10)
    l1.add_node(20)
    l1.add_node(30)
    l1.add_node(40)
    l1.add_node(50)

    #print
    l1.show()

    #size
    print str(l1.size())

    #insert_value at 1st
    print "inserting 60"
    l1.insert_value_at_position(60, 1)
    print "updated LL..."
    l1.show()

    #size
    print str(l1.size())


    #insert_value at 2
    l1.insert_value_at_position(70, 2)
    print "updated LL..."
    l1.show()

    #size
    print str(l1.size())

    #remove
    l1.remove()
    print "removing ...updated LL"
    l1.show()

    #size
    print str(l1.size())

    #remove from 1st
    l1.remove_by_position(1)
    print "updated LL"
    l1.show()

    #remove from 3
    l1.remove_by_position(3)
    print "updated LL"
    l1.show()

    #size
    print str(l1.size())

    #search
    l1.search(12)
    l1.search(20)

# <codecell>


