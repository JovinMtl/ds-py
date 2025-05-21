
// Author: Thierry Nsanzumukiza
// Date: May 21, 2025

// Implementing a Binary Search Tree

class node{
    constructor(val){
        this.left = null;
        this.right = null;
        this.parent = null;
        this.value = val;
    }
}

class BsT{
    constructor(rootElm){
        this.root = rootElm;
    }
    add(val){
        let elm = new node(val);
        let currentNode = this.root;
        // let greater = false;
        let shouldLoop = true;
        while(shouldLoop){
            if((val > currentNode.value)){
                if (! currentNode.right){
                    currentNode.right = elm
                    shouldLoop = false
                }else{
                    currentNode = currentNode.right
                    shouldLoop = true
                }
                    
            } else if ((val < currentNode.value)){
                if (! currentNode.left){
                    currentNode.left = elm
                    shouldLoop = false
                }else{
                    currentNode = currentNode.left
                    shouldLoop = true
                }
            }
        }
        return
    }
    
    display(){
        return JSON.stringify(this.root)
    }
}
const root = new node(20)
const bstInstance = new BsT(root)
bstInstance.add(15);
bstInstance.add(25);
bstInstance.add(35);
bstInstance.add(55)
bstInstance.add(95)
bstInstance.add(10)
bstInstance.add(18)
console.log("Have : ", bstInstance.display())