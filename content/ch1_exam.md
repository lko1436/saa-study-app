# <h1 class="exam-header">🏆 第一章：VPC 網路純血複習考 (精選 15 題)</h1>

這 15 題保證只考你學過的東西。如果題目提到「伺服器」，你就把它當成一台電腦；提到「檔案」，就把它當成一箱貨物。

---

### **1. 關於公有子網路的條件**
**Q：你建立了一個 VPC 與一個子網路。你想要讓這個子網路成為「公有子網路 (Public Subnet)」，除了分配 Public IP 給裡面的電腦，你還必須做什麼？**
* **A.** 建立一個 NAT Gateway。
* **B.** 建立 Internet Gateway (IGW) 並在路由表中加入一條 0.0.0.0/0 指向該 IGW。
* **C.** 建立一個 VPC Peering。
* **D.** 調整 Security Group 的規則。
<details><summary>💡 點擊看解析</summary><b>答案：B</b>。
<b>複習重點：</b> Public Subnet 的唯一定義就是：路由表有一條路通往 Internet Gateway。</details>

---

### **2. 安全組 (SG) 的基本特性**
**Q：你在 Security Group 的 Inbound (進入) 規則中允許了來自 0.0.0.0/0 的流量。請問 Outbound (出去) 規則會如何表現？**
* **A.** 你必須手動在 Outbound 增加規則，否則資料回不去。
* **B.** 安全組是 Stateful (有狀態的)，資料會自動被允許傳回使用者。
* **C.** 必須透過 NACL 才能讓資料傳回去。
* **D.** 只有給予電腦固定 IP 後，資料才能回傳。
<details><summary>💡 點擊看解析</summary><b>答案：B</b>。
<b>複習重點：</b> 安全組有記性（Stateful），進得來就一定出得去。</details>

---

### **3. 如何擋掉惡意 IP**
**Q：你發現某個特定 IP 位址不斷對你的電腦發動攻擊。你想要「拒絕 (Deny)」這個特定 IP 的存取，該在哪裡設定？**
* **A.** Security Group。
* **B.** Network ACL (NACL)。
* **C.** Internet Gateway。
* **D.** 路由表 (Route Table)。
<details><summary>💡 點擊看解析</summary><b>答案：B</b>。
<b>複習重點：</b> Security Group 只能設「允許」，只有 NACL 可以設定「拒絕 (Deny)」。</details>

---

### **4. NAT Gateway 的主要用途**
**Q：你的電腦放在私有子網路 (Private Subnet)，不希望外人連進來，但電腦需要上網下載系統更新。你該使用什麼？**
* **A.** Internet Gateway。
* **B.** NAT Gateway。
* **C.** VPC Peering。
* **D.** Direct Connect。
<details><summary>💡 點擊看解析</summary><b>答案：B</b>。
<b>複習重點：</b> NAT Gateway 是私有區的傳聲筒，讓內部能單向上網。</details>

---

### **5. AWS 保留 IP 數量**
**Q：在一個 CIDR 為 /24 的子網路中（總共 256 個 IP），AWS 會保留幾個 IP 無法讓使用者分配？**
* **A.** 2 個。
* **B.** 3 個。
* **C.** 5 個。
* **D.** 1 個。
<details><summary>💡 點擊看解析</summary><b>答案：C</b>。
<b>複習重點：</b> 記死這個數字：每個 Subnet 固定保留 5 個 IP。</details>

---

### **6. 跨區域連線的穩定性**
**Q：公司需要一條從「辦公室機房」到「AWS 雲端」的連線。老闆要求網路延遲必須極低且「非常穩定」，不能受公用網路波動影響。**
* **A.** Site-to-Site VPN。
* **B.** Direct Connect (DX)。
* **C.** VPC Peering。
* **D.** NAT Gateway。
<details><summary>💡 點擊看解析</summary><b>答案：B</b>。
<b>複習重點：</b> 看到「穩定」、「不走公網」就是實體專線 Direct Connect。</details>

---

### **7. VPC Peering 的限制**
**Q：你有三個 VPC：A、B、C。你建立了 A-B 的 Peering，也建立了 B-C 的 Peering。請問 A 能直接連到 C 嗎？**
* **A.** 可以，只要路由表設定好。
* **B.** 不可以，因為 Peering 不支援傳遞性 (Transitive)。
* **C.** 可以，但速度會變慢。
* **D.** 必須經過 Internet Gateway 才能連。
<details><summary>💡 點擊看解析</summary><b>答案：B</b>。
<b>複習重點：</b> Peering 不能借過。A 連 C 必須單獨再蓋一座橋。</details>

---

### **8. 網路 ACL (NACL) 的執行順序**
**Q：在 NACL 規則中，規則編號 100 是「拒絕流量」，規則編號 200 是「允許流量」。請問當流量進來時會發生什麼？**
* **A.** 流量會被允許，因為 200 號規則權限較大。
* **B.** 流量會被拒絕，因為號碼越小優先級越高。
* **C.** 兩者會衝突導致錯誤。
* **D.** 隨機選擇一條執行。
<details><summary>💡 點擊看解析</summary><b>答案：B</b>。
<b>複習重點：</b> NACL 是從小號碼開始跑，一旦符合就不看後面的了。</details>

---

### **9. 便宜的備援連線**
**Q：公司已經有 Direct Connect 專線，但怕線路斷掉，想要一個「低成本、快速部署」的備援路徑。**
* **A.** 再買一條 Direct Connect。
* **B.** 使用 Site-to-Site VPN。
* **C.** 建立 VPC Peering。
* **D.** 增加 NAT Gateway 數量。
<details><summary>💡 點擊看解析</summary><b>答案：B</b>。
<b>複習重點：</b> VPN 雖然走公網不穩，但它是 DX 最常見、最便宜的備胎。</details>

---

### **10. VPC Endpoints 的省錢技巧**
**Q：你想要讓私有子網路的電腦連到 AWS 的其他公共資源，且「不想支付資料處理費」也不想經過 Internet。**
* **A.** Interface Endpoint。
* **B.** Gateway Endpoint。
* **C.** NAT Gateway。
* **D.** Internet Gateway。
<details><summary>💡 點擊看解析</summary><b>答案：B</b>。
<b>複習重點：</b> 只要看到「免費（不收處理費）」連線，指的就是 Gateway 型 Endpoint。</details>

---

### **11. NAT Gateway 應該放在哪？**
**Q：為了讓 Private Subnet 的電腦可以上網，你必須把 NAT Gateway 放在哪個位置？**
* **A.** 放進 Private Subnet。
* **B.** 放進一個有連通 Internet Gateway 的 Public Subnet。
* **C.** 直接放在 VPC 外面。
* **D.** 放在地端辦公室。
<details><summary>💡 點擊看解析</summary><b>答案：B</b>。
<b>複習重點：</b> 傳聲筒（NAT）自己要能對外喊，所以它必須待在有大門（IGW）的客廳（Public 區）。</details>

---

### **12. 預設 Security Group 的規則**
**Q：當你建立一個新的 Security Group 時，它的「預設 Inbound (進入)」規則是什麼？**
* **A.** 允許所有流量。
* **B.** 拒絕所有流量。
* **C.** 允許來自同一 VPC 的流量。
* **D.** 只允許 HTTP 流量。
<details><summary>💡 點擊看解析</summary><b>答案：B</b>。
<b>複習重點：</b> 安全組預設是非常嚴格的，除非你開門，否則誰都進不來（Deny all by default）。</details>

---

### **13. IPv6 的單向上網**
**Q：你的環境全面改用 IPv6。你想要讓私有子網路的主機能對外連線，但不被外人主動攻擊。IPv4 用 NAT，IPv6 該用什麼？**
* **A.** 還是 NAT Gateway。
* **B.** Egress-Only Internet Gateway。
* **C.** 第二個 Internet Gateway。
* **D.** VPC Peering。
<details><summary>💡 點擊看解析</summary><b>答案：B</b>。
<b>複習重點：</b> IPv6 專用的單向出口叫 Egress-Only IGW。</details>

---

### **14. VPC Peering 的前提條件**
**Q：兩個 VPC 要建立 Peering 連線，哪一個條件必須滿足？**
* **A.** 兩邊的 IP (CIDR) 範圍不能重疊。
* **B.** 兩邊必須在同一個 AWS 帳號下。
* **C.** 兩邊必須在同一個可用區 (AZ)。
* **D.** 必須先建立 VPN。
<details><summary>💡 點擊看解析</summary><b>答案：A</b>。
<b>複習重點：</b> 兩個基地的門牌號碼如果一模一樣，郵差會迷路。所以 IP 絕對不能重疊。</details>

---

### **15. 監控網路流量紀錄**
**Q：如果你想檢查有哪些 IP 地址被你的 Network ACL 拒絕了，你該開啟哪個功能？**
* **A.** CloudWatch。
* **B.** VPC Flow Logs。
* **C.** CloudTrail。
* **D.** Config。
<details><summary>💡 點擊看解析</summary><b>答案：B</b>。
<b>複習重點：</b> 看到「網路流量紀錄」、「看誰被擋掉」就找 Flow Logs。</details>