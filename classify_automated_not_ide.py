import os
import cv2
import numpy as np
from keras.models import load_model
import os




def init_model(weights_path):
    model = load_model(weights_path)
    model.summary()
    return model

def start_classify(source_dir,
                    save_dir,
                    weights_path,
                    classes,
                    num_classes,
                    height,
                    width):
    width = int(width)
    height = int(height)
    print(source_dir)

    for class_name in classes:
        if not os.path.isdir(os.path.join(save_dir, class_name) + "/"):
            os.mkdir(save_dir + class_name + "/")

    first_time = True
    if (first_time):
        model = init_model((weights_path))
        first_time = False

    imgs_names = os.listdir(source_dir)
    pred = 'cat'
    color_flag = 1
    for img_name in imgs_names:
        print(img_name)
        ext = img_name[img_name.rfind(".") + 1:]
        if ext == "jpg" or ext == "png" or ext == "jpeg":
            print(source_dir + img_name, "img_path")
            img = cv2.imread(os.path.join(source_dir, img_name), color_flag)
            img_copy = img.copy()
            # img = optional_procssing(img)  # currently nothing
            # img = crop_and_clahe(img, gray=1, number_cut_pixels=100) # in case of seaweed and marine debris
            # img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            x = cv2.resize(img, (width, height))
            x = x / 255
            x = np.expand_dims(x, axis=0)
            y = model.predict(x, batch_size=1)
            cls_idx = y.argmax(axis=1)[0]
            conf = y[0][cls_idx]
            print("savepath", os.path.join(save_dir, classes[cls_idx],img_name))
            cv2.imwrite(os.path.join(save_dir, classes[cls_idx],img_name), img_copy)

def predict(img_name,
            save_dir,
            weights_path,
            classes,
            num_classes,
            height,
            width):
    pred = 'cat'
    print(width, height)
    width = int(width)
    height = int(height)
    first_time = True
    if (first_time):
        model = init_model((weights_path))
        first_time = False

    print(img_name)
    color_flag = 1
    img = cv2.imread(img_name, color_flag)
    img_copy = img.copy()
    #img = optional_procssing(img)  # currently nothing
    # img = crop_and_clahe(img, gray=1, number_cut_pixels=100)
    # img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    x = cv2.resize(img, (width, height))
    x = x / 255
    x = np.expand_dims(x, axis=0)
    y = model.predict(x, batch_size=1)
    cls_idx = y.argmax(axis=1)[0]
    conf = y[0][cls_idx]
    cls_name = classes[cls_idx]


    return (img_name, cls_name)
