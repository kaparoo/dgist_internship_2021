from PIL import Image

# resize features
resized_width = 224
resized_height = 224

#root_dir = "./datasets/dataset_blue"
root_dir = "./datasets"

# label prefix
# prefix_list = ["blocked", "free"]
prefix_list = ["obstacle_black"]

# number of images for each label
# num_images = [30, 30]
num_images = [12]

# image resize function
def resizeImage(prefix, num):

    old_path = f"{root_dir}/{prefix}_raw/"
    new_path = f"{root_dir}/{prefix}/"

    for i in range(1, num+1):
        image_name = f"{prefix} ({i}).jpg"
        image = Image.open(old_path+image_name)
        image_resize = image.resize((resized_width, resized_height))
        image_resize.save(new_path+image_name)
        print(f"{i}th image is resized!")

# image rotation function
def rotateImage(prefix, num):
    for i in range(1, num+1):
        path = f"{root_dir}/{prefix}/{prefix} ({i}).jpg"
        img = Image.open(path)
        for deg in (90, 180, 270):
            rotated_img = img.rotate(deg)
            path = f"{root_dir}/{prefix}/{prefix} ({i}) {deg}deg.jpg"
            rotated_img.save(path)
    print("Done!")


def main():
    for prefix, num in zip(prefix_list, num_images):    
        print(f"Resize (raw) images in {prefix}-labeled folder.")
        resizeImage(prefix, num)
        print(f"Done! Resized {num} images")

    # for prefix, num in zip(prefix_list, number_of_images):    
    #    print(f"Rotate images in {prefix}-labeled folder.")
    #    rotateImage(prefix, num)
    #    print(f"Done! Resized {num} images")

main()

