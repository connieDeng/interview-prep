class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        #placeholder that points to first element in list; dummy node
        self.head = node() 

    def append(self, data):
        #first create a new node holding data
        new_node = node(data)
        #create a node that will point to current node
        cur = self.head

        #while the next node is not null/none keep traversing
        while cur.next != None:
            #this is the traversing
            cur = cur.next
        #when at the end of the list, append the new node
        cur.next = new_node

    def length(self):
        cnt = 0
        cnt_node = self.head

        while cnt_node.next != None:
            cnt_node = cnt_node.next
            cnt += 1
        return cnt

    #print linked list
    def display(self):
        elem = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elem.append(cur.data)
        print(elem)

    def getData(self, index):
        if index >= self.length():
            print("Error, index to get data is out of bounds")
            return None
        else:
            cnt_node = self.head

            #range does not include index + 1
            #range(3) is 0,1,2
            #range(1) is 0
            for i in range(index+1):
                cnt_node = cnt_node.next

        return cnt_node.data

    def erase(self, index):
        if index >= self.length():
            print("Error, index to erase is out of bounds")
            return
        else:
            cur = self.head
            cur_ind = 0
            # always happens
            while True:
                prev = cur
                cur = cur.next
                if cur_ind == index:
                  prev.next = cur.next
                  return
                else:
                    cur_ind+=1
                    


#testing
my_list = linked_list()
my_list.display()
my_list.append(99)
my_list.append(3)
my_list.append(40)
my_list.display()
print('length: ' + str(my_list.length()))
print('get index[0]: ' + str(my_list.getData(0)))
print('get index[2]: ' + str(my_list.getData(2)))
my_list.erase(1)
my_list.display()
