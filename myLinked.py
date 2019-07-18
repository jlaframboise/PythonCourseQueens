head = None


def addToHead(head, data):
    newNode = {'data': data, 'next': head}
    head = newNode
    return head


def addToEnd(head, value):
    newNode = {'data': value, 'next': None}

    if head == None:
        return newNode
    ptr = head
    while ptr['next'] != None:
        ptr = ptr['next']
    ptr['next'] = newNode


def printList(head):
    ptr = head
    while ptr != None:
        print(ptr['data'])
        ptr = ptr['next']


head = addToHead(head, 1)
head = addToHead(head, 2)
head = addToHead(head, 5)
addToEnd(head, -4)
printList(head)
