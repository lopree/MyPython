# 安装环境
> Mac OS 10.13.3系统, Anaconda 4.5.0以及`Python 3.6.5 :: Anaconda, Inc.`

# pip与源码安装的两种方式
> 无论哪一种方式都需要配置好Python环境：pip,six,numpy,wheel这些包

安装完pip后：
```
sudo pip install six numpy wheel
```
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
> 官网链接：`https://www.tensorflow.org/install/install_sources#prepare_environment_for_macos`<br>以及参考文章：<br>
http://aifuns.cc/2017/11/30/tensorflow-build-install-mac.html

克隆TensorFlow项目：<br>
```
git clone https://github.com/tensorflow/tensorflow

```
在`/Users/apple/`下将会生成`tensorflow`文件夹

**注意:**如果之前在anconda中安装了TensorFlow（可以使用`pip list`显示出是否安装），然后可以`pip uninstall tensorflow`卸载掉已经安装的tensorflow

1. 利用brew安装Google自家的`bazel`编译工具
```

brew install bazel

```
当出现这个时表示安装成功：
![bazel安装成功](http://ov443bcri.bkt.clouddn.com/bazel.png)

2. `cd tensorflow`进入文件夹，`./configure`开始配置文件--只需要`一路回车`就可以,据说是MBP不支持这些

3. 配置完文件后，漫长的编译过程<br>
以下语句为了TensorFlow（仅仅支持CPU）编译生成 pip package ：

```
bazel build --config=opt //tensorflow/tools/pip_package:build_pip_package
```

***注意:*** 可能出现Xcode问题，后面有解决方案。

4. 生成wheel文件
```
bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg
```
这里面的`/tmp/tensorflow_pkg`为生成的文件的存放路径，可以自行设定。

5. 安装wheel文件
```
cd /tmp/tensorflow_pkg
```
进入存放wheel的文件夹，
```
pip install wheel文件的名字
```

6. 测试

![](http://ov443bcri.bkt.clouddn.com/Tensflow%E7%A4%BA%E4%BE%8B.png   "Tensflow案例")

# Xcode问题
> 参考：`https://stackoverflow.com/questions/45276830/xcode-version-must-be-specified-to-use-an-apple-crosstool?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa`

当出现问题：
```
ERROR:/private/var/tmp/_bazel_Kakadu/3f0c35881c95d2c43f04614911c03a57/external/local_config_cc/BUILD:49:5: in apple_cc_toolchain rule @local_config_cc//:cc-compiler-darwin_x86_64: Xcode version must be specified to use an Apple CROSSTOOL.

ERROR: Analysis of target '//tensorflow_serving/sources/storage_path:file_system_storage_path_source_proto' failed; build aborted.

I've already tried to use bazel clean and bazel clean --expunge but it didn't help and still Bazel doesn't see my xcode(I suppose) but it's completely installed. I even reinstalled it to make sure that all works fine but the error isn't disappeared

Bazel version installed is Build label: 0.5.2-homebrew Build target: bazel-out/darwin_x86_64-opt/bin/src/main/java/com/google/devtools/build/lib/bazel/BazelServer_deploy.jar Build time: Thu Jul 13 12:29:40 2017 (1499948980) Build timestamp: 1499948980 Build timestamp as int: 1499948980 KakaduDevs-Mac-mini:serving Kakadu$
```
解决方案：
1. bazel clean --expunge
2. sudo xcode-select -s /Applications/Xcode.app/Contents/Developer
3. sudo xcodebuild -license
4. bazel clean --expunge
5. bazel build --config=opt //tensorflow/tools/pip_package:build_pip_package

