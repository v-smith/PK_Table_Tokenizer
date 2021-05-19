#!/bin/bash -l
#$ -l h_rt=9:0:0
#$ -l mem=16G
#$ -l gpu=true
#$ -l tmpfs=15G
#$ -S /bin/bash
#$ -N Train_SP
#$ -wd /home/rmhivsm/Scratch/workspace
hostname
date

PROJECT_DIR='/home/rmhivsm/Scratch/PKTokenizers'
export PYTHONPATH=$PYTHONPATH:$PROJECT_DIR
cd $PROJECT_DIR || exit
source /share/apps/source_files/python/python-3.8.0.source
source .env
source ./.myenv/bin/activate

tar -zcvf $HOME/Scratch/files_from_job_$JOB_ID.tar.gz $TMPDI
PYTHONPATH=deps.zip python train_tokenizer.py
