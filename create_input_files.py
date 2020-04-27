from utils import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    trainCaptionPath = "../datasets/coco2014/trainval_coco2014_captions/captions_train2014.json"
    valCaptionPath = "../datasets/coco2014/trainval_coco2014_captions/captions_val2014.json"
    trainImagePath = "../datasets/coco2014/"
    valImagePath = "../datasets/coco2014/2014/"
    captionPath = "../scratch/dataset_coco.json"
    
    create_input_files(dataset='coco',
                       karpathy_json_path=captionPath,
                       image_folder=trainImagePath,
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder='../scratch/caption data/',
                       max_len=50)
