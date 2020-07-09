from imutils import paths
import numpy as np
import argparse
import cv2
import os


def dhash(image, hashSize=8):
    # convert the image to grayscale and resize,
    # add a single column (width) so we can compute the horizontal gradient
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (hashSize + 1, hashSize))
    # compute the (relative) horizontal gradient between adjacent column pixels
    diff = resized[:, 1:] > resized[:, :-1]
    # convert the difference image to a hash and return it
    return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])


# argument parser to parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
                help="path to input dataset")
ap.add_argument("-r", "--remove", type=int, default=-1,
                help="whether or not duplicates should be removed (i.e., dry run)")
args = vars(ap.parse_args())

# get the paths to all images in our input dataset directory
print("[INFO] computing image hashes...")
imagePaths = list(paths.list_images(args["dataset"]))

# initialize hashes dictionary
hashes = {}


for imagePath in imagePaths:
    # load the input image and compute the hash
    image = cv2.imread(imagePath)
    h = dhash(image)
    # get all image paths with that hash, add the current imagepath to it
    # store the list back in the hashes dictionary
    p = hashes.get(h, [])
    p.append(imagePath)
    hashes[h] = p

for (h, hashedPaths) in hashes.items():
    # check to see if there is more than one image with the same hash
    if len(hashedPaths) > 1:
        # check to see if this is a dry run
        if args["remove"] <= 0:
            # initialize a imgStack to store all images with the same hash
            imgStack = None

            for p in hashedPaths:

                image = cv2.imread(p)
                image = cv2.resize(image, (150, 150))
                # if our imgStack is None, initialize it
                if imgStack is None:
                    imgStack = image
                # otherwise, horizontally stack the images
                else:
                    imgStack = np.hstack([imgStack, image])
            # show the imgStack for the hash
            print("[INFO] hash: {}".format(h))
            cv2.imshow("Duplicate Image Stack", imgStack)
            cv2.waitKey(0)

            # otherwise, we'll be removing the duplicate images without showing
        else:
            # loop over all image paths with the same hash *except*
            # for the first image in the list
            for p in hashedPaths[1:]:
                os.remove(p)
