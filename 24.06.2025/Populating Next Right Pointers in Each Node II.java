// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    public Node(int _val) { val = _val; }
    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
}

class Solution {
    public Node connect(Node root) {
        if (root == null) return null;

        List<Node> currentLevel = new ArrayList<>();
        currentLevel.add(root);

        while (!currentLevel.isEmpty()) {
            List<Node> nextLevel = new ArrayList<>();

            for (int i = 0; i < currentLevel.size(); i++) {
                Node node = currentLevel.get(i);
                if (node == null) 
                    continue;

                // Link to the next node in this level, if any
                if (i < currentLevel.size() - 1) {
                    node.next = currentLevel.get(i + 1);
                }

                // Queue children for the next level
                if (node.left  != null) nextLevel.add(node.left);
                if (node.right != null) nextLevel.add(node.right);
            }

            currentLevel = nextLevel;
        }

        return root;
    }
}
