Day 12 – Decision Tree Classifier

Today, I worked on building my first Decision Tree Classifier to predict whether a student would Pass or Fail based on study hours and assignments.

What I Learned

• Decision Trees are used for classification problems where the output is categorical.
• The model splits data based on features to separate classes effectively.
• Gini Impurity and Entropy help the tree decide the best splits.
• Leaf nodes provide the final class prediction based on majority voting.
• max_depth controls how deep the tree grows to avoid overfitting.
• random_state ensures the tree structure is reproducible every time.
• Trees handle numerical and categorical features seamlessly.
• plot_tree visualizes the decision-making process clearly.



- Key Formulas

   - Gini Impurity:

       - Gini=1−∑(pi2​)

    - Entropy:

       - Entropy=−∑(pi​⋅log2​(pi​))


- Visualization

  - Nodes show:

     - Feature and split condition

     - Gini/Entropy value

     - Number of samples

     - Class distribution

     - Predicted class

     - Branches show the decision path from root to leaf nodes.


This completes Day 12 of my journey towards mastering DSA & AI/ML.
