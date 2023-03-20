#coding:utf-8

import rosbag
import fire
import cv2
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError
import argparse
import os


def export_image(bag_file, img_topic, des_path):
    bridge = CvBridge()
    seq = 0
    with rosbag.Bag(bag_file, 'r') as bag:  #要读取的bag文件；
        for topic, msg, t in bag.read_messages():
            if topic == img_topic:  #图像的topic；
                try:
                    # TODO delete it!
                    msg.encoding = 'bgr8'
                    cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")
                except CvBridgeError as e:
                    print(e)
                timestr = "{}".format(seq)
                seq += 1
                #%.6f表示小数点后带有6位，可根据精确度需要修改；
                image_name = timestr + ".jpg"  #图像命名：时间戳.jpg
                cv2.imwrite(os.path.join(des_path,image_name), cv_image)  #保存；

def export_pointcloud():
    print('run this command: rosrun pcl_ros pointcloud_to_pcd /input:=/points_raw')
    pass

def opt_parse():
    opt = argparse.ArgumentParser()
    opt.add_argument('--bag-file', type=str, help='path to bag file')
    opt.add_argument('--img-topic', type=str, help='image topic to save')
    opt.add_argument('--des-path', type=str, help='dest path to save')


if __name__ == '__main__':
    opt = opt_parse()
    fire.Fire()