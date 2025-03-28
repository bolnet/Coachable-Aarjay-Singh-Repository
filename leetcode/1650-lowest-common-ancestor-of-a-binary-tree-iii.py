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
