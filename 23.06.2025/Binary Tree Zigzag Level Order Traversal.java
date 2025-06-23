class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if(root == null) return res;
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
                boolean leftToRight = true;


        while(!q.isEmpty()){
            List<Integer> level = new ArrayList<>();
                        int levelSize = q.size();

            for(int i=0;i<levelSize;i++){
                TreeNode node  = q.poll();
                if(leftToRight){
                    level.add(node.val);
                }
                else{
                    level.add(0,node.val);
                }

                if(node.left != null) q.offer(node.left);
                if(node.right != null) q.offer(node.right);
            }
         res.add(level);
            leftToRight = !leftToRight;         }
        return res;
    }
}
