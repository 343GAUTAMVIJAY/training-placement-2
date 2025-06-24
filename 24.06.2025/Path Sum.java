class Solution {

    boolean flag = false;

    public boolean hasPathSum(TreeNode root, int targetSum) {
        recursion(root, targetSum);
        return flag;
    }

    private void recursion(TreeNode node, int curVal) {
        if (node == null) return;
        if (node.left == null && node.right == null) {
            // so this is a leaf node
            curVal -= node.val;
            if (curVal == 0) {
                flag = true;
            }
        }

        curVal -= node.val;
        recursion(node.left, curVal);
        recursion(node.right, curVal);
    }
}
