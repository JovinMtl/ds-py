

class LinkedList {
    constructor(firstNode){
        this.head = {
            val : firstNode,
            next : null
        };
        this.tail = this.head;
        this.length = firstNode ? 1 : 0
    }
    append(nodeValue){
        let last = {
            val: nodeValue ? nodeValue : null,
            next: null
        }
        this.tail.next = last;
        this.tail = last;
        this.length++;
    }
}

const myLinkedList = new LinkedList(5)
myLinkedList.append(2)
myLinkedList.append()
myLinkedList.append(3)

console.log("THe Lklst: " + JSON.stringify(myLinkedList))