from LinkedList import LinkedList

def sumList(llA, llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = LinkedList()
    
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.add(int(result%10))
        carry = result/10
    return ll



ll1 = LinkedList()
ll2 = LinkedList()

ll1.generate(3, 0, 11)
ll2.generate(3, 0, 11)

print(ll1)
print(ll2)
print("\n")

print(sumList(ll1, ll2))
