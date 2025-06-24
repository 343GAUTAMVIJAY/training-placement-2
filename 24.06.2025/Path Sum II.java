class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> result = new ArrayList<>();
        dfs(root, targetSum, new ArrayList<>(), result);
        return result;
    }

    private void dfs(TreeNode root, int targetSum, List<Integer> path, List<List<Integer>> result) {
        if (root == null)
            return; // Base case
        path.add(root.val); // For calculation, add current node to path

        // Check for leaf nodes and add path if possible
        if (root.left == null && root.right == null && root.val == targetSum) {
            result.add(new ArrayList<>(path)); // Add a copy of the path
        } else {
            dfs(root.left, targetSum - root.val, path, result);
            dfs(root.right, targetSum - root.val, path, result);
        }

        // Backtrack
        path.remove(path.size() - 1);
    }
}
