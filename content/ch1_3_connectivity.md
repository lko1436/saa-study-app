# 🌉 1-3 道路建設：如何把不同的基地連起來？

當你有兩個基地，或是想從家裡連進基地時，你需要蓋「路」。

---

### 1. 家裡連到雲端：VPN 與 專線 (Direct Connect)
* **VPN (走一般大馬路)：**
    * **特性：** 便宜、快（幾分鐘就蓋好）。
    * **缺點：** 走公共網路，流量大時會塞車、不穩定。
* **Direct Connect / DX (專屬地下道)：**
    * **特性：** 實體線路連到 AWS，極度穩定、頻寬超大。
    * **缺點：** 很貴，要等好幾週讓電信商拉線。



---

### 2. 基地連基地：VPC Peering 與 Transit Gateway
* **VPC Peering (蓋天橋)：**
    * **特性：** 一對一連線。
    * **限制：** 不支援「傳遞」 (No Transitive)。A 連 B，B 連 C，A 不能透過 B 去 C。
* **Transit Gateway / TGW (大型轉運站)：**
    * **特性：** 中心化管理。幾百個 VPC 都能連進來，管理最簡單。



---

### 3. 免費的秘密小門：VPC Endpoints
如果你在基地裡想去 S3 拿檔案，但不想走出大門去曬太陽（不經過公共網路）：
* **Gateway Endpoint：** * **重點：** **免費**。
    * **支援對象：** 只有 **S3** 與 **DynamoDB**。
* **Interface Endpoint：** * **重點：** **要錢**。
    * **支援對象：** 除了上面兩個以外的大部分服務。

---

### 📝 隨堂小測驗
**Q：如果你公司要求這條路必須「極度穩定」，而且每天要傳好幾 TB 的超大檔案，你應該推薦哪種連線方式？**

<details>
<summary><b>點擊查看答案</b></summary>
<b>答案：Direct Connect (DX)</b>。<br>
因為只有實體專線能提供「一致、穩定」的感覺，不會像一般馬路（VPN/公網）一樣忽快忽慢。
</details>

---

### ✍️ 筆記本重點摘要

1. **連線方案對比：**
   * **VPN：** 便宜、走公網、適合小流量/緊急用。
   * **Direct Connect (DX)：** 貴、實體線路、適合穩定大流量。

2. **跨 VPC 連線：**
   * **VPC Peering：** 一對一，不能轉彎（A->B->C 不通）。
   * **Transit Gateway：** 星狀結構，管理幾百個 VPC 最強。

3. **VPC Endpoints (秘密通道)：**
   * **Gateway 型：** 免費，限 **S3** 與 **DynamoDB**。
   * **Interface 型：** 貴，其他服務用。

4. **考試直覺：**
   * 看到「不想經過 Internet 抓 S3」 ➔ 選 **Gateway Endpoint**。
   * 看到「跨區域連接數百個 VPC」 ➔ 選 **Transit Gateway**。