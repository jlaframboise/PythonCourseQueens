def printNode(head):
    ptr = head

    while ptr != None:
        print(ptr['data'])
        ptr = ptr['next']


def addToHead(head, value):
    newNode = {'data': value, 'next': head}
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


def deleteHead(head):
    if head == None:
        return None
    return head['next']


# head = someList
# head = addToHead(head, 13)


def main():
    head = None
    head = addToHead(head, 10)
    head = addToHead(head, 3)
    printNode(head)


main()
