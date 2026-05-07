# <h1 class="exam-header">🏆 第一章：VPC 網路總結大會考</h1>

這是檢驗你是否掌握「網路設計」模組的最後關卡。請先看題目，在腦中思考答案後再點開解析。

---

### **Q1：IP 容量規劃題**
你正在為公司設計一個新的 VPC 子網路（Subnet），預計需要部署 **12 台** EC2 執行個體。為了節省 IP 空間，你打算使用最小的 CIDR 遮罩。請問以下哪個遮罩最符合需求？

A. `/29` (8 個 IP)  
B. `/28` (16 個 IP)  
C. `/27` (32 個 IP)  
D. `/30` (4 個 IP)

<details>
<summary><b>點擊查看答案與解析</b></summary>
<b>正確答案：B</b><br>
<b>解析：</b> AWS 在每個子網路中會保留 <b>5 個 IP</b>。
- 選項 A (/29)：8 - 5 = 3 (不夠)。
- 選項 B (/28)：16 - 5 = 11 (不夠，因為 11 < 12)。
- <b>等等！</b> 題目要求 12 台，所以 16-5=11 還是不夠。
- <b>正確答案應修正為：C (/27)</b>，32 - 5 = 27 個可用 IP，才能容納 12 台機器。
<i>(這題就是在考你有沒有記得減掉那 5 個保留 IP！)</i>
</details>

---

### **Q2：高可用連網架構 (High Availability)**
你的應用程式部署在兩個可用區 (Multi-AZ) 的 Private Subnets 中，需要透過 NAT Gateway 下載更新。為了確保「其中一個可用區發生故障」時，另一個可用區仍能正常連網，你該如何設計？

A. 在其中一個 Public Subnet 建立一個 NAT Gateway，並讓所有 Private Subnets 指向它。  
B. 在兩個 Public Subnets 各建立一個 NAT Gateway，並分別讓各自 AZ 的路由表指向對應的 NAT Gateway。  
C. 使用 Internet Gateway 代替 NAT Gateway。  
    D. 建立一個 VPC Peering。

<details>
<summary><b>點擊查看答案與解析</b></summary>
<b>正確答案：B</b><br>
<b>解析：</b> NAT Gateway 是單一可用區 (AZ-level) 服務。如果只設一個，當該 AZ 故障時，全公司的 Private Subnet 都會斷網。<b>Multi-AZ 故障轉移必須在每個 AZ 部署獨立的 NAT Gateway。</b>
</details>

---

### **Q3：最省錢連線方案 (Cost-Effective)**
公司有大量數據存儲在 **S3**，部署在 Private Subnet 的 EC2 頻繁需要存取這些數據。公司要求在「不經過公網」且「最低成本」的前提下完成連線，你該選擇？

A. NAT Gateway  
B. S3 Interface Endpoint (PrivateLink)  
C. S3 Gateway Endpoint  
D. Direct Connect

<details>
<summary><b>點擊查看答案與解析</b></summary>
<b>正確答案：C</b><br>
<b>解析：</b> 看到「S3/DynamoDB」+「不經過公網」+「最低成本」，首選一定是 <b>Gateway Endpoint</b>，因為它<b>完全免費</b>。Interface Endpoint 則會按流量收費。
</details>

---

### **Q4：混合雲選型題 (Hybrid Cloud)**
一家跨國企業需要將其地端機房與 AWS VPC 連接。他們要求連線必須具備 **「低延遲 (Low Latency)」** 且 **「頻寬極其穩定 (Consistent Network Experience)」** 以處理每日 10TB 的數據搬運。請問該推薦哪種方案？

A. Site-to-Site VPN  
B. Direct Connect (DX)  
C. AWS Transit Gateway  
D. Client VPN

<details>
<summary><b>點擊查看答案與解析</b></summary>
<b>正確答案：B</b><br>
<b>解析：</b> 關鍵字是「低延遲」與「穩定的頻寬」。VPN 走的是公共網路，速度不穩；只有 <b>Direct Connect (實體專線)</b> 能提供一致且高品質的連線體驗。
</details>

---

### **Q5：安全組 SG 故障排除**
你有一台在 Public Subnet 的 EC2。Security Group 規則如下：
- **Inbound:** Allow Port 80 from 0.0.0.0/0
- **Outbound:** Deny All
此時外部用戶嘗試透過 HTTP 存取網站，會發生什麼事？

A. 無法存取，因為 Outbound 被 Deny。  
B. 可以正常存取，因為 SG 是 Stateful (有狀態)。  
C. 可以正常存取，但需要在 NACL 開放規則。  
D. 無法存取，因為沒有開放 Port 443。

<details>
<summary><b>點擊查看答案與解析</b></summary>
<b>正確答案：B</b><br>
<b>解析：</b> 這是 SG 最核心的考點：<b>Stateful</b>。只要 Inbound 允許進來，回程流量會被自動允許，系統會「忽略」Outbound 規則的 Deny。
</details>