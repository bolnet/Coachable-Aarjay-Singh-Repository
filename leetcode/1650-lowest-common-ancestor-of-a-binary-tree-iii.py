'''
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
p=5
q=4
store path from p to root in [5,3]
traverse path from q to root and keep checking if node exist in set if yes retur the node
4->2->5 ...return 5

         A
       /   \
      B     C
     / \   /
    D   E F
       /
      G

      p=G q =F
      we use two pointer approcah to find the intersection.
      initialize two pointers p_pointer and q_pointer
      loop through till p_pointer and q_pointer are equal
        update p_pointer to it's parent if parent exist.
            if you reach to root then start traversing from the beginning of another node q
        update q_pointer to it's parent if parent exist
        if parent doesn't exist restart your travel from the beginning of other node p

      return p_pointer

    example:
    P_POINTER : G E B A F C A
    Q_POINTER : F C A G E B A



'''
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        s=set()
        while p:
            s.add(p.val)
            p=p.parent
        while q:
            if q.val in s:
                return q
            else:
                q=q.parent
        return None

    def lowestCommonAncestorEfficient(self, p: 'Node', q: 'Node') -> 'Node':
        p_pointer = p
        q_pointer = q
        while p_pointer != q_pointer:
            p_pointer = p_pointer.parent if p_pointer.parent else q
            q_pointer = q_pointer.parent if q_pointer.parent else p
        return p_pointer
