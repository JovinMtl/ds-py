

class LinkedList {
    constructor(firstNode){
        this.head = {
            val : firstNode,
            next : null
        };
        this.tail = this.head;
        this.length = firstNode ? 1 : 0
    }
}

const myLinkedList = new LinkedList(5)

console.log("THe Lklst: " + JSON.stringify(myLinkedList))