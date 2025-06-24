class Solution {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> result=new ArrayList<>();
        if(root==null)
        {
            return result;
        }
        Queue<TreeNode> q=new LinkedList<>();
        q.add(root);
        while(!q.isEmpty())
        {
            List<Integer> list=new ArrayList<>();
            int size=q.size();
            for(int i=0;i<size;i++)
            {
                TreeNode n=q.poll();
                list.add(n.val);
                if(n.left!=null)
                {
                    q.add(n.left);
                }
                 if(n.right!=null)
                {
                    q.add(n.right);
                }
            }
            result.add(list);
        }
        Collections.reverse(result);
        return result;
    }
}
