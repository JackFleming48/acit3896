<title>Trees</title>
1. Good for modelling real-life data.<br>
<ol>
   <li>reporting hierarchy at work</li>
   <li>tree of life</li>
   <li>syntax tree</li>
   <li>playoff bracket</li>
</ol>
2. A component of more sophisticated algorithms / datastructs
<ol>
    <li>compression(zip, lzh, etc)</li>
    <li>geometry (k-d trees, BSP trees, etc)</li>
    <li>self-balancing binary trees</li>
    <li>heap</li>
</ol>
3. Many software tools/libraries/APIs use trees for interface
<ol>
    <li>DOM</li>
    <li>filesystem</li>
    <li>programming language syntax</li>
    <li>JSON / serialization</li>
</ol>
Trees have a special node, it is called a <strong>root</strong>. They also have:
<br>
<ul>
    <li>*nodes (aka vertices, singular vertext)</li>
    <li>*edges</li>
    <li>*1 special node, the root</li>
    <ul>
        <li>*(drawn at the top)</li>
    </ul>
    <li>*parent and child relationships(higher is parent, lower is child in a given pair)</li>
    <li>one parent per node (except root)</li>
    <li>nodes can have any number of childred (incl 0)</li>
    <ul>
        <li>nodes with 0 children are called leaves</li>
    </ul>
    <li>ancenstor: parent, parent's parent, p's p's p, etc
    <li>descendant: child, child's child, c's c's c, etc</li>
    <li>size: number of nodes</li>
    <li>distance (between two nodes): number of edges to get there</li>
    <li>depth (of node): distance of node to root</li>
        <ul>
            <li>Ex: depth of root is always 0</li>
        </ul>
    <li>height (of node): distance of node to furthest descendant</li>
    <li>depth of tree: maximum depth of any node</li>
    <li>height of tree: maximum height of any nodes</li>
</ul>

Example implementation:<br>
```python
class TreeNode:
    __init__(self, contents):
        self.contents = contents
        self.parent = None # ..... some other TreeNode ....
        self.children = [] # any number of children    
```