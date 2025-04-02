

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
        this.tail.next = {
            val: nodeValue,
            next: null
        }
    }
}

const myLinkedList = new LinkedList(5)
myLinkedList.append(2)

console.log("THe Lklst: " + JSON.stringify(myLinkedList))