
class Node{
    constructor(value){
        this.val = value;
        this.next = null
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
                this.length--;
            }
            current = current.next;
        }
    }
    pop(){
        this.head = this.head?.next;
        this.length--;
    }
    print(){
        let data = []
        this.head.val && data.push(this.head.val)
        let next = this.head.next
        while (next?.next != null){
            data.push(next.val);
            next = next?.next
        }
        data.push(this.tail.val)
        return data
    }
}

const myLinkedList = new LinkedList()
myLinkedList.append(1)
myLinkedList.append(2)
myLinkedList.append(3)
myLinkedList.append(4)
myLinkedList.append(5)
myLinkedList.append(6)

console.log("THe Lklst: " + JSON.stringify(myLinkedList))
console.log("Has length of: " + myLinkedList.length)
console.log("Its content: " + myLinkedList.print())