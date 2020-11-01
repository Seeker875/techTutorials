### Variable Reduction Approaches

How to reduce variables in a dataset with 80k variables

Since variable transformations are not allowed we can not use Representation learning based approaches.

Since our base model is Xgboost, we can try to reduce variables by building N xgboost models 

Xgboost with Gpu cuts training time by more than 1/2 for most of the datasets.

Xgboost with Gpu Limitations

1. Only allows tree construction to be hist based. Citi team uses hist based approach so they can easily move to training xgBoost on Gpu

Cost 
1. Training Time for Xgboost
2. Memory limitaions

Build shallower models, less number of rounds, take samples of the variables 20 k at a time, fit the model
