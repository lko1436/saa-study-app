import streamlit as st
import os

# 1. 網頁基本配置
st.set_page_config(page_title="AWS SAA-C03 戰鬥手冊", layout="wide", initial_sidebar_state="expanded")

# 2. 自定義介面樣式 (介面繁體化)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stRadio > label { font-weight: bold; font-size: 18px; color: #1f4e79; }
    .stSelectbox > label { font-weight: bold; font-size: 16px; }
    .exam-header { color: #ff9900; border-bottom: 2px solid #ff9900; padding-bottom: 5px; }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.title("☁️ SAA-C03 核心知識體系")

# 3. 完整的 10 大章節與所有小節索引 (一次補齊)
menu_structure = {
    "0. 雲端造物主 (Blueprint)": {
        "📖 雲端造物主的求生指南": "ch0_blueprint.md"
    },
    "1. VPC 網路設計 (Networking)": {
        "1-1 VPC 基礎與子網路劃分": "ch1_1_vpc_base.md",
        "1-2 網路安全 (SG vs NACL)": "ch1_2_security.md",
        "1-3 混合雲與進階連線 (DX/VPN/Endpoints)": "ch1_3_connectivity.md",
        "🏆 第一章：VPC 網路總結大會考": "ch1_exam.md"
    },
    "2. 彈性運算資源 (Compute)": {
        "2-1 EC2 深度選型與置放群組": "ch2_1_ec2.md",
        "2-2 Auto Scaling 與負載平衡 (ELB)": "ch2_2_asg_elb.md",
        "2-3 Lambda 與 Fargate (Serverless)": "ch2_3_serverless.md",
        "🏆 第二章：運算資源總結大會考": "ch2_exam.md"
    },
    "3. 儲存架構設計 (Storage)": {
        "3-1 S3 十一種九的深度細節": "ch3_1_s3.md",
        "3-2 EBS 性能對比與 EFS 共享儲存": "ch3_2_ebs_efs.md",
        "3-3 存儲遷移 (Snowball/DataSync)": "ch3_3_migration.md",
        "🏆 第三章：儲存架構總結大會考": "ch3_exam.md"
    },
    "4. 關聯式資料庫 (SQL)": {
        "4-1 RDS 基礎與 Multi-AZ 高可用": "ch4_1_rds.md",
        "4-2 Aurora 深度架構與 Serverless": "ch4_2_aurora.md",
        "🏆 第四章：關聯式資料庫總結大會考": "ch4_exam.md"
    },
    "5. 非關聯式與緩存 (NoSQL/Cache)": {
        "5-1 DynamoDB 性能與 DAX 緩存": "ch5_1_dynamodb.md",
        "5-2 ElastiCache (Redis vs Memcached)": "ch5_2_elasticache.md",
        "🏆 第五章：非關聯式與緩存總結大會考": "ch5_exam.md"
    },
    "6. 權限與安全控管 (IAM/Security)": {
        "6-1 IAM 深度解析與權限邊界": "ch6_1_iam.md",
        "6-2 加密與認證 (KMS/Secrets/Cognito)": "ch6_2_auth.md",
        "🏆 第六章：安全控管總結大會考": "ch6_exam.md"
    },
    "7. 邊緣加速與防護 (Edge)": {
        "7-1 CloudFront CDN 與 Route 53 路由": "ch7_1_edge.md",
        "7-2 網路防禦 (WAF/Shield/Global Accelerator)": "ch7_2_protection.md",
        "🏆 第七章：邊緣加速總結大會考": "ch7_exam.md"
    },
    "8. 解耦與自動化 (App Integration)": {
        "8-1 非同步訊息 (SQS/SNS/EventBridge)": "ch8_1_messaging.md",
        "8-2 資源部署與自動化 (CloudFormation/SAM)": "ch8_2_automation.md",
        "🏆 第八章：解耦與自動化總結大會考": "ch8_exam.md"
    },
    "9. 監控、審計與遷移 (Management)": {
        "9-1 監控與日誌 (CloudWatch/CloudTrail)": "ch9_1_monitor.md",
        "9-2 混合雲遷移與分析 (SCT/DMS)": "ch9_2_migration.md",
        "🏆 第九章：監控與遷移總結大會考": "ch9_exam.md"
    },
    "10. 架構設計準則 (WAF/Cost)": {
        "10-1 Well-Architected 六大支柱實踐": "ch10_1_waf.md",
        "10-2 成本優化與組織管理 (Organizations)": "ch10_2_cost.md",
        "🏆 第十章：架構設計總結大會考": "ch10_exam.md"
    }
}

# 4. 側邊欄：一級選單
main_chapter = st.sidebar.selectbox("📂 選擇主模組", list(menu_structure.keys()))

# 5. 側邊欄：二級選單
sub_chapter_list = list(menu_structure[main_chapter].keys())
sub_chapter = st.sidebar.radio("📄 選擇細項小節", sub_chapter_list)

# 6. 讀取並顯示內容
file_name = menu_structure[main_chapter][sub_chapter]
file_path = os.path.join("content", file_name)

if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        st.markdown(f.read(), unsafe_allow_html=True)
else:
    st.title(sub_chapter)
    st.warning(f"目前此章節內容尚未寫入：`{file_name}`")
    st.info("請跟 AI 索取此章節內容，並存入 content 資料夾。")