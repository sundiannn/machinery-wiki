# 電機機械 Wiki 目錄

> 每次新增、改名或刪除頁面時，AI 都要同步更新本頁（見 AGENTS.md 第 4.4 節）。
> 狀態：draft（初稿）／checked（已通過 lint 與使用者確認）

## 來源摘要

| 章 | 頁面 | 狀態 |
|---|---|---|
| Ch.1 | [電機機械原理導論](sources/ch01.md) | 已 ingest（2026-11-23） |
| Ch.2 | [變壓器](sources/ch02.md) | 已 ingest（2026-11-23） |
| Ch.3 | [交流電機基礎](sources/ch03.md) | 已 ingest（2026-11-23） |
| Ch.4 | [同步發電機](sources/ch04.md) | 已 ingest（2026-11-23） |
| Ch.5 | [同步電動機](sources/ch05.md) | 已 ingest（2026-11-23） |

## 概念頁

### 總覽
- [電機](concepts/electric-machines.md)：在機械能與電能之間互相轉換的裝置
- [磁場四大原理](concepts/four-magnetic-principles.md)：變壓器、電動機、發電機作用的共同基礎（全課地圖）
- [初學者名詞小抄](concepts/beginner-glossary.md)：定子、轉子、場電流、阻抗、功因、虛功率等名詞的一句話解釋

### 基礎物理
- [旋轉運動](concepts/rotational-motion.md)：角速度、轉矩、$P=\tau\omega$

### 磁與鐵心
- [磁場強度與導磁係數](concepts/magnetic-field-and-permeability.md)：電流產生 $H$，材料決定 $B$
- [磁路](concepts/magnetic-circuit.md)：把磁通路徑當電路分析，氣隙佔大部分磁阻
- [磁化曲線](concepts/magnetization-curve.md)：鐵會飽和，電機運轉在膝點附近
- [鐵損](concepts/core-losses.md)：磁滯損＋渦流損，用疊片與矽鋼降低

### 電磁感應與力
- [法拉第定律](concepts/faraday-law.md)：磁通變化感應電壓（變壓器作用）
- [載流導線受力](concepts/induced-force.md)：磁場中的電流受力（電動機作用）
- [運動導體的感應電壓](concepts/motional-voltage.md)：導線在磁場中運動產生電壓（發電機作用）

### 變壓器（Ch.2）
- [變壓器](concepts/transformer.md)：交流電換電壓、頻率不變；本章地圖
- [交流功率](concepts/ac-power.md)：實功率、虛功率、視在功率、功率因數
- [理想變壓器](concepts/ideal-transformer.md)：電壓比 $a$、電流比 $1/a$、阻抗乘 $a^2$
- [實際變壓器](concepts/real-transformer.md)：漏磁通與激磁電流
- [變壓器等效電路](concepts/transformer-equivalent-circuit.md)：用電阻與電抗表示所有非理想效應
- [開路與短路測試](concepts/oc-sc-test.md)：兩個實驗求出等效電路參數
- [標么值](concepts/per-unit-system.md)：用「基準值的幾倍」表示電量
- [電壓調整率與效率](concepts/voltage-regulation-and-efficiency.md)：負載下電壓掉多少、功率送出多少
- [分接頭](concepts/transformer-taps.md)：小幅調整匝數比
- [自耦變壓器](concepts/autotransformer.md)：繞組串接，容量大但無隔離
- [三相變壓器](concepts/three-phase-transformer.md)：Y、Δ 四種接法

### 交流電機基礎（Ch.3）
- [交流電機](concepts/ac-machines.md)：定子、轉子、同步與感應兩大類；本章地圖
- [旋轉線圈](concepts/rotating-loop.md)：最簡單的交流發電機，電壓 $\phi\omega\sin\omega t$
- [旋轉磁場](concepts/rotating-magnetic-field.md)：三相電流產生大小固定、持續旋轉的磁場
- [電頻率與轉速](concepts/electrical-frequency-and-speed.md)：$f_{se} = n_{sm}P/120$
- [氣隙磁通分布](concepts/air-gap-flux-distribution.md)：分布繞組讓磁通接近正弦
- [交流電機的感應電壓](concepts/ac-induced-voltage.md)：$E_A = \sqrt2\pi N_C\phi f$
- [交流電機的感應轉矩](concepts/ac-induced-torque.md)：$\tau = k\mathbf{B}_R\times\mathbf{B}_{net}$
- [電機損失與功率流](concepts/machine-losses-and-power-flow.md)：四類損失與功率流程圖
- [速度調整率](concepts/speed-regulation.md)：電動機轉速隨負載的變化

### 同步發電機（Ch.4）
- [同步發電機](concepts/synchronous-generator.md)：轉子電磁鐵被帶著轉，在定子產生三相電；本章地圖
- [內生電壓](concepts/internal-generated-voltage.md)：$E_A = K\phi\omega$，由場電流控制
- [同步機等效電路](concepts/synchronous-equivalent-circuit.md)：電樞反應、同步電抗、相量圖
- [同步機的功率與轉矩](concepts/synchronous-power-and-torque.md)：$P = 3V_\phi E_A\sin\delta/X_S$
- [同步機參數測試](concepts/synchronous-machine-tests.md)：開路、短路、直流測試與短路比
- [發電機單獨運轉](concepts/generator-operating-alone.md)：負載功因如何影響端電壓

### 同步電動機（Ch.5）
- [同步電動機](concepts/synchronous-motor.md)：轉子追著旋轉磁場跑；和同步發電機是同一台機器；本章地圖
- [同步電動機的轉矩與負載](concepts/synchronous-motor-torque-speed.md)：轉速固定、脫出轉矩、滑動極
- [V 曲線](concepts/v-curve.md)：場電流決定欠激或過激、吸收或供給虛功率
- [功率因數校正](concepts/power-factor-correction.md)：過激同步電動機降低輸電損失、同步電容器
- [同步電動機的啟動](concepts/synchronous-motor-starting.md)：降頻、外部原動機、阻尼繞組

### 第一台電機（Ch.1）
- [線性直流機](concepts/linear-dc-machine.md)：同一台機器可當電動機也可當發電機

## 例題引導
- [例 1-2 氣隙的磁阻](examples/ch01-air-gap.md)（Ch.1）
- [例 1-10 線性直流機](examples/ch01-linear-machine.md)（Ch.1）
- [例 2-1 輸電要不要變壓器](examples/ch02-transmission.md)（Ch.2）
- [例 2-2 開路／短路測試求等效電路](examples/ch02-oc-sc-test.md)（Ch.2）
- [例 3-2 簡單的兩極發電機](examples/ch03-simple-generator.md)（Ch.3）
- [例 4-1 由測試求同步電抗](examples/ch04-parameter-test.md)（Ch.4）
- [例 4-3 功率因數對端電壓的影響](examples/ch04-power-factor.md)（Ch.4）
- [例 5-3 用同步電動機改善功因](examples/ch05-power-factor-correction.md)（Ch.5）

## 問答

（尚無）
