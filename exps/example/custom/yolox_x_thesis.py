#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.

import os

from yolox.exp import Exp as MyExp


class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 1.33
        self.width = 1.25
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]

        # Define yourself dataset path
        self.data_dir = "datasets/thesis_dataset/" # 학습데이터 경로
        self.train_ann = "train.json"
        self.val_ann = "val.json"
        self.test_ann = "test.json"

        self.num_classes = 2

        self.max_epoch = 300 # epoch 수정
        self.data_num_workers = 0
        self.eval_interval = 1