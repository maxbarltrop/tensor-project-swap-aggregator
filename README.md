# tensor-project-swap-aggregator
Tensor Hiring Take-Home Project - Token Swap Aggregator

https://www.loom.com/share/882067db60f94e0aa27e1ba922531934

To run: git clone -> python3 ./aggregate.py

# Algorithm Steps 
- Initialize a Node for every Neighbour of Token A (any token we can swap A to accross all exchanges). Set Token A as the Previous node for this node. Push the Neighbour onto a priority queue, prioritized by the
**swap rate**. Save this Node in a Map from Token -> Node
- Step 2: Continue to pop off the priority queue into **token** and find the current node If we've already found a path to this token with length > 1 that is better than the L1 path, skip and save this for step 3. Otherwise, find the optimal rate from this **token** to every other token. If the amount at our current Node * the optimal rate is better than the existing amount for that neighbouring Node, update it.
- Step 3: Find the optimal rate from all Nodes with an implied path length of 2 to the target token. If one of these computed quantities is higher, update the target node
- Step 4: Output: Iterate back from the target node to all visited Nodes, printing the token and exchanged used. Return the Amount at the target Node. 



