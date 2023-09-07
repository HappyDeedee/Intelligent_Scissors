```
python setup.py build_ext --inplace
python app.py
```



you need to install:
* pip install opencv-python
* pip install pillow
* pip install dotmap    
* pip install cython
* pip install scikit-image


Notes:
1. blues lines are point paths.
2. red line is the close path.
3. Result Image window shows the cropped image that can be saved.
4. Online Mode button can be switched batch mode, and you have to select calculate button to do the calculation
5. Online Mode will do the calculation automatically every time you delete or add a node.
6. Set the downsampling factor before open the image.
7. For large images, please consider downsample them. Otherwise, it takes really long time to calculate.