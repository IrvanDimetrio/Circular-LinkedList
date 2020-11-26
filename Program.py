class Node:
 
    # Constructor untuk buat node baru
    def __init__(self, data):
        self.data = data
        self.next = None
 
class CircularLinkedList:
 
    # Constructor untuk buat circular linked list nya
    def __init__(self):
        self.head = None
 
    # Fungsi untuk memasukkan Node di awal
    # circular linked list
    def push(self, data):
        ptr1 = Node(data)
        temp = self.head
 
        ptr1.next = self.head
 
        # Kalau linked list tidak kosong maka set menjadi
        # node terakhir
        if self.head is not None:
            while (temp.next != self.head):
                temp = temp.next
            temp.next = ptr1
 
        else:
            ptr1.next = ptr1  # For the first node
 
        self.head = ptr1
 
        # Fungsi untuk print Nodes sebagai circular linked list
 
    def printList(self):
        temp = self.head
        if self.head is not None:
            while (True):
                print "%d" % (temp.data),
                temp = temp.next
                if (temp == self.head):
                    break
 
# Inisialisasi List kosong nya
cllist = CircularLinkedList()
 
# Hasil akhir linked list akan menjadi 5->2->12->9
cllist.push(9)
cllist.push(12)
cllist.push(2)
cllist.push(5)
 
print "\nIsi dari Circular Linked list nya adalah"
print ""
cllist.printList()
