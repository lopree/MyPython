# 安装环境
> Mac OS 10.13.3系统, Anaconda 4.5.0以及`Python 3.6.5 :: Anaconda, Inc.`

# pip与源码安装的两种方式
## pip安装
1. 在ancoda下安装，最后会导致`SSE4.2`以及`AVX`编译问题--虽然机器上有但是不会运用在TensorFlow上。<br>
问题显示：

```
W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.1 instructions, but these are available on your machine and could speed up CPU computations.
W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.2 instructions, but these are available on your machine and could speed up CPU computations.
W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX instructions, but these are available on your machine and could speed up CPU computations.
W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX2 instructions, but these are available on your machine and could speed up CPU computations.
W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use FMA instructions, but these are available on your machine and could speed up CPU computations.

```

2. 编译速度：pip安装的远远不如源码安装编译的速度

## 源码安装
> 官网链接：`https://www.tensorflow.org/install/install_sources#prepare_environment_for_macos`

克隆TensorFlow项目：<br>
```
git clone https://github.com/tensorflow/tensorflow

```
在`/Users/apple/`下将会生成`tensorflow`文件夹

1. 利用brew安装Google自家的`bazel`编译工具
```

brew install bazel

```

![bazel安装成功](http://ov443bcri.bkt.clouddn.com/bazel.png)