import os
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="split")
    parser.add_argument("--data_dir", type=str, help="data directory")
    parser.add_argument("--split", type=str, help="train or val", choices=["train", "val"])
    args = parser.parse_args()

    if args.split == 'train':
        seqs = ['road01_ins', 'road02_ins', 'road02_seg', 'road03_ins', 'road03_seg']
    elif args.split == 'val':
        seqs = ['road04_ins', 'road04_seg']

    with open('%s_files.txt'%args.split, 'w') as f:
        for seq in seqs:
            for record in sorted(os.listdir(os.path.join(args.data_dir, seq, 'ColorImage'))):
                sequence_length = len(os.listdir(os.path.join(args.data_dir, seq, 'ColorImage', record, 'Camera 5')))
                for frame_idx in range(1, sequence_length-1):
                    f.writelines(os.path.join(seq, "ColorImage", record, "Camera")+' %d 5\n'%frame_idx)