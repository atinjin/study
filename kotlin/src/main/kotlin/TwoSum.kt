import java.util.*

/**
 * @author Atin (atinjin@coupang.com)
 * @since 2018. 11. 07
 *
 * https://leetcode.com/problems/two-sum/
 */
fun main(args: Array<String>) {
    val nums = intArrayOf(2, 7, 11, 15)
    val target = 9
    val solution = Solution()
    val result = solution.twoSum(nums, target)
    println(Arrays.toString(result))

}

class Solution {
    fun twoSum(nums: IntArray, target: Int) : IntArray {
        for(i in nums.indices) {
            for(j in nums.indices) {
                if(i != j && nums[i] + nums[j] == target) {
                    return intArrayOf(i,j)
                }
            }
        }
        return intArrayOf()
    }
}