import os
import argparse
from train import train
from test import test

def main(args):
    if args.mode == 'train':
        print('Training...')
        train(args)
    elif args.mode == 'test':
        print('Testing...')
        test(args)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--mode', type=str, default='train')
    parser.add_argument('--num_epochs', type=int, default=1000)
    parser.add_argument('--batch_size', type=int, default=32)
    parser.add_argument('--latent_dim', type=int, default=200)

    parser.add_argument('--kernel_size', type=int, default=4)
    parser.add_argument('--stride_size', type=int, default=2)

    parser.add_argument('--beta', type=float, default=0.5)
    parser.add_argument('--generator_lr', type=float, default=2e-5)
    parser.add_argument('--discriminator_lr', type=float, default=2e-5)

    parser.add_argument('--device', type=str)
    parser.add_argument('--multi_gpu', type=bool, default=False)
    parser.add_argument('--num_workers', type=int, default=4)

    parser.add_argument('--save_epoch', type=int, default=1)
    parser.add_argument('--sample_epoch', type=int, default=5)
    parser.add_argument('--test_epoch', type=int, default=100)

    parser.add_argument('--checkpoints_path', type=str, default='./checkpoints')
    parser.add_argument('--train_path', type=str, default='./data/train')
    parser.add_argument('--dataset', type=str, default='abdom_ct')
    parser.add_argument('--tensorboard_path', type=str, default='./tensorboard')
    parser.add_argument('--results_path', type=str, default='./results')

    args = parser.parse_args()
    main(args)