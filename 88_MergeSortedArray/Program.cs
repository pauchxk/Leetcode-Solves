public class Solution
{
    public void Merge(int[] nums1, int m, int[] nums2, int n)
    {
        int p1 = m-1;
        int p2 = n-1;
        int i = m+n-1;

        while(p2>=0)
        {
            if(p1 >=0 && nums1[p1] > nums2[p2])
                nums1[i--] = nums1[p1--];
            else
                nums1[i--]= nums2[p2--];
        }

        foreach (var item in nums1) { Console.WriteLine(item); }
    }
}

public class Program
{
    protected static void Main()
    {
        Solution solution = new();
        int[] nums1 = {1,2,3,0,0,0};
        int[] nums2 = { 2,5,6 };
        int m = nums2.Count();
        int n = nums2.Count();
        solution.Merge(nums1, m, nums2, n);
    }
}