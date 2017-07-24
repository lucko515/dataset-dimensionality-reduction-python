# MNIST Visualization with t-SNE, PCA and LDA

Here I've analysed dimensionality reduction techniques on the MNIST images. In this mini project you will find examples of using t-SNE, PCA, KernelPCA and LDA.

## Dataset

Dataset used in this mini project is famouse MNIST dataset. You can download it manually or you can use TensorFlow to do it.

In the case of using TensorFlow to include this dataset, execute these two lines in your python file:

```
from tensorflow.examples.tutorials.mnist import input_data

mnist_data = input_data.read_data_sets("MNIST_data", one_hot=False)
```

## Install

### &nbsp;&nbsp;&nbsp; Supported Python version
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Python version used in this project: 3.5+

### &nbsp;&nbsp;&nbsp; Libraries used

> *  [Tensorflow](https://www.tensorflow.org) 1.2.0
> *  [Numpy](http://www.numpy.org) 1.10.4
> *  [Matplotlib](https://matplotlib.org) 1.5.1
> *  [Scikit-learn](http://scikit-learn.org/stable/) 0.17.1

## Code

The code used in this project is inside **t_sne_mnist_dataset.ipynb**.

## Run

To run this project you will need some software, like Anaconda, which provides support for running .ipynb files (Jupyter Notebook).

After making sure you have that, you can run from a terminal or cmd next lines:

`ipython notebook t_sne_mnist_dataset.ipynb`

or

`jupyter notebook t_sne_mnist_dataset.ipynb`




## License

MIT License

Copyright (c) 2017 Luka Anicin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
