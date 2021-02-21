# FontChinese7x7

上古神器 III : 7x7像素点阵中文字体

想要在低分辨率屏幕上显示中文, 却发现中文字体实在是太大?

找了全网发现字体库最小也只有12x12?

甚至是好不容易找到了一个8x8字体, 结果发现字体收费且明确说明不得以任何形式嵌入到软件当中?

那就让这个项目来解决你的问题!

# 这是什么?

这个项目提供了一个叫“观致”的字体, 该字体存在于早期年代的点阵屏当中, 现已非常罕见.

该字体内置了7x7的中文点阵字体, 能够让中文字体在7x7下依然有着良好的可读性.

其他内容不需要多说想必大家也都知道了.

例如可以拿来作为报错信息:

![7x7报错测试](test1.png)

又例如可以拿来作为提示信息:

![7x7提示测试](test2.png)

更甚至是可以拿来做RPG游戏的相关文本内容:

![7x7游戏内容测试](test3.png)

# 关于“观致”字体版权

这是一款非常老的字体, 预估已经有15-20多岁的年龄了.

因为这个字体实在是太老, 互联网上与该字体相关的页面均在2005-2010年左右, 几乎全部404, 具体的版权信息难以知晓. 

但根据字体文件中的属性信息, 该字体版权方为“北京中易中标电子信息技术有限公司(Beijing Zhongyi Electronic Co., Ltd.)”, 并宣称“这是日文字体Misaki基础上补充的”.

本人已无渠道追溯该字体文件的原始出处, 因此处于学习和研究的目的, 将该字体文件公开在了这里, 目的是避免这个字体消失在互联网上.

若该项目存在字体侵权, 希望版权方能够主动联系我, 我会在第一时间内将该项目撤下.

# 特殊提示

项目中的脚本使用了Python27+Windows GDI对字体进行7x7取模.

因为Windows10下微软对GDI有抗锯齿, 且本人并不知道如何关掉这个功能, 因此该脚本并不能完美兼容Windows10及以上版本操作系统.

建议使用Windows7虚拟机来运行该脚本以达到最好的取模效果.

当然, 如果你知道如何解决这个问题, 那么非常欢迎提出一个Pull Requests!

# 项目版权

除字体文件版权无法知晓外, 代码均为MIT License.

原字体文件的作者依旧保留对该字体文件的版权.