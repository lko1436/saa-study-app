# <h1 class="exam-header">🏆 第一章：VPC 網路 20 題考古實戰</h1>

這 20 題是從 SAA-C03 核心題庫中精煉出來的，請每一題都先在腦中想出那個「秘密基地」的比喻。

---

### **1. 關於公有子網路 (Public Subnet)**
**Q：你正在設定一個新的 VPC。你已經建立了一個子網路，並在裡面放了一台 EC2，且給了它 Public IP。但你發現你還是連不到這台電腦，你還缺什麼？**
* **A.** 一個 NAT Gateway。
* **B.** 建立一個 Internet Gateway (IGW) 並將子網路的路由表指向它。
* **C.** 建立一個 Virtual Private Gateway。
* **D.** 將 EC2 換成彈性 IP (EIP)。
<details><summary>點擊看解析</summary><b>答案：B</b>。
沒有大門 (IGW)，Public IP 也沒用。Public Subnet 的定義就是「有路通往 IGW」。</details>

---

### **2. 安全性配置：黑名單**
**Q：你的網站正受到特定 IP 位址的惡意爬蟲攻擊，你需要立即封鎖該 IP。你該在哪裡設定？**
* **A.** Security Group。
* **B.** Network ACL (NACL)。
* **C.** WAF。
* **D.** Internet Gateway。
<details><summary>點擊看解析</summary><b>答案：B</b>。
Security Group 只有「Allow」，沒有「Deny」。要擋掉特定壞人，必須在 NACL 寫黑名單。</details>

---

### **3. NAT Gateway 的位置**
**Q：為了讓 Private Subnet 的執行個體可以下載系統補丁，你決定使用 NAT Gateway。你應該把 NAT Gateway 放在哪裡？**
* **A.** Private Subnet 內。
* **B.** Public Subnet 內。
* **C.** VPC 圍牆外面。
* **D.** 辦公室地端。
<details><summary>點擊看解析</summary><b>答案：B</b>。
NAT Gateway 本身需要連上 Internet，所以它必須待在有大門的 Public Subnet。</details>

---

### **4. 路由表 (Route Table) 的邏輯**
**Q：在 VPC 中，如果子網路的路由表沒有任何目標為 0.0.0.0/0 (Internet) 的路徑，這代表什麼？**
* **A.** 它是公有子網路。
* **B.** 它是私有子網路。
* **C.** 這個 VPC 壞掉了。
* **D.** 這台電腦沒有 IP。
<details><summary>點擊看解析</summary><b>答案：B</b>。
沒有指向大門的路，就是「私有子網路 (Private Subnet)」。</details>

---

### **5. IP 保留規則**
**Q：你在一個 /24 的子網路中 (總共 256 個 IP)，實際上可以分配給資源使用的 IP 有幾個？**
* **A.** 256。
* **B.** 254。
* **C.** 251。
* **D.** 250。
<details><summary>點擊看解析</summary><b>答案：C</b>。
AWS 固定保留 5 個 IP (256 - 5 = 251)。</details>

---

### **6. 安全組的「記性」(Stateful)**
**Q：你在 Security Group 的 Inbound 規則開啟了 Port 80 (允許進來)。你還需要手動開啟 Outbound 規則讓資料傳出去嗎？**
* **A.** 需要，因為安全組進出分開。
* **B.** 不需要，因為安全組是 Stateful (有狀態)。
* **C.** 需要，除非使用 NACL。
* **D.** 不需要，因為 AWS 會自動偵測流量。
<details><summary>點擊看解析</summary><b>答案：B</b>。
Security Group 有記性，你讓它進來，它就自動會讓你出去。</details>

---

### **7. 跨帳戶連線：VPC Peering**
**Q：公司有兩個不同 AWS 帳戶的 VPC，現在需要這兩個 VPC 內部的私有 IP 能互相通訊，且要最穩定的內部連線。**
* **A.** 使用 Internet Gateway 連接。
* **B.** 建立 VPC Peering。
* **C.** 建立 Site-to-Site VPN。
* **D.** 使用 NAT Gateway。
<details><summary>點擊看解析</summary><b>答案：B</b>。
VPC Peering 可以在不同帳號間建立天橋，流量不走 Internet，最安全穩定。</details>

---

### **8. S3 存取的成本優化**
**Q：私有區的 EC2 需要存取 S3 倉庫。為了節省資料處理費且不經過 Internet，該怎麼做？**
* **A.** 建立 NAT Gateway。
* **B.** 建立 S3 Gateway Endpoint。
* **C.** 建立 Interface Endpoint。
* **D.** 使用 Direct Connect。
<details><summary>點擊看解析</summary><b>答案：B</b>。
S3 專屬的 Gateway Endpoint 是「免費」且「不出門」的最佳選擇。</details>

---

### **9. 高可用性的網路規劃**
**Q：為了達成高可用性 (High Availability)，你在設計 VPC 時應該怎麼做？**
* **A.** 所有的子網路都放在同一個可用區 (AZ)。
* **B.** 在不同的可用區 (AZ) 分別建立子網路。
* **C.** 建立兩個 Internet Gateway。
* **D.** 使用更大的 IP 區段。
<details><summary>點擊看解析</summary><b>答案：B</b>。
不要把雞蛋放在同一個籃子，子網路要跨 AZ 擺放。</details>

---

### **10. 混合雲：穩定連線**
**Q：公司需要一條從本地機房到 AWS 的連線，要求「一致的網路效能」且「完全不走公共網際網路」。**
* **A.** Site-to-Site VPN。
* **B.** Direct Connect (DX)。
* **C.** Transit Gateway。
* **D.** Client VPN。
<details><summary>點擊看解析</summary><b>答案：B</b>。
只要看到「一致效能」、「不走 Internet」，就是實體專線 Direct Connect。</details>

---

### **11. VPC Peering 的限制**
**Q：你建立了 VPC A 與 VPC B 的 Peering 連線。VPC A 的 CIDR 是 10.0.0.0/16，VPC B 也是 10.0.0.0/16。請問會發生什麼事？**
* **A.** AWS 會自動處理 IP 衝突。
* **B.** Peering 連線會建立失敗，因為 CIDR 範圍重疊 (Overlapping)。
* **C.** 只有一半的電腦可以連線。
* **D.** 必須使用 NAT Gateway 來橋接。
<details><summary>點擊看解析</summary><b>答案：B</b>。
考古題大重點：<b>要建立 Peering，兩個 VPC 的 IP 範圍絕對不能重疊</b>。</details>

---

### **12. 連接多個 VPC 的最佳方案**
**Q：公司規模擴大，現在有 50 個不同的 VPC 需要互相通訊。手動建立 Peering 太麻煩了，你該建議使用什麼？**
* **A.** VPC Endpoint Service。
* **B.** Transit Gateway。
* **C.** 更多更多的 Internet Gateway。
* **D.** 使用 Site-to-Site VPN 把大家串起來。
<details><summary>點擊看解析</summary><b>答案：B</b>。
當 VPC 數量很多時，<b>Transit Gateway</b> 就像中央轉運站，管理起來最簡單。</details>

---

### **13. NACL 的規則順序**
**Q：在 NACL 設定中，你有兩條規則：規則 100 是「允許所有流量」，規則 90 是「拒絕所有流量」。請問結果為何？**
* **A.** 允許所有流量，因為 100 比較大。
* **B.** 拒絕所有流量，因為 NACL 會從小號碼規則開始執行。
* **C.** 兩者抵銷。
* **D.** 系統會報錯。
<details><summary>點擊看解析</summary><b>答案：B</b>。
NACL 是<b>按號碼順序執行 (Smallest number first)</b>。一旦符合規則 90 (拒絕)，後面的 100 就不會看了。</details>

---

### **14. 臨時上網方案：Egress-Only Internet Gateway**
**Q：你在使用 IPv6。你想要讓 Private Subnet 的執行個體可以上網，但外面的人不能進來。IPv4 用 NAT Gateway，那 IPv6 該用什麼？**
* **A.** 還是用 NAT Gateway。
* **B.** Egress-Only Internet Gateway。
* **C.** Internet Gateway 2.0。
* **D.** VPC Peering。
<details><summary>點擊看解析</summary><b>答案：B</b>。
這是 IPv6 專屬的「單向大門」，效果跟 NAT Gateway 一樣，但專門給 IPv6 用。</details>

---

### **15. 辦公室緊急備援連線**
**Q：公司已經有一條 Direct Connect (DX) 專線，但為了防止挖土機挖斷線路，需要一個「便宜且快速」的備援方案。**
* **A.** 再拉一條 Direct Connect。
* **B.** Site-to-Site VPN (透過 Internet)。
* **C.** 搬家到 AWS 機房旁邊。
* **D.** 使用雪球 (Snowball) 運送資料。
<details><summary>點擊看解析</summary><b>答案：B</b>。
VPN 雖然不穩，但當作 DX 斷線時的<b>便宜備援 (Backup)</b> 是最常見的考題解法。</details>

---

### **16. 安全組 (SG) 的對象來源**
**Q：在 Security Group 規則中，除了填寫 IP 範圍 (0.0.0.0/0)，你還可以填寫什麼作為來源？**
* **A.** 使用者的姓名。
* **B.** 另一個 Security Group 的 ID。
* **C.** 伺服器的 MAC 位址。
* **D.** 基地台的名稱。
<details><summary>點擊看解析</summary><b>答案：B</b>。
這叫「引用 (Referencing)」。例如：只允許來自「Web-SG」的人連線到「DB-SG」。</details>

---

### **17. 預設 VPC 的行為**
**Q：你剛開通一個新的 AWS 帳號，AWS 自動幫你建好了一個「預設 VPC」。請問它的子網路預設是？**
* **A.** 全部都是 Private。
* **B.** 全部都是 Public (已經連好 IGW)。
* **C.** 一半 Public 一半 Private。
* **D.** 裡面沒有子網路。
<details><summary>點擊看解析</summary><b>答案：B</b>。
預設 VPC 是為了讓你快速上手，所以裡面的子網路預設都接好了大門 (IGW)。</details>

---

### **18. Bastian Host (跳板機) 的位置**
**Q：你需要遠端連線到 Private Subnet 裡的 Linux 伺服器進行維修，你會在 Public Subnet 放一台什麼機器？**
* **A.** NAT Gateway。
* **B.** Bastion Host (跳板機)。
* **C.** 資料庫備份機。
* **D.** 負載平衡器。
<details><summary>點擊看解析</summary><b>答案：B</b>。
<b>跳板機 (Bastion Host)</b> 是一台放在 Public 區的小機器，你先連到它，再從它連進去 Private 區。</details>

---

### **19. Flow Logs (流量日誌)**
**Q：老闆想知道最近有哪些 IP 一直在嘗試連線到你的 VPC，但被拒絕了。你該開啟什麼功能？**
* **A.** CloudWatch 日記。
* **B.** VPC Flow Logs。
* **C.** S3 存取紀錄。
* **D.** Inspector。
<details><summary>點擊看解析</summary><b>答案：B</b>。
<b>VPC Flow Logs</b> 記錄了所有進入或離開網路介面的 IP 流量。看到「網路流量紀錄」就選它。</details>

---

### **20. 混合雲：多點連線**
**Q：公司在台北、台中、高雄都有分公司，想要全部都連到雲端的 VPC。最簡單的管理方式是？**
* **A.** 蓋三條 Direct Connect。
* **B.** AWS VPN CloudHub。
* **C.** 建立一個巨大的 Peering 網。
* **D.** 叫員工用手機熱點。
<details><summary>點擊看解析</summary><b>答案：B</b>。
<b>VPN CloudHub</b> 可以讓多個站點透過 VPN 集中連到一個虛擬閘道，適合這種多點連線場景。</details>