// Definition for a Node.
// pub struct Node {
//     pub val: i32,
//     pub neighbors: Vec<Rc<RefCell<Node>>>,
// }

use std::cell::RefCell;
use std::collections::HashMap;
use std::rc::Rc;

// TC: O(V + E)
// SC: O(V)
impl Solution {
    pub fn clone_graph(node: Option<Rc<RefCell<Node>>>) -> Option<Rc<RefCell<Node>>> {
        let node = node?;
        let mut clones = HashMap::new();
        Some(Self::clone_from(&node, &mut clones))
    }

    fn clone_from(
        node: &Rc<RefCell<Node>>,
        clones: &mut HashMap<*const RefCell<Node>, Rc<RefCell<Node>>>,
    ) -> Rc<RefCell<Node>> {
        if let Some(clone) = clones.get(&Rc::as_ptr(node)) {
            return Rc::clone(clone);
        }

        let clone = Rc::new(RefCell::new(Node {
            val: node.borrow().val,
            neighbors: Vec::new(),
        }));
        clones.insert(Rc::as_ptr(node), Rc::clone(&clone));

        for neighbor in node.borrow().neighbors.iter() {
            let cloned_neighbor = Self::clone_from(neighbor, clones);
            clone.borrow_mut().neighbors.push(cloned_neighbor);
        }

        clone
    }
}
