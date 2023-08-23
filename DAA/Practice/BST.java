class Node {
    int value;
    Node left, right;

    Node(int val) {
        this.value = val;
    }

}

public class BST {
    Node root;

    void addNode(int val) {
        Node node = new Node(val);
        if (root == null) {
            root = node;
            return;
        }
        Node next = root;
        Node t1 = next;
        while (next != null) {
            t1 = next;
            next = (val < next.value) ? next.left : next.right;
        }
        if (val < t1.value)
            t1.left = node;
        else
            t1.right = node;
    }

    void inorder(Node rootNode) {
        if (rootNode != null) {
            inorder(rootNode.left);
            System.out.println("Data:" + rootNode.value);
            inorder(rootNode.right);
        }

    }

    public static void main(String[] args) {
        BST bst = new BST();
        bst.addNode(2);
        bst.addNode(1);
        bst.addNode(13);
        bst.addNode(43);
        bst.inorder(bst.root);
    }
}
