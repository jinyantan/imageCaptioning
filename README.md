# Image Captioning Model 2

## Train
Before you begin, make sure to save the required data files for training, validation, and testing. Look at contents of create_input_files.py and point it to the the Karpathy JSON file which can be downloaded here: http://cs.stanford.edu/people/karpathy/deepimagesent/caption_datasets.zip and the image folder containing the extracted train2014 and val2014 folders from your downloaded data.

To create data processed files run:
python create_input_files.py

To utilize the glove embedding, gloveProcessing.ipynb has to be ran with glove_path changed to folder where http://nlp.stanford.edu/data/glove.6B.zip is extracted to.


see train.py on how the model will be trained
The parameters for the model (and training it) are at the beginning of the file, so you can easily check or modify them should you wish to.

To train your model from scratch, simply run:

python train.py

To resume training at a checkpoint, point to the corresponding file with the checkpoint parameter at the beginning of the code.

Note that we perform validation at the end of every training epoch.

## Test
To get a  caption for a particular image run:

python caption.py --img='path/to/image.jpeg' --model='path/to/BEST_checkpoint_coco_5_cap_per_img_5_min_word_freq.pth.tar' --word_map='path/to/WORDMAP_coco_5_cap_per_img_5_min_word_freq.json' --beam_size=5

To generate captions for a validation set: 
run python eval.py, which implements this process for calculating the BLEU score on the validation set, with or without Beam Search.
