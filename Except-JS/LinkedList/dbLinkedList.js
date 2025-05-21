
class Node{
    constructor(value){
        this.val = value;
        this.next = null
        this.prev = null
    }
}

class LinkedList {
    constructor(firstNode){
        let head = new Node(firstNode)
        // this.head = {
        //     val : firstNode,
        //     next : null
        // };
        this.head = head
        this.tail = this.head;
        this.length = firstNode != undefined ? 1 : 0
    }
    append(nodeValue){
        let last = new Node(nodeValue)
        last.prev = this.tail
        // let last = {
        //     val: nodeValue ? nodeValue : null,
        //     next: null
        // }
        this.tail.next = last;
        this.tail = last;
        this.length++;
    }
    prepend(nodeValue){
        let first = new Node(nodeValue)
        first.next = this.head
        this.head.prev = first
        // let first = {
        //     val: nodeValue ? nodeValue : null,
        //     next: this.head
        // }
        this.head = first
        this.length++
    }
    remove(index){
        if (Number(index) >= this.length){
            return undefined
        }
        if (Number(index) == 0){
            this.pop()
            return
        }
        let current = this.head
        for (let i = 0; i <= index; i++){
            if (i == (index -1)){
                // let tempNode = current;
                current.next = current.next.next;
                current.next.next.prev = current.next;
                this.length--;
            }
            current = current.next;
        }
    }
    pop(){
        this.head = this.head?.next;
        this.head.prev = null
        this.length--;
    }
    print(){
        let data = []
        this.head.val != undefined && data.push(this.head.val)
        let next = this.head.next
        while (next?.next != null){
            data.push(next.val);
            next = next?.next
        }
        data.push(this.tail.val)
        return data
    }
    reverse(){
        // this.head = this.tail
        let current = this.tail
        this.head.val = current.val
        this.head.prev = null
        while (current.next != null){
            current.next = this.tail.prev
            this.tail = this.tail.prev
            current = current.next
            current.prev = this.tail.next
        }
        return
    }
}

const myLinkedList = new LinkedList(0)
myLinkedList.append(1)
myLinkedList.append(2)
myLinkedList.append(3)
myLinkedList.append(4)
myLinkedList.append(5)
myLinkedList.append(6)
// myLinkedList.remove(2)
// myLinkedList.remove(0)
// myLinkedList.pop()


// console.log("THe Lklst: " + JSON.stringify(myLinkedList))
console.log("Has length of: " + myLinkedList.length + ": " + myLinkedList.print())
myLinkedList.reverse()
console.log("The reversed : ", myLinkedList.print())
