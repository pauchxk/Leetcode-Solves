using System;

public class ListNode
{
    public int val;
    public ListNode next;

    public ListNode(int val = 0, ListNode next = null)
    {
        this.val = val;
        this.next = next;
    }
}

public class Solution
{
    public ListNode DeleteDuplicates(ListNode head)
    {
        ListNode current = head;

        if (head == null)
        {
            return null;
        }

        while (current.next != null)
        {
            if (current.val == current.next.val)
            {
                current.next = current.next.next;
            }
            else
            {
                current = current.next;
            }
        }

        return head;
    }
}

public class Program
{
    public static void Main()
    {
        Solution solution = new Solution();

        // Example 1: [1, 1, 2]
        ListNode input1 = BuildLinkedList(new int[] { 1, 1, 2 });
        ListNode result1 = solution.DeleteDuplicates(input1);
        PrintLinkedList(result1);

        // Example 2: [1, 1, 2, 3, 3]
        ListNode input2 = BuildLinkedList(new int[] { 1, 1, 2, 3, 3 });
        ListNode result2 = solution.DeleteDuplicates(input2);
        PrintLinkedList(result2);
    }

    // Helper to build linked list from array
    public static ListNode BuildLinkedList(int[] values)
    {
        if (values.Length == 0) return null;

        ListNode head = new ListNode(values[0]);
        ListNode current = head;

        for (int i = 1; i < values.Length; i++)
        {
            current.next = new ListNode(values[i]);
            current = current.next;
        }

        return head;
    }

    // Helper to print linked list
    static void PrintLinkedList(ListNode head)
    {
        Console.Write("[");
        while (head != null)
        {
            Console.Write(head.val);
            if (head.next != null)
                Console.Write(",");
            head = head.next;
        }
        Console.WriteLine("]");
    }
}
