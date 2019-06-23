import os
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="split")
    parser.add_argument("--data_dir", type=str, help="data directory", 
                        default='/home/ubuntu/hdd/data/Cityscapes/leftImg8bit_sequence_trainvaltest/leftImg8bit_sequence')
    parser.add_argument("--split", type=str, help="train or val", choices=["train", "val"])
    args = parser.parse_args()

    cities = sorted(os.listdir(os.path.join(args.data_dir, args.split)))

    with open('%s_files.txt'%args.split, 'w') as f:
        for city in cities:
            n_images = len(os.listdir(os.path.join(args.data_dir, args.split, city)))
            for i in range(n_images//30): # number of sequences
                for frame_idx in range(1, 29):
                    f.writelines(os.path.join(args.split, city)+' %d l\n'%(frame_idx+i*30))