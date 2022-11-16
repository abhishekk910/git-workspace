package main

import (
	"errors"
	"fmt"
)

type BST struct {
	key   int
	left  *BST
	right *BST
}

func (t *BST) Insert(data int) error {
	if t == nil {
		return errors.New("Tree is nil")
	}

	if t.key == data {
		return errors.New("This node value already exists")
	}

	if t.key > data {
		if t.left == nil {
			t.left = &BST{key: data}
			return nil
		}
		return t.left.Insert(data)
	}

	if t.key < data {
		if t.right == nil {
			t.right = &BST{key: data}
			return nil
		}
		return t.right.Insert(data)
	}
	return nil
}

// func (tree *BST) delete ()

func (t *BST) search(data int) {
	if data == t.key {
		fmt.Println("Node is Present in the tree")
		return
	}
	if data < t.key {
		if t.left == nil {
			fmt.Println("Node is not present in tree")
		} else {
			t.left.search(data)
			return
		}
	} else {
		if t.right == nil {
			fmt.Println("Node is not present in tree")
		} else {
			t.right.search(data)
			return
		}
	}
}

func (t *BST) PreOrder() {
	if t != nil {
		fmt.Printf("%d ", t.key)
		t.left.PreOrder()
		t.right.PreOrder()
	}
	return
}

func (t *BST) FindMin() int {
	if t.left == nil {
		return t.key
	}
	return t.left.FindMin()
}

func (t *BST) FindMax() int {
	if t.right == nil {
		return t.key
	}
	return t.right.FindMax()
}

func count(bst *BST) int {
	if bst == nil {
		return 0
	}
	return (1 + count(bst.left) + count(bst.right))
}

// Delete removes the Item with value from the tree
func (t *BST) Delete(data int) {
	t.remove(data)
}

func (t *BST) remove(value int) *BST {
	if t == nil {
		return nil
	}
	if value < t.key {
		t.left = t.left.remove(value)
		return t
	}
	if value > t.key {
		t.right = t.right.remove(value)
		return t
	}
	if t.left == nil && t.right == nil {
		t = nil
		return nil
	}
	if t.left == nil {
		t = t.right
		return t
	}
	if t.right == nil {
		t = t.left
		return t
	}

	smallestValueonright := t.right

	for {
		//find smallest value on the right side
		if smallestValueonright != nil && smallestValueonright.left != nil {
			smallestValueonright = smallestValueonright.left
		} else {
			break
		}
	}
	t.key = smallestValueonright.key
	t.right = t.right.remove(t.key)
	return t
}

func main() {
	bst := &BST{}
	list1 := []int{20, 4, 30, 4, 1, 5, 6}
	bst.key = 10
	for _, val := range list1 {
		bst.Insert(val)
	}
	fmt.Println("Preorder Traversal : ")
	bst.PreOrder()
	fmt.Println()
	res := bst.FindMin()
	fmt.Println(res)
	res = bst.FindMax()
	fmt.Println(res)
	bst.search(1)
	// res = count(bst)
	// fmt.Println(res)
	bst.Delete(30) 
	bst.PreOrder()
}
