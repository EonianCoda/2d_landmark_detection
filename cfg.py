cfg = {
    ### Model setting ###
    # model type
    'model_type_idx': 0,
    'model_type': {0 : 'classifier',
                   1 : 'regressor'},
    ### Scheduler setting ###
    'scheduler_type': 1,  # 0: ReduceLROnPlateau, 1: Warmup_ReduceLROnPlateau 
    'warm_epoch': 2,   # If scheduler == 1, then use warm_epoch arg
    ### training setting ##
    'train_annot':'./data/train_annot.pkl',
    'train_data_root':'./data/train',
    'split_ratio': 0.9,
    'transform':{'flip':False,
                 'roation':True,
                 'noise':True,},
    ### testing data ##
    'test_annot':'./data/val_annot.pkl',
    'test_data_root':'./data/val',
    
    'seed': 987,
    'epoch':10,
}

classifier_cfg = {
    'num_HG': 1,
    'HG_depth':4,
    ### Training hyperparameters ###
    'batch_size': 8,
    'loss_idx': 0,
    'losses': {0:"MSE",
                1:"wing_loss",
                2:"adaptive_wing_loss"},
    'lr':1e-4
}
regressor_cfg = {
    'backbone_idx': 0,
    'backbone': {0: "mobilenet_v2",
                 1: "efficientnet_b0",
                 2: "mobilenet_v3_small"},
    'dropout': 0.2,
    ### Training hyperparameters ###
    'loss_idx': 2,
    'losses': {0:"L2",
                1:"L1",
                2:"smoothL1",
                3:"wing_loss"},
    'batch_size': 16,
    'lr': 1e-3,
}
