<h1 id="Title">Stella TTS Based on VITS</h1>

<h2 id="Contents">Contents</h2>

- [Update](#Update)
- [Introduction](#Introduction)
- [MoeGoe](#MoeGoe)
- [Models](#Models)
  - [Shiki Natsume](#Natsume)
  - [Chipanese Bilingual Model](#Bilingual)
  - [Café Stella and the Reaper's Butterflies](#Stella)
  - [Yosuga No Sora](#Yosuga)
  - [Bishojo Mangekyo](#Mangekyo)
  - [Genshin](#Genshin)
  - [A Certain Scientific Railgun](#Railgun)
- [Contact](#Contact)
- [References](#References)

<h2 id="Update">Update</h2>

- `japanese_triphone_cleaners` is available. 

<h2 id="Introduction">Introduction</h2>

Just have some fun...

The datasets and models are only for research use, NOT commercial!

<h2 id="MoeGoe">MoeGoe</h2>

You can run my models on [MoeGoe](https://github.com/CjangCjengh/MoeGoe) developed by [CjangCjengh](https://github.com/CjangCjengh)! Please first read the instructions of MoeGoe
and then download my models and corresponding configuration files.

<h2 id="Models">Models</h2>

---

<h3 id="Natsume">Shiki Natsume</h3>

![triphone](assets/triphone.png)

- Description

To further utilize the contextual information of the text, I wrote a **physiscal triphone** cleaners for Japanese. For more details about triphone, refer to [this material](http://sap.ist.i.kyoto-u.ac.jp/dictation/doc/phone_m.pdf).

Raw text:
```
さあ、はりきって行きましょう。
```

Phonemes:
```
s a a,h a r i k i Q t e i k i m a ʃ o o.
```

Triphones (physical):
```
s+a s-a+a a-a,h+a h-a+r a-r+i r-i+k i-k+i k-i+Q i-Q+t Q-t+e t-e+i e-i+k i-k+i k-i+m i-m+a m-a+ʃ a-ʃ+o ʃ-o+o o-o.
```

The following 2 speakers are supported.

|Name|ID|
 |-|-|
 |四季ナツメ|0|
 |司波深雪|1|

- Model:

- Configuration file:

- Demo:

---

<h3 id="Bilingual"> Chipanese Bilingual Model</h3>

![chipanese](assets/gugong.png)

- Description

I modified the Japanese cleaner and conbined it with a Chinese cleaner into a bilingual one, called "Chipanese cleaner"! 
The training data are from [Genshin](https://zh.moegirl.org.cn/%E5%8E%9F%E7%A5%9E), [Café Stella and the Reaper's Butterflies](https://zh.moegirl.org.cn/%E6%98%9F%E5%85%89%E5%92%96%E5%95%A1%E9%A6%86%E4%B8%8E%E6%AD%BB%E7%A5%9E%E4%B9%8B%E8%9D%B6) and [Kami-sama no You na Kimi e](https://zh.moegirl.org.cn/%E7%8C%AE%E7%BB%99%E7%A5%9E%E6%98%8E%E8%88%AC%E7%9A%84%E4%BD%A0).
For more information, please refer to this repo: [VITS-Bilingual](https://github.com/Francis-Komizu/VITS-Bilingual).

MoeGoe is NOT supported currently!

The following 2 speakers are supported.

|Name|ID|
 |-|-|
 |四季ナツメ|0|
 |派蒙|1|
 
- Model

- Configuration file

- Demo
  - Colab: [VITS (中日双语)](https://colab.research.google.com/drive/1SjWrj93oLPIFuqLUtye5Kv1Yf6FiCcYz?usp=sharing)
  - BILIBILI: [基于VITS的中日双语语音合成模型](https://www.bilibili.com/video/BV1PG411t7k4?spm_id_from=333.999.0.0)

---

<h3 id="Stella">Café Stella and the Reaper's Butterflies</h3>

![cafe stella](assets/stella.png)

- Description

 |Name|ID|
 |-|-|
 |四季ナツメ|0|
 |明月栞那|1|
 |墨染希|2|
 |火打谷愛衣|3|
 |汐山涼音|4|

- Model: 
  - [Google Drive (380 epochs)](https://drive.google.com/file/d/1WymtQdT0hQwUfzDIAbiQ3d7kDl5Y-aW7/view?usp=sharing)
  - [百度网盘 (198 epochs) 提取码0721](https://pan.baidu.com/s/1jfJ5vH9KNzZu10ualhNHjQ)

- Configuration file: 
  - [Google Drive](https://drive.google.com/file/d/18ly18hVT8jvgyKbLl7qqqBAaV7Fwkrp5/view?usp=sharing)
  - [百度网盘 提取码0721](https://pan.baidu.com/s/1uxP5vGBeNwd4UpPLkQnimA)

- Demo
  - Colab: [VITS (星光咖啡馆)](https://colab.research.google.com/drive/1nKa-l15f_talGvIwPmKTLYwwaE1Mztjg?usp=sharing)
  - BILIBLI: [基于VITS的星光咖啡馆5人语音合成模型](https://www.bilibili.com/video/BV1ra411P7CA?share_source=copy_web&vd_source=630b87174c967a898cae3765fba3bfa8)

---

<h3 id="Yosuga">Yosuga No Sora</h3>

![yosuga no sora](assets/yosuga.png)

- Description

|Name|ID|
|-|-|
|春日野穹|0|
|天女目瑛|1|
|依媛奈緒|2|
|渚一葉|3|
|春日野悠 (reserved)|4|

- Model: 
  - [Google Drive (600 epochs)](https://drive.google.com/file/d/1gaNtg4XVx0Eo4RC3gScHc3dNBWhoVdxv/view?usp=sharing)

- Configuration file: 
  - [Google Drive](https://drive.google.com/file/d/1KzwZvwdKTXLpMIQ96Q1FXP_bdEyb-in5/view?usp=sharing)

- Demo
  - Colab: [VITS (缘之空)](https://colab.research.google.com/drive/1FeuXBF_XXjYiEI11Y9UQW7YBfUZFJZbc?usp=sharing)
  - AcFun: [基于VITS的缘之空4人语音合成模型 (完整视频)](https://www.acfun.cn/v/ac36752427)
  - BILIBILI: [基于VITS的in solitude, where we are least alone语音合成模型 (阉割视频)](https://www.bilibili.com/video/BV1SW4y1b7Vt?spm_id_from=333.999.0.0&vd_source=017d04cd0542838d46958fe808b04d97)

---

<h3 id="Mangekyo">Bishojo Mangekyo</h3>

![mangekyo](assets/renge.png)

- Description

|Name|ID|
|-|-|
|蓮華|0|
|篝ノ霧枝|1|
|沢渡雫|2|
|亜璃子|3|
|灯露椎|4|
|覡夕莉|5|

- Model:
  - [Google Drive (715 epochs)](https://drive.google.com/file/d/1_0EyLIo5WwpAXycoyQWLpxszmsSN4MyO/view?usp=sharing)

- Configuration file:
  - [Google Drive](https://drive.google.com/file/d/1rLvi8ydtnJn-hSGi1v-p9qE2JhgcpsZ6/view?usp=sharing)

- Demo
  - Colab: [VITS (美少女万华镜)](https://colab.research.google.com/drive/1eFmnzUU8OGMlKwFw4OJG23CmawF1_zKh?usp=sharing)
  - AcFUN: [基于VITS的美少女万华镜语音合成模型](https://www.acfun.cn/v/ac36911138)

---

<h3 id="Genshin">Genshin</h3>

![genshin](assets/genshin.jpg)

- Description

Both single speaker model of Paimon and multi-speaker model of 46 characters will be supported!

- Model: 
  - Google Drive: [Paimon]()
  - Google Drive: [46 characters]()

- Configuration file: 
  - Google Drive: [Paimon]()
  - Google Drive: [46 characters]()

- Demo
  - Colab: [Paimon](https://colab.research.google.com/drive/1HDV84t3N-yUEBXN8dDIDSv6CzEJykCLw#scrollTo=oiPvCIJ_MHot)
  - BILIBILI: [派蒙Vtuber出道计划——基于AI深度学习VITS和VSeeFace的派蒙语音合成/套皮](https://www.bilibili.com/video/BV16G4y1B7Ey?share_source=copy_web&vd_source=630b87174c967a898cae3765fba3bfa8)
  - Colab: [46 characters]()
  - BILIBILI: on the road-map
  
---

<h3 id="Railgun">A Certain Scientific Railgun (collecting data...)</h3>

![railgun](assets/railgun.png)

- Characters

|Name|ID|Name|ID|
|-|-|-|-|
|上条当麻|0|削板軍覇|7|
|一方通行|1|御坂妹|8|
|垣根帝督|2|最終信号|9|
|御坂美琴|3|白井黒子|10|
|麦野沈利|4|佐天涙子|11|
|食蜂操祈|5|飾利初春|12|
|正体不明|6|インデックス|13|

- Model: 

- Configuration file: 

- Demo

<h2 id="Contact">Contact</h3>

QQ: 2235306122

BILIBILI: [Francis-Komizu](https://space.bilibili.com/636704927)

<h2 id="References">References</h3>

[Original code](https://github.com/jaywalnut310/vits)

[Reference code](https://github.com/CjangCjengh/vits)

[Triphone](http://sap.ist.i.kyoto-u.ac.jp/dictation/doc/phone_m.pdf)
