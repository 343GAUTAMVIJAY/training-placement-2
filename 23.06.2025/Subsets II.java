class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums); // To check for duplicacy
        getSubsets(nums, result, new ArrayList<>(), 0);
        return result;
    }

    public void getSubsets(int[] nums, List<List<Integer>> result, List<Integer> temp, int ind){
        result.add(new ArrayList<>(temp));
        for(int i = ind; i < nums.length; i++){
            if(i > ind && nums[i] == nums[i-1]) continue;
            temp.add(nums[i]);
            getSubsets(nums, result, temp, i + 1);
            temp.remove(temp.size()-1);
        }
    }
}
