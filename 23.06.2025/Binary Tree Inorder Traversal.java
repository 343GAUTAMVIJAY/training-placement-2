class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        // Morris inorder Traversal is a tree traversal algorithm 
        // aiming to achieve a space complexity of O(1) 
        // without recursion or an external data structure
        List<Integer> ans = new ArrayList<>();
        if(root == null){
            return ans;
        }
        TreeNode curr = root;
        while(curr != null){
            // case -1 : if LST is null then add current val and move to the RST
            if(curr.left == null){
                ans.add(curr.val);
                curr = curr.right;
            }else{
                // move to the rightmost element of LST
                // and make a temporary link between curr and rightmost element of LST
                // as rightmodt element of LST is inorder predecessor of current element
                TreeNode prev = curr.left;
                while(prev.right != null && prev.right != curr){
                    prev = prev.right;
                }

                if(prev.right == null){
                    // establish the temporary link and traverse LST
                    // as it is not traversed yet
                    prev.right = curr;
                    curr = curr.left;
                }else{
                    // break the temopary link
                    // add current value to ans as LST is traversed
                    // move to RST
                    prev.right = null;
                    ans.add(curr.val);
                    curr = curr.right;
                }
            }
        }
        return ans;
    }
}
