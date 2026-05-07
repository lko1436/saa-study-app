# <h1 class="exam-header">🏆 第二章：運算資源總結大會考</h1>

恭喜你讀完運算資源模組！這裡有 5 題針對考試核心邏輯的測驗，請思考後再點開解析。

---

### **Q1：省錢與彈性的權衡**
你的公司要在下個月舉辦為期 **3 天** 的快閃促銷活動，預計流量會是平常的 100 倍。你希望在活動期間「自動加開機器」來應付人潮，且活動一結束就關掉機器省錢。你該使用哪種組合？

A. 租用專屬主機 (Dedicated Hosts) + 手動調整數量  
B. 使用 Auto Scaling Group (ASG) 並設定 Target Tracking 策略  
C. 全部換成 Lambda 跑整個網站  
D. 買 3 年期的預留實體 (Reserved Instances)

<details>
<summary><b>點擊查看答案與解析</b></summary>
<b>正確答案：B</b><br>
<b>解析：</b> 關鍵字是「自動加開」與「活動結束省錢」。<b>ASG</b> 就是為了這種不定期流量設計的，Target Tracking 可以讓它根據負載自動增減。3 年預留或是專屬主機對 3 天活動來說太浪費且不具彈性。
</details>

---

### **Q2：分流員的選擇 (ALB vs NLB)**
你正在設計一個大型遊戲的後端，該遊戲使用 **TCP 協定**，且要求**極低延遲**與處理**每秒數百萬個連線**的能力。你該選擇哪一種負載平衡器？

A. Application Load Balancer (ALB)  
B. Network Load Balancer (NLB)  
C. Gateway Load Balancer (GWLB)  
D. Classic Load Balancer (CLB)

<details>
<summary><b>點擊查看答案與解析</b></summary>
<b>正確答案：B</b><br>
<b>解析：</b> 看到「極低延遲」、「海量連線」以及「TCP/UDP 協定」，首選一定是 <b>NLB</b>。ALB 是用來處理網址路徑分流（HTTP/HTTPS）的，速度稍慢於 NLB。
</details>

---

### **Q3：防止資料消失的危機處理**
有一位新手工程師誤用了 **Instance Store** 作為資料庫的儲存空間。今天因為底層硬體故障，該 EC2 執行個體被停止了。請問資料還在嗎？

A. 還在，重新啟動 (Start) 機器就會出現。  
B. 還在，但必須聯絡 AWS 客服幫忙掛載硬碟。  
C. 不在了，Instance Store 是臨時性的，關機或故障資料就會永久消失。  
D. 不在了，但可以從快照 (Snapshot) 自動恢復。

<details>
<summary><b>點擊查看答案與解析</b></summary>
<b>正確答案：C</b><br>
<b>解析：</b> 這是 EC2 最愛考的坑。<b>Instance Store (臨時儲存)</b> 只要遇到 Stop 或硬體故障，資料就掰掰了。重要資料應該放在 EBS（雲端硬碟）才安全。
</details>

---

### **Q4：懶人技術的選擇**
你公司有一個每天午夜需要執行一次的「產生報表」程式，每次執行大約需要 **20 分鐘**。你希望「完全不想管伺服器」，請問以下哪個方案最合適？

A. AWS Lambda  
B. AWS Fargate  
C. EC2 Spot Instance  
D. S3 Batch Operations

<details>
<summary><b>點擊查看答案與解析</b></summary>
<b>正確答案：B</b><br>
<b>解析：</b> 雖然 Lambda 也是不用管伺服器，但它有 <b>15 分鐘的限制</b>。你的任務需要 20 分鐘，所以會被中斷。這種情況要選 <b>Fargate</b>，它同樣是 Serverless (懶人方案)，但沒有時間限制。
</details>

---

### **Q5：機器擺放的位置 (Placement Groups)**
你有一群負責大數據運算的伺服器（例如 Kafka 叢集），你希望即便機房的某個**機架 (Rack) 壞掉**，也不要讓整組運算掛掉，你該選哪種置放方式？

A. Cluster Placement Group  
B. Partition Placement Group  
C. Spread Placement Group  
D. 隨機擺放

<details>
<summary><b>點擊查看答案與解析</b></summary>
<b>正確答案：B</b><br>
<b>解析：</b> <b>Partition (分區)</b> 專門為大數據設計，它把機器分組放在不同機架。如果一個機架故障，只會影響其中一小部分資料，其他分區還能運作。
</details>