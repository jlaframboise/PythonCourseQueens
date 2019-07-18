'''Tower of Hanoi recursion algorithm'''
def moveDisks(h, source, dest, spare):
    if h > 0:
        # move top h-1 disks from source to spare peg
        moveDisks(h - 1, source, spare, dest)
        # move biggest disk to destination
        print('move Disk {} from {} to {}'.format(h, source, dest))
        # move top h-1 disks from spare peg to destination
        moveDisks(h - 1, spare, dest, source)


