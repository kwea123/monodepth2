# Copyright Niantic 2019. Patent Pending. All rights reserved.
#
# This software is licensed under the terms of the Monodepth2 licence
# which allows for non-commercial use only, the full terms of which are made
# available in the LICENSE file.

from __future__ import absolute_import, division, print_function

import os
import skimage.transform
import numpy as np
import PIL.Image as pil

from .mono_dataset import MonoDataset


class CityscapesDataset(MonoDataset):
    """Superclass for different types of KITTI dataset loaders
    """
    def __init__(self, *args, **kwargs):
        super(CityscapesDataset, self).__init__(*args, **kwargs)

        fx = 2262.52
        fy = 2265.3017905988554
        cx = 1096.98
        cy = 513.137

        img_w = 2048
        img_h = 1024

        self.full_res_shape = (img_w, img_h)

        self.K = np.array([[fx/img_w, 0, cx/img_w, 0],
                           [0, fy/img_h, cy/img_h, 0],
                           [0,        0,        1, 0],
                           [0,        0,        0, 1]], dtype=np.float32)

        
    def check_depth(self):
        return False

    def get_color(self, folder, frame_index, side, do_flip):
        all_images = sorted(os.listdir(os.path.join(self.data_path, folder)))
        image_path = os.path.join(self.data_path, folder, all_images[frame_index])
        color = self.loader(image_path)

        if do_flip:
            color = color.transpose(pil.FLIP_LEFT_RIGHT)

        return color