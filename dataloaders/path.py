# -*- coding: utf-8 -*-
"""
 @Time    : 2019/1/21 22:07
 @Author  : Wang Xin
 @Email   : wangxin_buaa@163.com
"""


class Path(object):
    @staticmethod
    def db_root_dir(database):
        if database == 'nyu':
            return '/home/gao/space/github_code/dorn_depth_estimation/data/nyudepth_hdf5'
        elif database == 'kitti':
            return '/home/data/UnsupervisedDepth/wangixn/kitti'
        else:
            print('Database {} not available.'.format(database))
            raise NotImplementedError
