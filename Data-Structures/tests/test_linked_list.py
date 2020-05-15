from linked_list import __version__
from linked_list.linked_list import LinkedList, Node

def test_version():
    assert __version__ == '0.1.0'

def test_linked_list_created():
    linked_list = LinkedList()
    assert linked_list.head == None

def test_node_created():
    node = Node(7)
    assert node.value == 7
    assert node.next == None

def test_insert_empty():
    fruits = LinkedList()
    fruits.insert("oranges")
    assert fruits.head.value == "oranges"
    assert fruits.head.next == None

def test_insert_filled():
    fruits = LinkedList()
    fruits.insert("oranges")
    fruits.insert("apples")
    assert fruits.head.value == "apples"
    assert fruits.head.next.value == "oranges"

def test_includes():
    sports = LinkedList()
    sports.insert("basketball")
    sports.insert("baseball")
    sports.insert("football")
    assert sports.includes("basketball") == True

def test_not_includes():
    sports = LinkedList()
    sports.insert("basketball")
    sports.insert("baseball")
    sports.insert("football")
    assert sports.includes("soccer") == False

def test_to_string():
    abc = LinkedList()
    abc.insert("c")
    abc.insert("b")
    abc.insert("a")
    assert str(abc) == "{ a } -> { b } -> { c } -> NULL"
