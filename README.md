# Image-Tucker-Compress

分别使用tensorly和tensorcomlib测试了张量图像压缩

## 安装Python库

`numpy,pillow,matplotlib,tensorly,skimage,tensorcomlib`

## Tensorly测试结果

运行`tensorly`文件夹下的`image_tucker.py`文件，设置`tucker_rank`分别为[50,50,3]、[100,100,3]、[200,200,3]和[300,300,3]。如果报`Memery`错误，修改`tensorly`源代码，`full_matrx = False`。

运行结果如下：

### rank = [50,50,3]

![](https://i.loli.net/2018/09/11/5b976d893cab0.png)

```
Image Compression Ratio：0.925347646077474
Image Compare PSNR：25.946412228266816
Decomposition Time：0.7083556652069092
```



### rank = [100,100,3]

![](https://i.loli.net/2018/09/11/5b976da997704.png)

```
Image Compression Ratio：0.8316332499186198
Image Compare PSNR：28.686432064795255
Decomposition Time：0.8138234615325928
```



### rank = [200,200,3]

![](https://i.loli.net/2018/09/11/5b976dc42f20a.png)

```
Image Compression Ratio：0.5869839986165364
Image Compare PSNR：30.804968069749638
Decomposition Time：1.4251620769500732
```



### rank = [300,300,3]

![](https://i.loli.net/2018/09/11/5b976de410a5f.png)

```
Image Compression Ratio：0.2660408020019531
Image Compare PSNR：38.38228135960186
Decomposition Time：1.942857027053833
```



## Tensorcomlib

Tensorcomlib是我自己练习写的一个库，测试效果和tensorly相似，输出信息可能更详细一点。

### 比较

![](https://i.loli.net/2018/09/11/5b976e62db9fd.png)

## 联系方式

sunyanqinyin@foxmail.com

## 参考资料

1. Tensorly文档
2. 《基于张量Tucker分解的彩色图像压缩 》，王东方

