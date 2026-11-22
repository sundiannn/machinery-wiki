---
title: 變壓器
en: Transformer
aliases: [變壓器, transformer, 內鐵式, 外鐵式, 比壓器, 比流器, PT, CT]
chapters: [ch02]
sources: [sources/ch02.md]
updated: 2026-11-23
status: draft
---

# 變壓器（Transformer）

## 一句話說明
變壓器把交流電從一個電壓「換」成另一個電壓，頻率不變；它沒有會動的零件，兩組線圈之間只靠鐵心裡的磁通傳遞能量。

## 白話解釋
發電廠到你家之間，電要走很遠。用高電壓輸送，電流就小，電線上浪費的能量就少；到了家附近再把電壓降下來，用起來才安全。變壓器就是負責「升壓」和「降壓」的設備〔講義 p.1–2〕〔AI 補充〕。

## 正式內容
**定義與構造**〔講義 p.1–3〕
- 兩組以上的線圈繞在共同的鐵磁性鐵心上，線圈之間（通常）不直接相連，唯一的連結是鐵心中的共同磁通
- 接電源的叫**一次繞組（primary winding）**，接負載的叫**二次繞組（secondary winding）**，若有第三組叫三次繞組
- 鐵心有兩種構造：**內鐵式（core form）**——長方形鐵心，繞組繞在兩側；**外鐵式（shell form）**——三腳鐵心，繞組繞在中間腳
- 鐵心由彼此絕緣的薄疊片構成，以減少渦流（見[鐵損](core-losses.md)）
- 低壓繞組放在最內側、兩繞組疊繞：使高壓繞組對鐵心的絕緣比較容易，也讓漏磁通少很多

**為什麼重要**〔講義 p.1–2〕
- 理想上只改變電壓準位，不改變傳送的功率：升壓時電流必須變小，才能讓輸入功率等於輸出功率
- 電力系統：發電 12～25 kV → 升壓到 110 kV～近 1000 kV 長距離低損耗輸電 → 降壓到 12～34.5 kV 配電 → 最低 120 V 供家庭、辦公室、工廠使用
- 加上變壓器後輸電損失大幅下降，見[例 2-1](../examples/ch02-transmission.md)

**依用途命名**〔講義 p.3–4〕

| 名稱 | 位置與功能 |
|---|---|
| 單位變壓器（unit transformer） | 接在發電機輸出，升壓到輸電電壓（110 kV 以上） |
| 變電變壓器（substation transformer） | 輸電線末端，降到配電電壓（2.3～34.5 kV） |
| 配電變壓器（distribution transformer） | 降到實際使用電壓（110、208、220 V 等） |
| 比壓器（PT） | 把高電壓取樣成成正比的低電壓，供量測 |
| 比流器（CT） | 產生遠小於但正比於一次電流的二次電流，供量測 |

前三種本質相同，只是用途不同〔講義 p.3〕。

## 本章地圖
1. 先學[理想變壓器](ideal-transformer.md)，以及需要的[交流功率](ac-power.md)
2. 再看[實際變壓器](real-transformer.md)與它的[等效電路](transformer-equivalent-circuit.md)，參數由[開路與短路測試](oc-sc-test.md)求得
3. 計算工具：[標么值](per-unit-system.md)
4. 性能指標：[電壓調整率與效率](voltage-regulation-and-efficiency.md)、調整用的[分接頭](transformer-taps.md)
5. 特殊形式：[自耦變壓器](autotransformer.md)、[三相變壓器](three-phase-transformer.md)

## 和其他概念的關係
- 運作原理是[法拉第定律](faraday-law.md)，即[磁場四大原理](four-magnetic-principles.md)中的「變壓器作用」
- 和[電機](electric-machines.md)關係密切，但沒有旋轉部件

## 出處
- [Ch.2 來源摘要](../sources/ch02.md)〔講義 p.1–4〕
