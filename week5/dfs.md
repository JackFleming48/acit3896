<title>DFS</title>
DFS is an algorithm for traversing or searching tree or graph data structures.
<ul>
    <li>starts at the root node</li>
    <li>explores as far as possible along each branch before backtracking</li>
    <li>extra memory, usually a stack, is used to keep track of discovered nodes</li>
    <ul>
        <li>help with backtracking</li>
    </ul>
</ul>
<br>
DFS has a time of:<br>
- O(|V| + |E|)
<br>
DFS Pre-order:<br>
<ol>
    <li>visit left subtree<li>
    <li>visit right subtree</li>
    <li>if no child move to parent and subtree not visited</li>
</ol>
DFS Post-order:<br>
<ol>
    <li>visit left subtree</li>
    <li>visit right subtree</li>
    <li>print the node</li>
</ol>
In essence, pre-order you output the node as it is visited, post-order you output the deepest node and until root is reached.