## Image Finder

**Image Finder** is an automation tool in Python that allows users to detect specific images on the screen that were created beforehand and interact automatically with them. This project facilitates the creation and detection of visual patterns for automating repetitive processes involving graphical elements.

### Requirements
- Python 3.6+
- `pyautogui`
- `cv2` (OpenCV)
- `keyboard`
- `numpy`

### Running

1. Clone the repository:
    ```bash
    git clone https://github.com/fregues-mp/image_finder.git
    ```

2. Install the required dependencies:
    ```bash
    pip install pyautogui opencv-python keyboard numpy
    ```

3. Run the macro with the following command:
    ```bash
    python main.py
    ```

### How to Use
1. Create the images you want to detect on the screen and add them to the project directory. Adjust the image names as necessary in the code.

   Example:
   ```python
   if not base.PN(r'data\example.png', name='test', move_func=base.center, value=c):
       c += 1
   ```

2. Add variations of the same image. The program will look for the next image only if the previous one is not found.

   Example:
   ```python
   if not base.PN(r'data\example1.png', r'data\example2.png', r'data\example3.png', name='test', move_func=base.center, value=c):
       c += 1
   ```

3. The **EI()** function allows you to automatically stop the loop upon detecting a specific image called "reset" or another of your choice. When the image is detected, the loop will be interrupted.

    Example:
    ```python
    if base.EI('reset'):
        c = 0
        break  
    ```

### Click on Edges and Corners

Now, you can specify where you want the click to occur, using specific click functions that can be applied to different parts of the detected image, such as the edges or corners.

Example usage:

```python
# Click in the center
base.EI_Click_PN(r'data/test.png', name='test', move_func=base.center, value=c)

# Click in the bottom left corner
base.EI_Click_PN(r'data/test.png', name='test', move_func=base.bottom_left, value=c)

# Click to the left
base.EI_Click_PN(r'data/test.png', name='test', move_func=base.left, value=c)
```

Available movement functions:

- `center(pos, size)` - center
- `bottom(pos, size)` - bottom edge
- `top(pos, size)` - top edge
- `left(pos, size)` - left edge
- `right(pos, size)` - right edge
- `top_left(pos, size)` - top left corner
- `top_right(pos, size)` - top right corner
- `bottom_left(pos, size)` - bottom left corner
- `bottom_right(pos, size)` - bottom right corner

### Supported Image Formats

OpenCV supports a variety of image formats that can be used with the detection function. Some of the supported formats include:

- **PNG** (`.png`)
- **JPEG** (`.jpg`, `.jpeg`)
- **BMP** (`.bmp`)
- **TIFF** (`.tiff`, `.tif`)
- **GIF** (`.gif`) - only the first image in an animated GIF sequence.
- **PPM** (`.ppm`)
- **PGM** (`.pgm`)
- **PBM** (`.pbm`)
- **WebP** (`.webp`) - available in newer versions of OpenCV.

### Contributions

![logo_small](https://github.com/user-attachments/assets/3a29afa3-0b39-43ee-9760-cca03d978e62)

-------

Feel free to contribute! Open an *issue* or submit a *pull request*.

### License

This project is licensed under the [MIT License](https://github.com/fregues-mp/image_finder/blob/main/LICENSE).