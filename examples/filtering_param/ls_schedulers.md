ls_schedulers

- lr_scheduler.LambdaLR
optimizer (Optimizer) 
lr_lambda (function or list) 


- lr_scheduler.MultiplicativeLR
optimizer (Optimizer) 
lr_lambda (function or list) 


- lr_scheduler.StepLR
optimizer (Optimizer) 

- lr_scheduler.MultiStepLR
optimizer (Optimizer) 
milestones (list) 


- lr_scheduler.ConstantLR
optimizer (Optimizer) 

- lr_scheduler.LinearLR
optimizer (Optimizer)

- lr_scheduler.ExponentialLR
optimizer (Optimizer) 

- lr_scheduler.PolynomialLR
optimizer (Optimizer)

- lr_scheduler.CosineAnnealingLR
optimizer (Optimizer) 

- lr_scheduler.ChainedScheduler
schedulers (list)

- lr_scheduler.SequentialLR
optimizer (Optimizer) 
schedulers (list)
milestones (list)

- lr_scheduler.ReduceLROnPlateau
optimizer (Optimizer) 
mode (str) 
threshold_mode (str) 
min_lr (float or list) 

- lr_scheduler.CyclicLR
optimizer (Optimizer) 
base_lr (float or list) 
max_lr (float or list) 
mode (str) 
scale_fn (function) 
scale_mode (str) 
base_momentum (float or list) 
max_momentum (float or list) 

- lr_scheduler.OneCycleLR
optimizer (Optimizer) 
max_lr (float or list) 
anneal_strategy (str) 
base_momentum (float or list)
max_momentum (float or list)


- lr_scheduler.CosineAnnealingWarmRestarts
optimizer (Optimizer) 

