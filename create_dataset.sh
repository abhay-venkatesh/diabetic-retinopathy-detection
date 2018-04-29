#!/usr/bin/env sh
# Create the imagenet lmdb inputs
# N.B. set the path to the imagenet train + val data dirs
set -e
#  --resize_height=$RESIZE_HEIGHT \
    # --resize_width=$RESIZE_WIDTH \
DATA=sample
EXAMPLE=retina256
TRAIN_DATA_ROOT=$DATA/train/
TEST_DATA_ROOT=$DATA/test/

rm -rf $EXAMPLE

RESIZE=false
if $RESIZE; then
  RESIZE_HEIGHT=224
  RESIZE_WIDTH=224
else
  RESIZE_HEIGHT=0
  RESIZE_WIDTH=0
fi

echo "Creating train lmdb..."


mkdir -p $EXAMPLE

GLOG_logtostderr=1 convert_imageset.bin \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    $TRAIN_DATA_ROOT \
    $DATA/train.txt \
    $EXAMPLE/$EXAMPLE"_train_lmdb"

echo "Creating test lmdb..."

GLOG_logtostderr=1 convert_imageset.bin \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    $TEST_DATA_ROOT \
    $DATA/test.txt \
    $EXAMPLE/$EXAMPLE"_test_lmdb"

echo "Done."

compute_image_mean.bin $EXAMPLE/$EXAMPLE"_train_lmdb" \
  $EXAMPLE/$EXAMPLE"_train_mean.binaryproto"
echo "Create Mean."

python convert_mean_proto_to_npy.py  $EXAMPLE/$EXAMPLE"_train_mean.binaryproto"  $EXAMPLE/$EXAMPLE"_train_mean.npy"

echo "Done."
