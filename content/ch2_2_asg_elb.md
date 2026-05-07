# <h1 class="exam-header">2-2 Auto Scaling 與 負載平衡 (ELB)</h1>

當基地客人變多時，我們需要兩樣工具來幫忙：**ELB (分流員)** 與 **ASG (自動增援部隊)**。

---

### 1. 負載平衡器 ELB (社區分流員)
**ELB (Elastic Load Balancing)** 就像站在門口的分流員。他會把客人（流量）平均分配給每一台電腦（EC2），不讓某一台累死。

考試最常考這兩種 ELB 的選擇：
* **ALB (Application Load Balancer):** * **專長：** 看得懂「內容」。
    * **用法：** 它可以根據網址（例如：`/video` 去 A 電腦，`/images` 去 B 電腦）來分流。
    * **關鍵字：** HTTP/HTTPS、Layer 7、網址路徑分流。
* **NLB (Network Load Balancer):** * **專長：** 極速、處理海量連線。
    * **用法：** 它只看 IP 和 Port，速度最快，延遲最低。
    * **關鍵字：** TCP/UDP、極高頻寬、靜態 IP (Static IP)。



---

### 2. Auto Scaling Group / ASG (自動增援部隊)
當分流員（ELB）發現每一台電腦都滿載了，他會通知 **ASG**。
* **ASG 的工作：** 根據你設定的規則，自動幫你「加開」電腦，或者在半夜沒人時「關掉」電腦省錢。
* **健康檢查 (Health Check)：** 如果有一台電腦「當機」了，ASG 會直接把它「開除（殺掉）」，然後自動換一台新的給你。

---

### 3. 三種增援策略 (Scaling Policies)
* **Target Tracking (目標追蹤)：** * 就像設定恆溫空調。例如：維持 CPU 在 50%，高了就加機器，低了就減。
* **Step / Simple Scaling (階梯縮放)：** * 像警報器。如果 CPU 超過 80%，一次加 3 台機器。
* **Scheduled Scaling (預約縮放)：** * 就像百貨公司周年慶。你知道明天早上 10 點會有人潮，現在就設定好「明天 9:50 先開好 10 台等」。

---

### 📖 核心專有名詞 (Exam Keywords)
* **Elastic Load Balancing (ELB):** 負載平衡器（把流量分給多台機器）。
* **Auto Scaling Group (ASG):** 自動縮放群組（自動調整機器數量）。
* **Health Check:** 健康檢查（確認機器是否還活著）。
* **Desired Capacity:** 期望容量（你目前希望維持幾台機器）。

---

### 📝 快速複習
**Q：如果你今天經營一個電商網站，你想根據客人造訪的「網址內容」（例如 /shop 跟 /blog）把他們分給不同的伺服器處理，你應該選哪一種負載平衡器？**

<details>
<summary><b>點擊查看答案</b></summary>
<b>答案：ALB (Application Load Balancer)</b>。<br>
因為 ALB 是「聰明型」的分流員，它看得懂 HTTP 網址，能根據路徑 (Path-based routing) 來分流。
</details>