

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
    prepend(nodeValue){
        let first = {
            val: nodeValue ? nodeValue : null,
            next: this.head
        }
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
}

const myLinkedList = new LinkedList(5)
myLinkedList.append(2)
myLinkedList.append(8)
myLinkedList.append(3)
myLinkedList.prepend(12)
// myLinkedList.remove(2)
myLinkedList.remove(0)
myLinkedList.pop()

console.log("THe Lklst: " + JSON.stringify(myLinkedList))