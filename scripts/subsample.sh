#! /bin/bash
# this script shuffles and subsamples 100k lines from the training data I chose

scripts=`dirname "$0"`
base=$scripts/..

myData=$base/myData

cd $myData

mkfifo oneseed twoseed
tee oneseed twoseed < /dev/urandom > /dev/null &
shuf -n 100000 --random-source=oneseed train.en-de.de > train.sample.en-de.de &
shuf -n 100000 --random-source=twoseed train.en-de.en > train.sample.en-de.en &
wait
echo Subsampling done
